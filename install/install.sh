#!/usr/bin/env bash
# =============================================================
#  CrashServer / live2027_grid — Full Linux Installer
#  Usage: ./install/install.sh [flags]
#    --yes           skip all confirmation prompts
#    --skip-system   skip system package installation
#    --skip-samples  skip sample repository download
#    --optional      also install optional packages (librosa, opencv)
# =============================================================
set -uo pipefail   # pipefail + undefined vars, but NOT -e (we handle failures explicitly)

# ── Colors ─────────────────────────────────────────────────
RED='\033[0;31m'; GREEN='\033[0;32m'; YELLOW='\033[1;33m'
BLUE='\033[0;34m'; CYAN='\033[0;36m'; BOLD='\033[1m'; NC='\033[0m'

# ── Argument parsing ────────────────────────────────────────
SKIP_SYSTEM=false; SKIP_SAMPLES=false; YES=false; OPTIONAL=false
for arg in "$@"; do
  case $arg in
    --yes|-y)         YES=true ;;
    --skip-system)    SKIP_SYSTEM=true ;;
    --skip-samples)   SKIP_SAMPLES=true ;;
    --optional)       OPTIONAL=true ;;
  esac
done

# ── Status tracking ─────────────────────────────────────────
declare -A STATUS

ok()      { echo -e "  ${GREEN}✓${NC}  $1"; STATUS["$2"]="ok"; }
fail()    { echo -e "  ${RED}✗${NC}  $1"; STATUS["$2"]="FAILED"; }
skip()    { echo -e "  ${YELLOW}→${NC}  $1"; STATUS["$2"]="skipped"; }
warn()    { echo -e "  ${YELLOW}⚠${NC}  $1"; }
info()    { echo -e "  ${BLUE}·${NC}  $1"; }
section() { echo -e "\n${BOLD}${CYAN}━━━  $1  ━━━${NC}"; }

confirm() {
  $YES && return 0
  echo -en "  ${YELLOW}?${NC}  $1 [y/N] "
  read -r reply; [[ "$reply" =~ ^[Yy]$ ]]
}

# ── Paths ────────────────────────────────────────────────────
REPO_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SC_QUARKS="$HOME/.local/share/SuperCollider/downloaded-quarks"
SC_EXTENSIONS="$HOME/.local/share/SuperCollider/Extensions"
SAMPLE_PATH="$HOME/UltimateSamples"
VENV_DIR="${REPO_DIR}/venv"
VENV_PIP="${VENV_DIR}/bin/pip"
VENV_PYTHON="${VENV_DIR}/bin/python"

echo -e "\n${BOLD}CrashServer — Full Installer${NC}"
echo -e "  Repo:      ${REPO_DIR}"
echo -e "  Samples:   ${SAMPLE_PATH}"
echo -e "  SC quarks: ${SC_QUARKS}"
echo ""

# =============================================================
#  1. SYSTEM PACKAGES
# =============================================================
section "1 / 8 — System packages"

install_system_packages() {
  if [ -f /etc/arch-release ]; then
    info "Arch Linux detected — using pacman"
    sudo pacman -S --needed --noconfirm \
      supercollider sc3-plugins pipewire-jack git git-lfs python python-pip nodejs npm
  elif [ -f /etc/debian_version ]; then
    info "Debian/Ubuntu detected — using apt"
    sudo apt-get update -q
    sudo apt-get install -y \
      supercollider sc3-plugins jackd2 git git-lfs \
      python3 python3-pip python3-venv nodejs npm
  elif [ -f /etc/fedora-release ]; then
    info "Fedora detected — using dnf"
    # sc3-plugins may need: sudo dnf copr enable ycollet/sixteenh
    sudo dnf install -y \
      supercollider sc3-plugins jack-audio-connection-kit git git-lfs \
      python3 python3-pip nodejs npm
  else
    warn "Unknown distro — install manually:"
    warn "  supercollider, sc3-plugins, jack, git, git-lfs, python3, python3-venv, pip, nodejs, npm"
    STATUS["system_packages"]="skipped (unknown distro)"
    return 1
  fi
}

if $SKIP_SYSTEM; then
  skip "System packages skipped (--skip-system)" "system_packages"
elif confirm "Install/update system packages (supercollider, sc3-plugins, jack, node, python, git-lfs)?"; then
  if install_system_packages; then
    ok "System packages installed" "system_packages"
    git lfs install --system 2>/dev/null || git lfs install || warn "git lfs install failed"
  else
    fail "System package installation failed" "system_packages"
  fi
else
  skip "System packages skipped" "system_packages"
  # Try git lfs install even if skipping packages (may already be installed)
  git lfs install 2>/dev/null || true
fi

# Verify required tools
for cmd in sclang python3 node npm git; do
  if ! command -v "$cmd" &>/dev/null; then
    warn "Required tool not found: $cmd — install it and re-run"
  fi
done

# =============================================================
#  2. NODE — auto-install nvm if needed
# =============================================================
section "2 / 8 — Node.js"

NODE_MAJOR=$(node --version 2>/dev/null | sed 's/v\([0-9]*\).*/\1/' || echo "0")

if [ "$NODE_MAJOR" -ge 18 ]; then
  ok "Node $(node --version) >= v18" "node_version"
else
  warn "Node ${NODE_MAJOR} < 18 (or not found)"
  if confirm "Auto-install nvm + Node 20 LTS?"; then
    info "Installing nvm..."
    curl -fsSL https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.7/install.sh | bash
    export NVM_DIR="$HOME/.nvm"
    # shellcheck source=/dev/null
    [ -s "$NVM_DIR/nvm.sh" ] && source "$NVM_DIR/nvm.sh"
    if nvm install 20 && nvm use 20 && nvm alias default 20; then
      ok "Node $(node --version) installed via nvm" "node_version"
      warn "Add this to ~/.bashrc if not already there:"
      warn '  export NVM_DIR="$HOME/.nvm" && [ -s "$NVM_DIR/nvm.sh" ] && source "$NVM_DIR/nvm.sh"'
    else
      fail "nvm/Node install failed" "node_version"
    fi
  else
    fail "Node < 18 — npm install steps will fail" "node_version"
  fi
fi

info "Installing webTroop dependencies..."
if (cd "${REPO_DIR}/webTroop" && npm install --silent); then
  ok "webTroop npm install" "node_webroop"
else
  fail "webTroop npm install failed" "node_webroop"
fi

info "Installing hub dependencies..."
if (cd "${REPO_DIR}/hub" && npm install --silent); then
  ok "hub npm install" "node_hub"
else
  fail "hub npm install failed" "node_hub"
fi

# =============================================================
#  3. PYTHON VIRTUAL ENVIRONMENT + PACKAGES
# =============================================================
section "3 / 8 — Python venv + packages"

PYTHON_REQUIRED=(
  websockets python-rtmidi pyfiglet pyperclip LinkToPy
  requests numpy edn-format ply pyRFC3339 pytz setuptools monotonic
)
PYTHON_OPTIONAL=(
  librosa        # onset detection (regenOnset.py)
  opencv-python  # webcam feature (webcam.py)
)

if [ -d "${VENV_DIR}" ]; then
  ok "venv already exists at ${VENV_DIR}" "venv"
else
  info "Creating Python venv at ${VENV_DIR}..."
  if python3 -m venv "${VENV_DIR}"; then
    ok "venv created" "venv"
  else
    fail "venv creation failed — on Debian/Ubuntu run: sudo apt install python3-venv" "venv"
    warn "Cannot continue without venv — exiting Python section"
  fi
fi

if [ -x "${VENV_PYTHON}" ]; then
  info "Installing FoxDot Python package (editable)..."
  if "${VENV_PIP}" install -e "${REPO_DIR}/FoxDot" --quiet; then
    ok "FoxDot Python package installed" "foxdot_python"
  else
    fail "FoxDot Python package failed" "foxdot_python"
  fi

  info "Installing required Python dependencies..."
  if "${VENV_PIP}" install "${PYTHON_REQUIRED[@]}" --quiet; then
    ok "Python required packages installed" "python_required"
  else
    fail "Python required packages failed" "python_required"
  fi

  if $OPTIONAL; then
    info "Installing optional Python packages (librosa, opencv)..."
    if "${VENV_PIP}" install "${PYTHON_OPTIONAL[@]}" --quiet; then
      ok "Python optional packages installed" "python_optional"
    else
      warn "Some optional packages failed — non-critical"
      STATUS["python_optional"]="partial"
    fi
  else
    skip "Optional Python packages skipped (pass --optional to include)" "python_optional"
  fi
else
  fail "venv/bin/python not found — skipping Python package installs" "foxdot_python"
  STATUS["python_required"]="skipped (no venv)"
fi

# =============================================================
#  4. SUPERCOLLIDER QUARKS
# =============================================================
section "4 / 8 — SuperCollider quarks"

mkdir -p "$SC_QUARKS"

install_quark() {
  local name="$1"
  local url="$2"
  local dest="${SC_QUARKS}/${name}"
  if [ -d "$dest" ]; then
    info "${name} already installed — pulling latest..."
    if git -C "$dest" pull --quiet 2>/dev/null; then
      ok "${name} updated" "quark_${name}"
    else
      warn "${name} pull failed — using existing version"
      STATUS["quark_${name}"]="ok (existing)"
    fi
  else
    info "Cloning ${name}..."
    if git clone --depth 1 --quiet "$url" "$dest"; then
      ok "${name} installed" "quark_${name}"
    else
      fail "${name} clone failed" "quark_${name}"
    fi
  fi
}

install_quark "BatLib"            "https://github.com/supercollider-quarks/BatLib"
install_quark "Feedback"          "https://github.com/supercollider-quarks/Feedback"
install_quark "miSCellaneous_lib" "https://github.com/dkmayer/miSCellaneous_lib"
install_quark "ddwWavetableSynth" "https://github.com/jamshark70/ddwWavetableSynth"

FOXDOT_QUARK="${SC_QUARKS}/FoxDot"
if [ ! -d "$FOXDOT_QUARK" ]; then
  info "Cloning FoxDot SC quark..."
  if git clone --depth 1 --quiet "https://github.com/Qirky/FoxDotQuark" "$FOXDOT_QUARK"; then
    ok "FoxDot SC quark cloned" "quark_FoxDot_clone"
  else
    fail "FoxDot SC quark clone failed" "quark_FoxDot_clone"
  fi
else
  ok "FoxDot SC quark already present" "quark_FoxDot_clone"
fi

info "Patching FoxDot.sc (stems + MIDI + memory fixes)..."
if cp "${REPO_DIR}/config/FoxDot.sc" "${FOXDOT_QUARK}/FoxDot.sc"; then
  ok "FoxDot.sc patched" "foxdot_sc_patch"
else
  fail "FoxDot.sc patch failed" "foxdot_sc_patch"
fi

# =============================================================
#  5. SUPERCOLLIDER EXTENSIONS
# =============================================================
section "5 / 8 — SuperCollider extensions"

mkdir -p "$SC_EXTENSIONS"

install_extension() {
  local name="$1"
  local src="${REPO_DIR}/config/SC_Extensions/${name}"
  local dest="${SC_EXTENSIONS}/${name}"
  if [ ! -d "$src" ]; then
    warn "Extension source not found: ${src}"
    STATUS["ext_${name}"]="source missing"
    return
  fi
  [ -d "$dest" ] && rm -rf "$dest"
  info "Copying ${name}..."
  if cp -r "$src" "$dest"; then
    ok "${name} installed" "ext_${name}"
  else
    fail "${name} copy failed" "ext_${name}"
  fi
}

install_extension "mi-UGens"      # MiBraids, MiClouds, MiElements, MiPlaits
install_extension "PortedPlugins" # JPverb, Greyhole, SawDPW, DFM1, ...
install_extension "Open303"       # Open303 (TB-303 emulation)

# =============================================================
#  6. SAMPLES
# =============================================================
section "6 / 8 — Samples"

clone_samples() {
  local bank="$1"
  local dest="${SAMPLE_PATH}/${bank}"
  if [ -d "$dest" ]; then
    info "Bank ${bank} already exists — skipping"
    ok "Sample bank ${bank} present" "samples_${bank}"
  else
    info "Cloning sample bank ${bank} (may take a while — several GB)..."
    if GIT_LFS_SKIP_SMUDGE=0 git clone --depth 1 --progress \
        "https://github.com/CrashServer/${bank}" "$dest" 2>&1 | \
        grep -E "Receiving|Resolving|Filtering|done\." || true; then
      ok "Sample bank ${bank} downloaded" "samples_${bank}"
    else
      fail "Sample bank ${bank} download failed" "samples_${bank}"
    fi
  fi
}

if $SKIP_SAMPLES; then
  skip "Samples skipped (--skip-samples)" "samples_0"
  STATUS["samples_1"]="skipped"; STATUS["samples_2"]="skipped"
elif [ -d "$SAMPLE_PATH" ] && [ "$(ls -A "$SAMPLE_PATH" 2>/dev/null)" ]; then
  ok "Samples already present at ${SAMPLE_PATH}" "samples_0"
  STATUS["samples_1"]="ok (existing)"; STATUS["samples_2"]="ok (existing)"
elif confirm "Download samples from GitHub (~8 GB total — banks 0, 1, 2)?"; then
  mkdir -p "$SAMPLE_PATH"
  clone_samples "0"
  clone_samples "1"
  clone_samples "2"
else
  skip "Samples skipped" "samples_0"
  STATUS["samples_1"]="skipped"; STATUS["samples_2"]="skipped"
  warn "Set sample_path in webTroop/crash_config.json once samples are in place"
fi

# =============================================================
#  7. CONFIGURATION
# =============================================================
section "7 / 8 — Configuration"

CONFIG_FILE="${REPO_DIR}/webTroop/crash_config.json"

detect_ip() {
  ip route get 1.1.1.1 2>/dev/null | awk '{for(i=1;i<=NF;i++) if($i=="src") print $(i+1); exit}'
}

LAN_IP=$(detect_ip)

if [ -f "$CONFIG_FILE" ]; then
  # Always sync HOST_IP with current LAN IP — don't leave stale IPs on re-installs
  STORED_IP=$(python3 -c "import json; print(json.load(open('${CONFIG_FILE}'))['HOST_IP'])" 2>/dev/null || echo "")
  if [ -n "$LAN_IP" ] && [ "$LAN_IP" != "$STORED_IP" ]; then
    info "HOST_IP changed: ${STORED_IP} → ${LAN_IP} — updating..."
    python3 - <<PYEOF
import json
with open('${CONFIG_FILE}') as f: cfg = json.load(f)
cfg['HOST_IP'] = '${LAN_IP}'
with open('${CONFIG_FILE}', 'w') as f: json.dump(cfg, f, indent=4)
PYEOF
    ok "HOST_IP updated to ${LAN_IP}" "config"
  else
    ok "crash_config.json up to date (HOST_IP=${STORED_IP})" "config"
  fi
else
  info "Detected LAN IP: ${LAN_IP}"
  cat > "$CONFIG_FILE" <<EOF
{
    "HOST_IP": "${LAN_IP}",
    "FOXDOT_PATH": "${REPO_DIR}/FoxDot",
    "sample_path": "${SAMPLE_PATH}",
    "FOXDOT_WS_PORT": 20000,
    "freesoundApiKey": "REPLACE_WITH_YOUR_KEY",
    "SC_CPU_PORT": 2887,
    "showTodo": 0,
    "ARDUINO": 0
}
EOF
  ok "crash_config.json generated (HOST_IP=${LAN_IP})" "config"
  warn "Edit crash_config.json and set your freesoundApiKey"
fi

# =============================================================
#  8. GENERATE start.sh
# =============================================================
section "8 / 8 — Generating start.sh"

START_SH="${REPO_DIR}/start.sh"
cat > "$START_SH" <<'STARTEOF'
#!/usr/bin/env bash
# CrashServer launcher — generated by install.sh
# Usage: ./start.sh [--no-sc]
# Logs:  logs/ directory

set -uo pipefail
REPO_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
VENV_PYTHON="${REPO_DIR}/venv/bin/python"
LOG_DIR="${REPO_DIR}/logs"
PID_FILE="${REPO_DIR}/.pids"
mkdir -p "$LOG_DIR"

GREEN='\033[0;32m'; CYAN='\033[0;36m'; BOLD='\033[1m'; YELLOW='\033[1;33m'; NC='\033[0m'

HOST_IP=$(${VENV_PYTHON} -c \
  "import json; print(json.load(open('${REPO_DIR}/webTroop/crash_config.json'))['HOST_IP'])" \
  2>/dev/null || echo "localhost")

> "$PID_FILE"

cleanup() {
  echo -e "\n${YELLOW}Stopping CrashServer...${NC}"
  while read -r pid; do kill "$pid" 2>/dev/null || true; done < "$PID_FILE"
  rm -f "$PID_FILE"
  echo "Stopped."
}
trap cleanup EXIT INT TERM

launch() {
  local name="$1"; shift
  "$@" >> "${LOG_DIR}/${name}.log" 2>&1 &
  echo $! >> "$PID_FILE"
  echo -e "  ${GREEN}✓${NC}  ${name} (PID $!)"
}

echo -e "\n${BOLD}Starting CrashServer...${NC}\n"

launch "y-websocket" bash -c \
  "cd '${REPO_DIR}/webTroop' && HOST=0.0.0.0 PORT=4444 YPERSISTENCE=./dbDir \
   node ./node_modules/y-websocket/bin/server.cjs"

launch "server"      bash -c "cd '${REPO_DIR}/webTroop' && node server.js"
launch "vite"        bash -c "cd '${REPO_DIR}/webTroop' && npm run dev"

echo ""
echo -e "  ${BOLD}Web UI:${NC}  ${CYAN}http://${HOST_IP}:3000${NC}"
echo -e "  ${BOLD}Logs:${NC}    ${LOG_DIR}/"
echo ""

if [[ "${@:-}" != *"--no-sc"* ]]; then
  echo -e "  ${YELLOW}Open SuperCollider IDE and load:${NC}"
  echo -e "    ${CYAN}${REPO_DIR}/config/startuplive.scd${NC}"
  echo ""
fi

echo -e "  Press ${BOLD}Ctrl+C${NC} to stop all services\n"
wait
STARTEOF
chmod +x "$START_SH"
ok "start.sh generated at ${START_SH}" "start_sh"

# =============================================================
#  SUMMARY
# =============================================================
echo -e "\n${BOLD}${CYAN}━━━  Installation Summary  ━━━${NC}\n"

ALL_OK=true
for key in \
  system_packages \
  node_version node_webroop node_hub \
  venv foxdot_python python_required python_optional \
  quark_BatLib quark_Feedback quark_miSCellaneous_lib quark_ddwWavetableSynth \
  quark_FoxDot_clone foxdot_sc_patch \
  ext_mi-UGens ext_PortedPlugins ext_Open303 \
  samples_0 samples_1 samples_2 \
  config start_sh; do
  val="${STATUS[$key]:-not run}"
  if [[ "$val" == "ok"* ]]; then
    echo -e "  ${GREEN}✓${NC}  ${key}: ${val}"
  elif [[ "$val" == "skipped"* ]]; then
    echo -e "  ${YELLOW}→${NC}  ${key}: ${val}"
  elif [[ "$val" == "FAILED" ]]; then
    echo -e "  ${RED}✗${NC}  ${key}: ${val}"
    ALL_OK=false
  else
    echo -e "  ${YELLOW}?${NC}  ${key}: ${val}"
  fi
done

echo ""
if $ALL_OK; then
  echo -e "${GREEN}${BOLD}All done!${NC}"
else
  echo -e "${YELLOW}${BOLD}Completed with issues — check failed items above.${NC}"
fi

# =============================================================
#  NEXT STEPS — SC recompile is #1, it's mandatory
# =============================================================
echo -e "\n${BOLD}${RED}⚠  REQUIRED: Recompile SuperCollider class library${NC}"
echo -e "   New quarks + extensions are invisible to SC until you do this."
echo -e "   In SuperCollider IDE:  ${CYAN}Language → Recompile Class Library  (Ctrl+Shift+L)${NC}\n"

echo -e "${BOLD}Next steps:${NC}"
echo -e "  1.  ${RED}Recompile SC class library${NC} (see above — mandatory)"
echo -e "  2.  Open SC IDE and load: ${CYAN}${REPO_DIR}/config/startuplive.scd${NC}"
echo -e "  3.  Start everything:     ${CYAN}${REPO_DIR}/start.sh${NC}"
echo -e "  4.  Set freesoundApiKey in ${CYAN}webTroop/crash_config.json${NC} (optional)"
echo ""

# Auto-run verifier
echo -e "${BOLD}Running post-install verification...${NC}\n"
"${VENV_PYTHON}" "${REPO_DIR}/install/verify.py" 2>/dev/null \
  || python3 "${REPO_DIR}/install/verify.py" \
  || warn "verify.py failed to run — check manually"
echo ""
