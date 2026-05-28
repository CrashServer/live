#!/usr/bin/env bash
# ═══════════════════════════════════════════════════════════════════════════════
#  WebFoxDot — Interactive Installation Script
#  Supports: Arch Linux · Ubuntu · Debian · macOS (Homebrew)
# ═══════════════════════════════════════════════════════════════════════════════

set -euo pipefail

# ── Formatting ─────────────────────────────────────────────────────────────────
BOLD='\033[1m'
DIM='\033[2m'
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[0;33m'
BLUE='\033[0;34m'
CYAN='\033[0;36m'
WHITE='\033[0;37m'
RESET='\033[0m'

TICK="${GREEN}✓${RESET}"
CROSS="${RED}✗${RESET}"
ARROW="${CYAN}▶${RESET}"
WARN="${YELLOW}⚠${RESET}"
INFO="${BLUE}ℹ${RESET}"

PROJECT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# ── Helpers ────────────────────────────────────────────────────────────────────

banner() {
    echo ""
    echo -e "${BOLD}${CYAN}╔═══════════════════════════════════════════════════╗${RESET}"
    echo -e "${BOLD}${CYAN}║          WebFoxDot — Installation                ║${RESET}"
    echo -e "${BOLD}${CYAN}║   browser live coding · scsynth WASM engine      ║${RESET}"
    echo -e "${BOLD}${CYAN}╚═══════════════════════════════════════════════════╝${RESET}"
    echo ""
}

section() {
    echo ""
    echo -e "${BOLD}${WHITE}── $1 ──────────────────────────────────────────────${RESET}"
    echo ""
}

explain() {
    echo -e "  ${DIM}$1${RESET}"
}

ok()   { echo -e "  ${TICK}  $1"; }
fail() { echo -e "  ${CROSS}  $1"; }
warn() { echo -e "  ${WARN}  $1"; }
info() { echo -e "  ${INFO}  $1"; }
step() { echo -e "\n  ${ARROW} ${BOLD}$1${RESET}"; }

ask_yn() {
    # ask_yn "question" [default: y/n]  → returns 0 (yes) or 1 (no)
    local question="$1"
    local default="${2:-y}"
    local prompt
    if [[ "$default" == "y" ]]; then prompt="[Y/n]"; else prompt="[y/N]"; fi
    while true; do
        echo -en "\n  ${CYAN}?${RESET} ${BOLD}${question}${RESET} ${DIM}${prompt}${RESET} "
        read -r reply
        reply="${reply:-$default}"
        case "${reply,,}" in
            y|yes) return 0 ;;
            n|no)  return 1 ;;
            *) echo -e "  ${WARN} Please answer y or n." ;;
        esac
    done
}

ask_input() {
    # ask_input "question" "default_value"  → sets $REPLY
    local question="$1"
    local default="$2"
    echo -en "\n  ${CYAN}?${RESET} ${BOLD}${question}${RESET}"
    [ -n "$default" ] && echo -en " ${DIM}[${default}]${RESET}"
    echo -en " "
    read -r REPLY
    REPLY="${REPLY:-$default}"
}

cmd_exists() { command -v "$1" &>/dev/null; }

pause() {
    echo ""
    echo -en "  ${DIM}Press Enter to continue…${RESET}"
    read -r
}

# ── OS Detection ───────────────────────────────────────────────────────────────

detect_os() {
    OS="unknown"
    PKG=""
    if [[ "$OSTYPE" == "darwin"* ]]; then
        OS="macos"
        PKG="brew"
    elif [ -f /etc/os-release ]; then
        source /etc/os-release
        case "${ID:-}" in
            arch|manjaro|endeavouros|garuda) OS="arch";   PKG="pacman" ;;
            ubuntu)                          OS="ubuntu"; PKG="apt"    ;;
            debian|raspbian)                 OS="debian"; PKG="apt"    ;;
            linuxmint|pop)                   OS="ubuntu"; PKG="apt"    ;;
            fedora)                          OS="fedora"; PKG="dnf"    ;;
            *)
                # Fallback: check for apt or pacman
                if cmd_exists apt;    then OS="debian"; PKG="apt";    fi
                if cmd_exists pacman; then OS="arch";   PKG="pacman"; fi
                ;;
        esac
    fi
}

# ══════════════════════════════════════════════════════════════════════════════
#  MAIN
# ══════════════════════════════════════════════════════════════════════════════

banner

detect_os

echo -e "  Detected OS:  ${BOLD}${OS}${RESET} (package manager: ${PKG:-none detected})"
echo -e "  Project dir:  ${BOLD}${PROJECT_DIR}${RESET}"
echo ""
explain "This script will walk you through each installation step, explain what"
explain "every dependency is for, and let you skip anything you don't need."
explain "Nothing is installed without your confirmation."

pause

# ══════════════════════════════════════════════════════════════════════════════
section "STEP 1 — Python 3"
# ══════════════════════════════════════════════════════════════════════════════

explain "Python 3 runs two things:"
explain "  • serve.py       — the local dev server (sets mandatory CORS headers)"
explain "  • setup_samples.py — builds the sample symlinks + manifest.json"
echo ""

PYTHON_BIN=""
for bin in python3 python; do
    if cmd_exists "$bin" && "$bin" --version 2>&1 | grep -q "Python 3"; then
        PYTHON_BIN="$bin"
        break
    fi
done

if [ -n "$PYTHON_BIN" ]; then
    PYTHON_VER=$("$PYTHON_BIN" --version 2>&1)
    ok "Found: $PYTHON_VER  ($PYTHON_BIN)"
else
    fail "Python 3 not found."
    echo ""
    explain "WebFoxDot needs Python 3.8 or later. Install it with:"
    case "$OS" in
        arch)   explain "  sudo pacman -S python" ;;
        ubuntu|debian) explain "  sudo apt install python3 python3-pip" ;;
        macos)  explain "  brew install python3" ;;
        fedora) explain "  sudo dnf install python3" ;;
        *)      explain "  Install Python 3 from https://python.org" ;;
    esac
    echo ""
    if ask_yn "Install Python 3 now?"; then
        case "$OS" in
            arch)   sudo pacman -S --noconfirm python ;;
            ubuntu|debian) sudo apt-get install -y python3 python3-pip ;;
            macos)  brew install python3 ;;
            fedora) sudo dnf install -y python3 ;;
            *)  echo -e "  ${WARN} Cannot auto-install on this OS. Please install Python 3 manually." ; exit 1 ;;
        esac
        PYTHON_BIN="python3"
        ok "Python 3 installed."
    else
        fail "Python 3 is required. Exiting."
        exit 1
    fi
fi

# ══════════════════════════════════════════════════════════════════════════════
section "STEP 2 — SuperCollider (sclang)"
# ══════════════════════════════════════════════════════════════════════════════

explain "SuperCollider's language runtime (sclang) compiles SynthDef source files"
explain "(.scd) into binary .scsyndef files that the WASM audio engine loads."
explain ""
explain "The compiled .scsyndef files are already included in the repo, so this"
explain "is ONLY needed if you want to add or modify synths/FX."
echo ""

SCLANG_BIN=""
# macOS: SC app might not be in PATH
if [[ "$OS" == "macos" ]]; then
    for candidate in \
        sclang \
        "/Applications/SuperCollider.app/Contents/MacOS/sclang" \
        "/Applications/SuperCollider/SuperCollider.app/Contents/MacOS/sclang"
    do
        if cmd_exists "$candidate" 2>/dev/null || [ -x "$candidate" ]; then
            SCLANG_BIN="$candidate"; break
        fi
    done
else
    cmd_exists sclang && SCLANG_BIN="sclang"
fi

if [ -n "$SCLANG_BIN" ]; then
    SC_VER=$("$SCLANG_BIN" --version 2>&1 | head -1 || echo "version unknown")
    ok "Found: sclang  ($SC_VER)"
else
    warn "sclang not found."
    explain "Pre-compiled SynthDefs are included — you can skip this if you're not"
    explain "planning to write new synths or modify the FX chain."
    echo ""
    if ask_yn "Install SuperCollider now?" "n"; then
        echo ""
        case "$OS" in
            arch)
                explain "Installing from AUR (requires an AUR helper like yay or paru)..."
                if cmd_exists yay; then
                    yay -S --noconfirm supercollider
                elif cmd_exists paru; then
                    paru -S --noconfirm supercollider
                else
                    explain "No AUR helper found. Installing from official repos..."
                    sudo pacman -S --noconfirm supercollider
                fi
                ;;
            ubuntu|debian)
                explain "Adding the KXStudio repo for a recent SuperCollider build..."
                sudo apt-get install -y supercollider supercollider-common
                ;;
            macos)
                if cmd_exists brew; then
                    explain "Installing via Homebrew Cask..."
                    brew install --cask supercollider
                    SCLANG_BIN="/Applications/SuperCollider.app/Contents/MacOS/sclang"
                else
                    explain "Download SuperCollider from: https://supercollider.github.io/download"
                    explain "After installing, sclang will be at:"
                    explain "  /Applications/SuperCollider.app/Contents/MacOS/sclang"
                    explain "Add it to PATH by adding this to ~/.zprofile or ~/.bash_profile:"
                    explain "  export PATH=\"/Applications/SuperCollider.app/Contents/MacOS:\$PATH\""
                fi
                ;;
            fedora)
                sudo dnf install -y supercollider
                ;;
            *)
                explain "Please install SuperCollider from: https://supercollider.github.io/download"
                ;;
        esac
        cmd_exists sclang && SCLANG_BIN="sclang"
        [ -n "$SCLANG_BIN" ] && ok "SuperCollider installed." || warn "sclang still not found — you can add it to PATH later."
    else
        info "Skipping SuperCollider. Pre-compiled SynthDefs will be used as-is."
        SCLANG_BIN=""
    fi
fi

# macOS PATH hint
if [[ "$OS" == "macos" && -z "$SCLANG_BIN" ]]; then
    warn "macOS tip: if SC app is installed but sclang is not in PATH, add:"
    explain "  export PATH=\"/Applications/SuperCollider.app/Contents/MacOS:\$PATH\""
    explain "to your ~/.zprofile (zsh) or ~/.bash_profile (bash)"
fi

# ══════════════════════════════════════════════════════════════════════════════
section "STEP 3 — Samples (FoxDot UltimateSamples bank)"
# ══════════════════════════════════════════════════════════════════════════════

explain "The play() function — FoxDot-style drum pattern strings like:"
explain "  b1 >> play(\"X  o X  o\", amp=0.9, dur=0.5)"
explain "reads audio samples from a FoxDot UltimateSamples bank."
explain ""
explain "setup_samples.py creates symlinks in samples/ pointing to your bank,"
explain "then generates samples/manifest.json mapping characters to buffer IDs."
explain "Without this step, play() will run but produce no sound."
echo ""

SAMPLES_DIR="$PROJECT_DIR/samples"
MANIFEST="$SAMPLES_DIR/manifest.json"

if [ -f "$MANIFEST" ]; then
    EXISTING_COUNT=$(python3 -c "import json; m=json.load(open('$MANIFEST')); print(sum(v['count'] for v in m.values()))" 2>/dev/null || echo "?")
    ok "manifest.json already exists  (${EXISTING_COUNT} buffer slots)"
    explain "This was generated by a previous run. You can regenerate it if your"
    explain "sample bank has moved or changed."
    echo ""
    if ! ask_yn "Regenerate sample manifest?" "n"; then
        info "Keeping existing manifest."
        SKIP_SAMPLES=true
    else
        SKIP_SAMPLES=false
    fi
else
    SKIP_SAMPLES=false
fi

if [ "${SKIP_SAMPLES:-false}" = false ]; then
    explain "Where is your FoxDot sample bank? It should be a directory containing"
    explain "a '0/' subdirectory with folders named a-z, each having lower/ and upper/."
    explain "The default FoxDot install puts it at ~/FoxDot/snd/."
    echo ""

    # Suggest sensible defaults in priority order
    SUGGESTED=""
    for candidate in \
        "$HOME/UltimateSamples" \
        "$HOME/FoxDot/snd" \
        "$HOME/.local/lib/python3/dist-packages/FoxDot/snd" \
        "/usr/lib/python3/dist-packages/FoxDot/snd"
    do
        if [ -d "$candidate/0" ]; then
            SUGGESTED="$candidate"
            break
        fi
    done

    if [ -n "$SUGGESTED" ]; then
        ok "Auto-detected sample bank at: $SUGGESTED"
    else
        warn "Could not auto-detect a sample bank."
        explain "If you don't have one, you can install FoxDot to get the default bank:"
        explain "  pip install FoxDot    # then look in site-packages/FoxDot/snd/"
        explain "Or skip this step — you can run scripts/setup_samples.py later."
    fi

    ask_input "Path to sample bank root" "${SUGGESTED:-}"
    SAMPLE_PATH="$REPLY"

    if [ -z "$SAMPLE_PATH" ]; then
        info "No path entered — skipping sample setup."
        info "Run later:  python3 scripts/setup_samples.py --sample-path /your/path"
    elif [ ! -d "$SAMPLE_PATH" ]; then
        warn "Directory not found: $SAMPLE_PATH"
        info "Skipping sample setup. Run later:"
        info "  python3 scripts/setup_samples.py --sample-path \"$SAMPLE_PATH\""
    else
        ask_input "Sample bank sub-directory (the numbered bank)" "0"
        BANK="$REPLY"

        step "Running setup_samples.py..."
        explain ""
        if "$PYTHON_BIN" "$PROJECT_DIR/scripts/setup_samples.py" \
            --sample-path "$SAMPLE_PATH" --bank "$BANK"; then
            ok "Sample manifest generated."
        else
            warn "setup_samples.py failed. Check the path and bank number."
            info "You can retry later: python3 scripts/setup_samples.py --sample-path \"$SAMPLE_PATH\""
        fi
    fi
fi

# ══════════════════════════════════════════════════════════════════════════════
section "STEP 4 — Compile SynthDefs"
# ══════════════════════════════════════════════════════════════════════════════

explain "SynthDefs are SuperCollider synthesis programs (.scd source files)"
explain "compiled to binary .scsyndef files. The WASM audio engine loads these"
explain "at boot — it cannot read raw .scd source."
explain ""
explain "Pre-compiled files for all built-in synths are already in:"
explain "  synthdefs/compiled/"
explain ""
explain "You only need to recompile if you:"
explain "  • Modified an existing synth or FX"
explain "  • Added a new synth (see docs panel → Guide tab)"
echo ""

COMPILED_DIR="$PROJECT_DIR/synthdefs/compiled"
COMPILED_COUNT=$(ls "$COMPILED_DIR"/*.scsyndef 2>/dev/null | wc -l)
ok "$COMPILED_COUNT pre-compiled .scsyndef files found in synthdefs/compiled/"
echo ""

if [ -z "$SCLANG_BIN" ]; then
    info "sclang not available — skipping recompilation (pre-compiled files will be used)."
else
    if ask_yn "Recompile all SynthDefs now?" "n"; then
        step "Compiling all SynthDefs..."
        explain ""
        cd "$PROJECT_DIR"
        if bash scripts/build.sh; then
            ok "All SynthDefs compiled."
        else
            warn "Compilation had errors. Check sclang output above."
        fi
    else
        info "Using pre-compiled SynthDefs."
    fi
fi

# ══════════════════════════════════════════════════════════════════════════════
section "STEP 5 — Web Server"
# ══════════════════════════════════════════════════════════════════════════════

explain "WebFoxDot CANNOT be opened as a file:// URL. The browser blocks"
explain "SharedArrayBuffer (required by the WASM audio engine) unless the page"
explain "is served with two specific HTTP headers:"
explain ""
explain "  Cross-Origin-Opener-Policy:   same-origin"
explain "  Cross-Origin-Embedder-Policy: require-corp"
explain ""
explain "serve.py is the zero-dependency dev server that sets these headers."
explain "For production, any web server with those headers added will work."
echo ""

echo -e "  ${BOLD}Options:${RESET}"
echo ""
echo -e "  ${CYAN}1${RESET}  serve.py     Local Python dev server on port 8765 (recommended, no setup)"
echo -e "  ${CYAN}2${RESET}  Nginx        Production-grade reverse proxy (needs nginx installed)"
echo -e "  ${CYAN}3${RESET}  Caddy        Modern server with auto-HTTPS (needs caddy installed)"
echo -e "  ${CYAN}4${RESET}  Apache       Traditional server (needs httpd/apache2 installed)"
echo -e "  ${CYAN}5${RESET}  Skip         I'll configure the server myself"
echo ""
echo -en "  ${CYAN}?${RESET} ${BOLD}Which server do you want to use?${RESET} ${DIM}[1]${RESET} "
read -r SERVER_CHOICE
SERVER_CHOICE="${SERVER_CHOICE:-1}"

case "$SERVER_CHOICE" in
1)  # serve.py — nothing to install
    ok "serve.py selected. Start the server with:"
    echo ""
    echo -e "    ${BOLD}cd ${PROJECT_DIR}${RESET}"
    echo -e "    ${BOLD}python3 serve.py${RESET}"
    echo ""
    echo -e "  Then open: ${BOLD}http://127.0.0.1:8765${RESET}"
    ;;
2)  # Nginx config
    echo ""
    explain "Here is an Nginx server block you can drop into"
    explain "/etc/nginx/sites-available/webfoxdot and symlink to sites-enabled/:"
    echo ""
    cat << 'NGINX'
    server {
        listen 80;
        server_name your.domain.com;   # or localhost
        root /path/to/supersonic-proto;
        index index.html;

        # Required for SharedArrayBuffer / WASM threads
        add_header Cross-Origin-Opener-Policy   "same-origin"  always;
        add_header Cross-Origin-Embedder-Policy "require-corp" always;
        add_header Cache-Control                "no-store"     always;

        location / { try_files $uri $uri/ =404; }

        # Serve compiled SynthDefs as binary
        location ~* \.scsyndef$ { default_type application/octet-stream; }
    }
NGINX
    echo ""
    explain "Replace 'your.domain.com' and the root path, then:"
    explain "  sudo ln -s /etc/nginx/sites-available/webfoxdot /etc/nginx/sites-enabled/"
    explain "  sudo nginx -t && sudo systemctl reload nginx"
    ;;
3)  # Caddy config
    echo ""
    explain "Add this to your Caddyfile (/etc/caddy/Caddyfile):"
    echo ""
    cat << 'CADDY'
    your.domain.com {
        root * /path/to/supersonic-proto
        file_server
        header {
            Cross-Origin-Opener-Policy   "same-origin"
            Cross-Origin-Embedder-Policy "require-corp"
            Cache-Control                "no-store"
        }
    }
CADDY
    echo ""
    explain "Caddy handles HTTPS automatically with Let's Encrypt."
    explain "After editing: sudo systemctl reload caddy"
    ;;
4)  # Apache config
    echo ""
    explain "Add a VirtualHost block to your Apache config:"
    echo ""
    cat << 'APACHE'
    <VirtualHost *:80>
        DocumentRoot /path/to/supersonic-proto
        ServerName your.domain.com

        <Directory /path/to/supersonic-proto>
            Options Indexes FollowSymLinks
            AllowOverride None
            Require all granted
        </Directory>

        Header always set Cross-Origin-Opener-Policy   "same-origin"
        Header always set Cross-Origin-Embedder-Policy "require-corp"
        Header always set Cache-Control                "no-store"

        AddType application/octet-stream .scsyndef .wasm
    </VirtualHost>
APACHE
    echo ""
    explain "Make sure mod_headers is enabled:  sudo a2enmod headers"
    explain "Then: sudo systemctl reload apache2"
    ;;
5)
    info "Skipping server setup."
    info "Remember to add the two CORS headers to whatever server you use."
    ;;
esac

# ══════════════════════════════════════════════════════════════════════════════
section "STEP 6 — Quick verification"
# ══════════════════════════════════════════════════════════════════════════════

step "Checking project structure..."

ERRORS=0
for f in \
    "index.html" \
    "serve.py" \
    "js/engine/player.js" \
    "js/engine/clock.js" \
    "js/synths/registry.js" \
    "js/fx/registry.js" \
    "synthdefs/compiled/fd_dbass.scsyndef" \
    "synthdefs/compiled/fd_fx_chain.scsyndef" \
    "synthdefs/compiled/fd_sampler.scsyndef"
do
    if [ -f "$PROJECT_DIR/$f" ]; then
        ok "$f"
    else
        fail "MISSING: $f"
        ERRORS=$((ERRORS + 1))
    fi
done

echo ""

if [ -f "$PROJECT_DIR/samples/manifest.json" ]; then
    ok "samples/manifest.json"
else
    warn "samples/manifest.json missing — play() will boot but produce no sound"
    info "Fix: python3 scripts/setup_samples.py --sample-path /your/sample/bank"
fi

# ══════════════════════════════════════════════════════════════════════════════
section "STEP 7 — Start server now?"
# ══════════════════════════════════════════════════════════════════════════════

if [ "$ERRORS" -gt 0 ]; then
    warn "$ERRORS required file(s) missing — please check the errors above."
fi

if [ "$SERVER_CHOICE" = "1" ]; then
    if ask_yn "Start serve.py now on port 8765?"; then
        echo ""
        ok "Starting server..."
        echo ""
        echo -e "  ${BOLD}Open in browser:  http://127.0.0.1:8765${RESET}"
        echo -e "  ${DIM}Press Ctrl+C to stop.${RESET}"
        echo ""
        cd "$PROJECT_DIR"
        exec "$PYTHON_BIN" serve.py
    fi
fi

# ══════════════════════════════════════════════════════════════════════════════
section "Installation complete"
# ══════════════════════════════════════════════════════════════════════════════

echo -e "  ${BOLD}Quick start:${RESET}"
echo ""
echo -e "    cd ${PROJECT_DIR}"
echo -e "    python3 serve.py"
echo -e "    ${DIM}# open http://127.0.0.1:8765${RESET}"
echo ""
echo -e "  ${BOLD}Add a synth:${RESET}"
echo -e "    ${DIM}1. Write  synthdefs/src/synths/mysynth.scd${RESET}"
echo -e "    ${DIM}2. Run    ./scripts/build.sh mysynth${RESET}"
echo -e "    ${DIM}3. Add to js/synths/registry.js + SYNTHDEFS_TO_LOAD in index.html${RESET}"
echo ""
echo -e "  ${BOLD}Docs:${RESET}  Press ${CYAN}F1${RESET} inside the app for the built-in reference"
echo ""
