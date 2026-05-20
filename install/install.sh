#!/usr/bin/env bash
# =============================================================
#  CrashServer / live2027_grid — Full Linux Installer
#  Usage: ./install/install.sh [flags]
#    --yes           skip all confirmation prompts
#    --skip-system   skip system package installation
#    --skip-samples  skip sample repository download
#    --optional      also install optional packages (librosa, opencv)
# =============================================================
set -euo pipefail

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
echo -e "  Repo:     ${REPO_DIR}"
echo -e "  Samples:  ${SAMPLE_PATH}"
echo -e "  SC quarks: ${SC_QUARKS}"
echo ""

# =============================================================
#  1. SYSTEM PACKAGES
# =============================================================
section "1 / 7 — System packages"

install_system_packages() {
  if [ -f /etc/arch-release ]; then
    info "Arch Linux detected — using pacman"
    sudo pacman -S --needed --noconfirm \
      supercollider sc3-plugins pipewire-jack git python python-pip nodejs npm
  elif [ -f /etc/debian_version ]; then
    info "Debian/Ubuntu detected — using apt"
    sudo apt-get update -q
    sudo apt-get install -y \
      supercollider sc3-plugins jackd2 git python3 python3-pip nodejs npm
  elif [ -f /etc/fedora-release ]; then
    info "Fedora detected — using dnf"
    sudo dnf install -y \
      supercollider sc3-plugins jack-audio-connection-kit git python3 python3-pip nodejs npm
  else
    warn "Unknown distro — please install manually:"
    warn "  supercollider, sc3-plugins, jack, git, python3, pip, nodejs, npm"
    STATUS["system_packages"]="skipped (unknown distro)"
    return
  fi
}

if $SKIP_SYSTEM; then
  skip "System packages skipped (--skip-system)" "system_packages"
elif confirm "Install/update system packages (supercollider, sc3-plugins, jack, node, python)?"; then
  if install_system_packages; then
    ok "System packages installed" "system_packages"
  else
    fail "System package installation failed" "system_packages"
  fi
else
  skip "System packages skipped" "system_packages"
fi

# Verify required tools are present
for cmd in sclang python3 pip3 node npm git; do
  if ! command -v "$cmd" &>/dev/null; then
    warn "Required tool not found: $cmd"
  fi
done

# =============================================================
#  2. PYTHON VIRTUAL ENVIRONMENT + PACKAGES
# =============================================================
section "2 / 7 — Python venv + packages"

PYTHON_REQUIRED=(
  websockets
  python-rtmidi
  pyfiglet
  pyperclip
  LinkToPy
  requests
  numpy
  edn-format
  ply
  pyRFC3339
  pytz
  setuptools
  monotonic
)

PYTHON_OPTIONAL=(
  librosa          # onset detection (regenOnset.py)
  opencv-python    # webcam feature (webcam.py)
)

# Create venv if not already present
if [ -d "${VENV_DIR}" ]; then
  ok "venv already exists at ${VENV_DIR}" "venv"
else
  info "Creating Python venv at ${VENV_DIR}..."
  if python3 -m venv "${VENV_DIR}"; then
    ok "venv created" "venv"
  else
    fail "venv creation failed — check python3-venv is installed" "venv"
    exit 1
  fi
fi

info "Installing FoxDot Python package into venv (editable)..."
if "${VENV_PIP}" install -e "${REPO_DIR}/FoxDot" --quiet; then
  ok "FoxDot Python package installed" "foxdot_python"
else
  fail "FoxDot Python package failed" "foxdot_python"
fi

info "Installing required Python dependencies into venv..."
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

# =============================================================
#  3. NODE PACKAGES
# =============================================================
section "3 / 7 — Node packages"

# Check Node version
NODE_MAJOR=$(node --version 2>/dev/null | sed 's/v\([0-9]*\).*/\1/' || echo "0")
if [ "$NODE_MAJOR" -lt 18 ]; then
  warn "Node $(node --version) < v18. Install nvm + Node 20:"
  warn "  curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.7/install.sh | bash"
  warn "  source ~/.bashrc && nvm install 20 && nvm use 20"
  STATUS["node_version"]="needs upgrade"
else
  ok "Node $(node --version) >= v18" "node_version"
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
#  4. SUPERCOLLIDER QUARKS
# =============================================================
section "4 / 7 — SuperCollider quarks"

mkdir -p "$SC_QUARKS"

install_quark() {
  local name="$1"
  local url="$2"
  local dest="${SC_QUARKS}/${name}"
  if [ -d "$dest" ]; then
    info "${name} already installed — pulling latest..."
    git -C "$dest" pull --quiet && ok "${name} updated" "quark_${name}" \
      || warn "${name} pull failed (skipping)"
  else
    info "Cloning ${name}..."
    if git clone --depth 1 --quiet "$url" "$dest"; then
      ok "${name} installed" "quark_${name}"
    else
      fail "${name} clone failed" "quark_${name}"
    fi
  fi
}

install_quark "BatLib"           "https://github.com/supercollider-quarks/BatLib"
install_quark "Feedback"         "https://github.com/supercollider-quarks/Feedback"
install_quark "miSCellaneous_lib" "https://github.com/dkmayer/miSCellaneous_lib"
install_quark "ddwWavetableSynth" "https://github.com/jamshark70/ddwWavetableSynth"

# FoxDot SC quark (install then patch)
FOXDOT_QUARK="${SC_QUARKS}/FoxDot"
if [ ! -d "$FOXDOT_QUARK" ]; then
  info "Cloning FoxDot SC quark..."
  git clone --depth 1 --quiet "https://github.com/Qirky/FoxDotQuark" "$FOXDOT_QUARK" \
    && ok "FoxDot SC quark cloned" "quark_FoxDot_clone" \
    || fail "FoxDot SC quark clone failed" "quark_FoxDot_clone"
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
section "5 / 7 — SuperCollider extensions"

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
  # Remove stale dest first — cp -r into an existing dir creates a subdir
  [ -d "$dest" ] && rm -rf "$dest"
  info "Copying ${name}..."
  if cp -r "$src" "$dest"; then
    ok "${name} installed" "ext_${name}"
  else
    fail "${name} copy failed" "ext_${name}"
  fi
}

install_extension "mi-UGens"      # MiBraids, MiClouds, MiElements, MiPlaits
install_extension "PortedPlugins"  # JPverb, Greyhole, SawDPW, DFM1, ...
install_extension "Open303"        # Open303 (TB-303 emulation)

# =============================================================
#  6. SAMPLES
# =============================================================
section "6 / 7 — Samples"

clone_samples() {
  local bank="$1"
  local dest="${SAMPLE_PATH}/${bank}"
  if [ -d "$dest" ]; then
    info "Bank ${bank} already exists — skipping clone"
    ok "Sample bank ${bank} present" "samples_${bank}"
  else
    info "Cloning sample bank ${bank} (this may take a while — several GB)..."
    if git clone --depth 1 --quiet "https://github.com/CrashServer/${bank}" "$dest"; then
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
  ok "Samples directory already populated at ${SAMPLE_PATH}" "samples_0"
  STATUS["samples_1"]="ok (existing)"; STATUS["samples_2"]="ok (existing)"
elif confirm "Download samples from GitHub (~8 GB total for banks 0, 1, 2)?"; then
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
section "7 / 7 — Configuration"

CONFIG_FILE="${REPO_DIR}/webTroop/crash_config.json"

detect_ip() {
  ip route get 1.1.1.1 2>/dev/null | awk '{for(i=1;i<=NF;i++) if($i=="src") print $(i+1); exit}'
}

if [ -f "$CONFIG_FILE" ]; then
  ok "crash_config.json already exists — not overwriting" "config"
  warn "Current HOST_IP: $(python3 -c "import json; print(json.load(open('${CONFIG_FILE}'))['HOST_IP'])" 2>/dev/null || echo '?')"
  warn "Run: python3 install/verify.py  to check if HOST_IP is still correct"
else
  LAN_IP=$(detect_ip)
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
fi

# =============================================================
#  SUMMARY
# =============================================================
echo -e "\n${BOLD}${CYAN}━━━  Installation Summary  ━━━${NC}\n"

ALL_OK=true
for key in \
  system_packages foxdot_python python_required python_optional \
  node_version node_webroop node_hub \
  quark_BatLib quark_Feedback quark_miSCellaneous_lib quark_ddwWavetableSynth \
  quark_FoxDot_clone foxdot_sc_patch \
  ext_mi-UGens ext_PortedPlugins ext_Open303 \
  samples_0 samples_1 samples_2 config; do
  val="${STATUS[$key]:-not run}"
  if [[ "$val" == "ok" || "$val" == "ok (existing)" ]]; then
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
  echo -e "${GREEN}${BOLD}All done!${NC} Run ${CYAN}python3 install/verify.py${NC} to confirm everything works."
else
  echo -e "${YELLOW}${BOLD}Completed with issues.${NC} Check failed items above, then re-run."
fi

echo -e "\n${BOLD}Next steps:${NC}"
echo -e "  1.  Edit ${CYAN}webTroop/crash_config.json${NC} — set HOST_IP, freesoundApiKey"
echo -e "  2.  Recompile SC class library:  ${CYAN}sclang → Ctrl+Shift+L${NC}"
echo -e "  3.  Start SuperCollider with:    ${CYAN}config/startuplive.scd${NC}"
echo -e "  4.  Start webTroop:              ${CYAN}cd webTroop && node server.js${NC}"
echo -e "  5.  Start Vite:                  ${CYAN}cd webTroop && npm run dev${NC}"
echo -e "  6.  Start Y-WebSocket:           ${CYAN}cd webTroop && HOST=0.0.0.0 PORT=4444 node ./node_modules/y-websocket/bin/server.cjs${NC}"
echo ""
