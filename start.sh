#!/usr/bin/env bash
# ═══════════════════════════════════════════════════════════════════════════════
#  CrashFoxDot — Unified Launcher & Installer
#
#  Usage:
#    ./start.sh                    interactive menu
#    ./start.sh start [--no-sc]    start all webTroop services
#    ./start.sh stop               stop all services
#    ./start.sh status             service + version status
#    ./start.sh restart [svc]      restart all, or one: grid | webfoxdot | sc
#    ./start.sh sc [start|stop]    launch SuperCollider headless via sclang
#    ./start.sh webfoxdot          start WebFoxDot browser environment (port 8765)
#    ./start.sh install            installation menu
#    ./start.sh install webfoxdot  run supersonic-proto/install.sh
#    ./start.sh install all        run install/install.sh (full system)
# ═══════════════════════════════════════════════════════════════════════════════

set -uo pipefail

REPO_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
VENV_PYTHON="${REPO_DIR}/venv/bin/python"
LOG_DIR="${REPO_DIR}/logs"
PID_FILE="${REPO_DIR}/.pids"
WEBFOXDOT_DIR="${REPO_DIR}/supersonic-proto"
WEBFOXDOT_PID="${REPO_DIR}/.pids.webfoxdot"
SC_PID_FILE="${REPO_DIR}/.pids.sc"
SC_STARTUP="${REPO_DIR}/config/startuplive_headless.scd"
SC_BOOT_DELAY="${SC_BOOT_DELAY:-2}"  # seconds to wait inside SC after boot before StageLimiter

mkdir -p "$LOG_DIR"

# ── Colors ─────────────────────────────────────────────────────────────────────

BOLD='\033[1m'; DIM='\033[2m'
RED='\033[0;31m'; GREEN='\033[0;32m'; YELLOW='\033[1;33m'
CYAN='\033[0;36m'; BLUE='\033[0;34m'; GRAY='\033[0;90m'
WHITE='\033[0;37m'; NC='\033[0m'

TICK="${GREEN}✓${NC}"; CROSS="${RED}✗${NC}"
ARROW="${CYAN}▶${NC}"; WARN="${YELLOW}⚠${NC}"

# ── Helpers ────────────────────────────────────────────────────────────────────

port_pids() { lsof -ti:"$1" 2>/dev/null || true; }
port_up()   { [[ -n "$(port_pids "$1")" ]] && echo "yes" || echo "no"; }

kill_port() {
    local port=$1 label=${2:-port $1}
    local pids; pids=$(port_pids "$port")
    if [[ -n "$pids" ]]; then
        echo -e "  ${GRAY}killing stale ${label} (port ${port}, PID ${pids})${NC}"
        echo "$pids" | xargs kill 2>/dev/null || true
        sleep 0.4
    fi
}

wait_for_ports() {
    local ports=("$@"); local max=20
    printf "${GRAY}  waiting"
    for ((i=0; i<max; i++)); do
        local all=true
        for p in "${ports[@]}"; do [[ -z "$(port_pids "$p")" ]] && all=false && break; done
        $all && { echo -e " ready${NC}"; return 0; }
        sleep 0.5; printf "."
    done
    echo -e " (still starting)${NC}"
}

header() {
    echo ""
    echo -e "${BOLD}${CYAN}╔═══════════════════════════════════════════════════╗${NC}"
    printf "${BOLD}${CYAN}║${NC}  ${BOLD}%-49s${NC}${BOLD}${CYAN}║${NC}\n" "$1"
    echo -e "${BOLD}${CYAN}╚═══════════════════════════════════════════════════╝${NC}"
    echo ""
}

section() { echo -e "\n${BOLD}${WHITE}── $1${NC}"; echo ""; }

# ── HOST_IP detection & update ─────────────────────────────────────────────────

update_host_ip() {
    local current_ip
    current_ip=$(python3 -c \
        "import json; print(json.load(open('${REPO_DIR}/webTroop/crash_config.json'))['HOST_IP'])" \
        2>/dev/null || echo "localhost")

    local actual_ip
    actual_ip=$(ip route get 8.8.8.8 2>/dev/null \
        | awk '/src/{for(i=1;i<=NF;i++) if($i=="src") print $(i+1)}' | head -1)
    actual_ip="${actual_ip:-$(hostname -I 2>/dev/null | awk '{print $1}')}"

    HOST_IP="$current_ip"
    if [[ -n "$actual_ip" && "$actual_ip" != "$current_ip" ]]; then
        echo -e "${WARN}  HOST_IP in crash_config.json is ${RED}${current_ip}${NC}, actual LAN IP is ${GREEN}${actual_ip}${NC}"
        printf "  ${CYAN}Auto-update? [Y/n]${NC} "; read -r -t 5 ans || ans="y"
        if [[ "${ans,,}" != "n" ]]; then
            sed -i "s/\"HOST_IP\": \"${current_ip}\"/\"HOST_IP\": \"${actual_ip}\"/" \
                "${REPO_DIR}/webTroop/crash_config.json"
            HOST_IP="$actual_ip"
            echo -e "  ${TICK}  Updated to ${GREEN}${HOST_IP}${NC}\n"
        else
            echo -e "  ${GRAY}Keeping ${current_ip}.${NC}\n"
        fi
    fi
}

# ── Status display ─────────────────────────────────────────────────────────────

show_status() {
    section "Services"
    local -a services=(
        "y-websocket:4444"
        "webTroop server:1234"
        "Vite dev:3000"
        "grid serve:1235"
        "WebFoxDot:8765"
        "scsynth (SC):57110"
    )
    for svc in "${services[@]}"; do
        local name="${svc%%:*}"
        local port="${svc##*:}"
        local pids; pids=$(port_pids "$port")
        printf "    %-22s ${GRAY}:%s${NC}  " "${name}" "${port}"
        if [[ -n "$pids" ]]; then
            echo -e "${GREEN}UP${NC}  ${GRAY}PID ${pids}${NC}"
        else
            echo -e "${RED}DOWN${NC}"
        fi
    done

    section "Versions"
    local py_ver; py_ver=$(python3 --version 2>/dev/null || echo "not found")
    local node_ver; node_ver=$(node --version 2>/dev/null || echo "not found")
    local npm_ver; npm_ver=$(npm --version 2>/dev/null | sed 's/^/v/' || echo "not found")
    local sc_ver; sc_ver=$(sclang --version 2>/dev/null | head -1 || echo "not found")
    local venv_ok; venv_ok=$([[ -f "$VENV_PYTHON" ]] && echo "${GREEN}present${NC}" || echo "${RED}missing — run ./start.sh install all${NC}")

    printf "    %-22s %s\n" "Python" "$py_ver"
    printf "    %-22s %s\n" "Node.js" "$node_ver"
    printf "    %-22s %s\n" "npm" "$npm_ver"
    printf "    %-22s %s\n" "sclang" "$sc_ver"
    echo -e "    venv                   ${venv_ok}"

    if [[ -f "${WEBFOXDOT_DIR}/lib/dist/supersonic.js" ]]; then
        local ss_size; ss_size=$(du -sh "${WEBFOXDOT_DIR}/lib/dist/supersonic.js" 2>/dev/null | cut -f1)
        echo -e "    SuperSonic WASM        ${GREEN}present${NC} ${GRAY}(${ss_size})${NC}"
    else
        echo -e "    SuperSonic WASM        ${RED}missing — run ./start.sh install webfoxdot${NC}"
    fi

    local sc_compiled
    sc_compiled=$(ls "${WEBFOXDOT_DIR}/synthdefs/compiled/"*.scsyndef 2>/dev/null | wc -l | tr -d ' ')
    echo -e "    WebFoxDot synthdefs     ${CYAN}${sc_compiled}${NC} compiled"

    if [[ -f "${REPO_DIR}/webTroop/crash_config.json" ]]; then
        local host_ip; host_ip=$(python3 -c \
            "import json; print(json.load(open('${REPO_DIR}/webTroop/crash_config.json'))['HOST_IP'])" \
            2>/dev/null || echo "?")
        echo -e "    HOST_IP                ${CYAN}${host_ip}${NC}"
    fi
    echo ""
}

# ── Launch helper ──────────────────────────────────────────────────────────────

launch() {
    local name="$1"; shift
    "$@" >> "${LOG_DIR}/${name}.log" 2>&1 &
    echo $! >> "$PID_FILE"
    echo -e "  ${TICK}  ${name} ${GRAY}(PID $!)${NC}"
}

cleanup() {
    echo -e "\n${YELLOW}Stopping CrashFoxDot...${NC}"
    if [[ -f "$PID_FILE" ]]; then
        while read -r pid; do kill "$pid" 2>/dev/null || true; done < "$PID_FILE"
        rm -f "$PID_FILE"
    fi
    if [[ -f "$WEBFOXDOT_PID" ]]; then
        while read -r pid; do kill "$pid" 2>/dev/null || true; done < "$WEBFOXDOT_PID"
        rm -f "$WEBFOXDOT_PID"
    fi
    echo -e "Stopped. ${GRAY}(SuperCollider kept running)${NC}"
}

# ── Start webTroop stack ───────────────────────────────────────────────────────

do_start() {
    local no_sc=false
    [[ "${*:-}" == *"--no-sc"* ]] && no_sc=true

    update_host_ip

    echo -e "${YELLOW}Clearing stale instances:${NC}"
    kill_port 4444  "y-websocket"
    kill_port 1234  "webTroop server"
    kill_port 3000  "Vite"
    kill_port 1235  "grid serve"
    echo ""

    > "$PID_FILE"
    trap cleanup EXIT INT TERM

    echo -e "${CYAN}Launching webTroop services:${NC}"
    launch "y-websocket" bash -c \
        "cd '${REPO_DIR}/webTroop' && HOST=0.0.0.0 PORT=4444 YPERSISTENCE=./dbDir \
         node ./node_modules/y-websocket/bin/server.cjs"
    launch "server"     bash -c "cd '${REPO_DIR}/webTroop' && node server.js"
    launch "vite"       bash -c "cd '${REPO_DIR}/webTroop' && npm run dev"
    launch "grid-serve" bash -c "cd '${REPO_DIR}/grid' && '${VENV_PYTHON}' serve.py"

    echo ""
    echo -e "  ${BOLD}Web IDE (local):${NC}   ${CYAN}http://localhost:3000${NC}"
    echo -e "  ${BOLD}Web IDE (LAN):${NC}     ${CYAN}http://${HOST_IP}:3000${NC}"
    echo -e "  ${BOLD}Grid UI:${NC}           ${CYAN}http://localhost:1235${NC}"
    echo -e "  ${BOLD}Logs:${NC}              ${LOG_DIR}/"
    echo ""

    if ! $no_sc; then
        echo -e "  ${YELLOW}Open SuperCollider IDE and load:${NC}"
        echo -e "    ${CYAN}${REPO_DIR}/config/startuplive.scd${NC}"
        echo ""
    fi
}

# ── SuperCollider via sclang (headless) ───────────────────────────────────────

do_start_sc() {
    if ! command -v sclang &>/dev/null; then
        echo -e "  ${CROSS}  sclang not found. Install SuperCollider first."
        return 1
    fi

    # Kill any running scsynth / sclang instances we launched
    if [[ -f "$SC_PID_FILE" ]]; then
        while read -r pid; do kill "$pid" 2>/dev/null || true; done < "$SC_PID_FILE"
        rm -f "$SC_PID_FILE"
        sleep 0.5
    fi
    # Also clean up any leftover scsynth on its default OSC port
    local syn_pids; syn_pids=$(port_pids 57110)
    if [[ -n "$syn_pids" ]]; then
        echo -e "  ${GRAY}killing stale scsynth (port 57110, PID ${syn_pids})${NC}"
        echo "$syn_pids" | xargs kill 2>/dev/null || true
        sleep 0.5
    fi

    # Patch SC_BOOT_DELAY into the scd script if different from default
    local tmpscript; tmpscript=$(mktemp /tmp/crashfoxdot_sc_XXXXXX.scd)
    sed "s/2\.wait/${SC_BOOT_DELAY}.wait/" "$SC_STARTUP" > "$tmpscript"

    > "$SC_PID_FILE"
    sclang "$tmpscript" >> "${LOG_DIR}/sclang.log" 2>&1 &
    local sc_pid=$!
    echo $sc_pid >> "$SC_PID_FILE"
    echo -e "  ${TICK}  sclang started ${GRAY}(PID ${sc_pid})${NC}"
    echo -e "  ${GRAY}Startup: ${SC_STARTUP}${NC}"
    echo -e "  ${GRAY}Log:     ${LOG_DIR}/sclang.log${NC}"
    echo ""
    echo -e "  ${YELLOW}Waiting for SuperCollider to boot (this takes ~10 s)...${NC}"

    local booted=false
    for ((i=0; i<30; i++)); do
        sleep 1; printf "."
        # scsynth binds port 57110 once the server is ready
        if [[ -n "$(port_pids 57110)" ]]; then
            booted=true; break
        fi
        # Also bail early if sclang died
        if ! kill -0 "$sc_pid" 2>/dev/null; then
            echo ""
            echo -e "  ${CROSS}  sclang exited early — check ${LOG_DIR}/sclang.log"
            rm -f "$tmpscript"
            return 1
        fi
    done
    echo ""

    if $booted; then
        echo -e "  ${TICK}  SuperCollider ${GREEN}UP${NC}  ${GRAY}(scsynth :57110, StageLimiter activating in ${SC_BOOT_DELAY}s...)${NC}"
    else
        echo -e "  ${WARN}  scsynth not detected on :57110 yet — may still be booting"
        echo -e "  ${GRAY}Run: tail -f ${LOG_DIR}/sclang.log${NC}"
    fi

    rm -f "$tmpscript"
}

do_stop_sc() {
    local killed=false

    # 1. Kill sclang by tracked PID
    if [[ -f "$SC_PID_FILE" ]]; then
        while read -r pid; do
            if kill "$pid" 2>/dev/null; then
                echo -e "  ${GRAY}killed sclang PID ${pid}${NC}"
                killed=true
            fi
        done < "$SC_PID_FILE"
        rm -f "$SC_PID_FILE"
    fi

    # 2. Kill any sclang still running (in case PID file was stale)
    local stale_sclang; stale_sclang=$(pgrep -u "$(id -u)" sclang 2>/dev/null || true)
    if [[ -n "$stale_sclang" ]]; then
        echo -e "  ${GRAY}killed stale sclang (PID ${stale_sclang})${NC}"
        echo "$stale_sclang" | xargs kill 2>/dev/null || true
        killed=true
    fi

    # 3. Kill scsynth directly — it survives sclang's death as an orphan
    local scsynth_pids; scsynth_pids=$(pgrep -u "$(id -u)" scsynth 2>/dev/null || true)
    if [[ -n "$scsynth_pids" ]]; then
        echo -e "  ${GRAY}killed scsynth (PID ${scsynth_pids})${NC}"
        echo "$scsynth_pids" | xargs kill 2>/dev/null || true
        killed=true
        # Give it 1s; if still alive, SIGKILL
        sleep 1
        local still; still=$(pgrep -u "$(id -u)" scsynth 2>/dev/null || true)
        if [[ -n "$still" ]]; then
            echo -e "  ${GRAY}SIGKILL scsynth (PID ${still})${NC}"
            echo "$still" | xargs kill -9 2>/dev/null || true
        fi
    fi

    if $killed; then
        echo -e "  ${TICK}  SuperCollider stopped"
    else
        echo -e "  ${GRAY}  SuperCollider was not running${NC}"
    fi
}

# ── Start WebFoxDot browser environment ───────────────────────────────────────

do_start_webfoxdot() {
    if [[ ! -d "$WEBFOXDOT_DIR" ]]; then
        echo -e "  ${CROSS}  supersonic-proto/ not found. Run: ${CYAN}./start.sh install webfoxdot${NC}"
        return 1
    fi
    kill_port 8765 "WebFoxDot"
    > "$WEBFOXDOT_PID"
    echo -e "  ${TICK}  WebFoxDot server starting..."
    "${VENV_PYTHON:-python3}" "${WEBFOXDOT_DIR}/serve.py" >> "${LOG_DIR}/webfoxdot.log" 2>&1 &
    echo $! >> "$WEBFOXDOT_PID"
    sleep 0.5
    if [[ -n "$(port_pids 8765)" ]]; then
        echo -e "  ${TICK}  WebFoxDot ${GREEN}UP${NC}  ${GRAY}port 8765${NC}"
        echo -e "  ${BOLD}WebFoxDot (local):${NC}  ${CYAN}http://localhost:8765${NC}"
        echo -e "  ${BOLD}WebFoxDot (LAN):${NC}    ${CYAN}http://${HOST_IP:-localhost}:8765${NC}"
    else
        echo -e "  ${WARN}  WebFoxDot may still be starting — check ${LOG_DIR}/webfoxdot.log"
    fi
}

do_stop_webfoxdot() {
    kill_port 8765 "WebFoxDot"
    [[ -f "$WEBFOXDOT_PID" ]] && rm -f "$WEBFOXDOT_PID"
    echo -e "  ${TICK}  WebFoxDot stopped"
}

# ── Stop all ───────────────────────────────────────────────────────────────────

do_stop() {
    echo -e "${YELLOW}Stopping all services:${NC}"
    kill_port 4444  "y-websocket"
    kill_port 1234  "webTroop server"
    kill_port 3000  "Vite"
    kill_port 1235  "grid serve"
    kill_port 8765  "WebFoxDot"
    [[ -f "$PID_FILE" ]]         && rm -f "$PID_FILE"
    [[ -f "$WEBFOXDOT_PID" ]]    && rm -f "$WEBFOXDOT_PID"
    echo -e "  ${TICK}  webTroop + WebFoxDot stopped"
    echo -e "  ${GRAY}  (SuperCollider kept running — use ./start.sh sc stop to kill it)${NC}"
}

# ── Kill everything — nuclear option ──────────────────────────────────────────

do_killall() {
    echo -e "${RED}Killing everything:${NC}"

    # sclang + scsynth by process name
    local sc_pids; sc_pids=$(pgrep -u "$(id -u)" -d ' ' sclang scsynth 2>/dev/null || true)
    if [[ -n "$sc_pids" ]]; then
        echo -e "  ${GRAY}killing sclang/scsynth (PID ${sc_pids})${NC}"
        pkill -u "$(id -u)" sclang  2>/dev/null || true
        pkill -u "$(id -u)" scsynth 2>/dev/null || true
    fi

    # All known service ports
    for port in 4444 1234 3000 1235 8765; do
        kill_port "$port"
    done

    # serve.py processes (grid + webfoxdot)
    pkill -u "$(id -u)" -f "serve\.py" 2>/dev/null || true

    # y-websocket node process
    pkill -u "$(id -u)" -f "y-websocket" 2>/dev/null || true

    # Clean PID files
    rm -f "$PID_FILE" "$WEBFOXDOT_PID" "$SC_PID_FILE"

    # Brief pause then SIGKILL anything still on those ports
    sleep 0.8
    local leftovers; leftovers=$(lsof -ti:4444,1234,3000,1235,8765,57110 2>/dev/null || true)
    if [[ -n "$leftovers" ]]; then
        echo -e "  ${GRAY}force-killing stragglers...${NC}"
        echo "$leftovers" | xargs kill -9 2>/dev/null || true
    fi
    local sc_left; sc_left=$(pgrep -u "$(id -u)" scsynth 2>/dev/null || true)
    if [[ -n "$sc_left" ]]; then
        echo -e "  ${GRAY}force-killing scsynth...${NC}"
        echo "$sc_left" | xargs kill -9 2>/dev/null || true
    fi

    sleep 0.3
    echo -e "  ${TICK}  All clear"
    show_status
}

# ── Restart helpers ────────────────────────────────────────────────────────────

do_restart_grid() {
    kill_port 1235 "grid serve"
    nohup bash -c "cd '${REPO_DIR}/grid' && '${VENV_PYTHON}' serve.py" \
        >> "${LOG_DIR}/grid-serve.log" 2>&1 &
    echo -e "  ${TICK}  grid-serve restarted ${GRAY}(PID $!)${NC}"
}

do_restart_webfoxdot() {
    do_stop_webfoxdot
    do_start_webfoxdot
}

# ── Documentation browser ─────────────────────────────────────────────────────

_doc_viewer() {
    local file="$1"
    if [[ ! -f "$file" ]]; then
        echo -e "  ${CROSS}  Doc not found: ${file}"; sleep 1; return
    fi
    if command -v glow &>/dev/null; then
        glow -p "$file"
    elif command -v bat &>/dev/null; then
        bat --language=md --paging=always "$file"
    else
        less -R "$file"
    fi
}

_doc_refresh() {
    local GEN="${REPO_DIR}/docs/generated"
    local PY="${REPO_DIR}/docs/generate.py"
    [[ ! -f "$PY" ]] && return

    # Check if any generated file is older than its primary sources
    local needs_regen=false
    local sources=(
        "${REPO_DIR}/FoxDot/FoxDot/osc/scsyndef"
        "${REPO_DIR}/FoxDot/FoxDot/lib/Crashserver/crashFX.py"
        "${REPO_DIR}/grid/cells.json"
        "${REPO_DIR}/supersonic-proto/js/synths/registry.js"
        "${REPO_DIR}/supersonic-proto/js/fx/registry.js"
    )
    for gen_file in "${GEN}"/*.md; do
        [[ -f "$gen_file" ]] || { needs_regen=true; break; }
    done
    if ! $needs_regen; then
        local gen_mtime; gen_mtime=$(stat -c %Y "${GEN}/synths.md" 2>/dev/null || echo 0)
        for src in "${sources[@]}"; do
            local src_mtime; src_mtime=$(stat -c %Y "$src" 2>/dev/null || echo 0)
            if (( src_mtime > gen_mtime )); then needs_regen=true; break; fi
        done
    fi

    if $needs_regen; then
        echo -e "  ${YELLOW}Regenerating reference docs...${NC}"
        python3 "$PY" 2>/dev/null && echo -e "  ${TICK}  Docs updated" || echo -e "  ${WARN}  Doc generation had errors"
        echo ""
    fi
}

do_doc_menu() {
    local D="${REPO_DIR}/docs"
    local G="${REPO_DIR}/docs/generated"
    local WFD="${REPO_DIR}/supersonic-proto"

    _doc_refresh

    while true; do
        echo ""
        echo -e "${BOLD}${CYAN}── Documentation ───────────────────────────────────${NC}"
        echo ""
        echo -e "  ${BOLD}How-to guides${NC}"
        echo -e "    ${BOLD}1)${NC}  Add a synth to FoxDot"
        echo -e "    ${BOLD}2)${NC}  Add an FX to FoxDot"
        echo -e "    ${BOLD}3)${NC}  Radial menu — add cells · attacks · #@ parts"
        echo -e "    ${BOLD}4)${NC}  WebSocket message types & how to add"
        echo -e "    ${BOLD}5)${NC}  WebFoxDot — overview, deploy, extend"
        echo ""
        echo -e "  ${BOLD}Generated reference${NC}  ${GRAY}(auto-updated from source)${NC}"
        echo -e "    ${BOLD}a)${NC}  FoxDot synths          ${GRAY}(214 synths + params)${NC}"
        echo -e "    ${BOLD}b)${NC}  FoxDot FX              ${GRAY}(120 effects by category)${NC}"
        echo -e "    ${BOLD}c)${NC}  Attacks                ${GRAY}(from cells.json)${NC}"
        echo -e "    ${BOLD}e)${NC}  Grid cells             ${GRAY}(all cells by column)${NC}"
        echo -e "    ${BOLD}f)${NC}  WebFoxDot synths       ${GRAY}(registry.js)${NC}"
        echo -e "    ${BOLD}g)${NC}  WebFoxDot FX           ${GRAY}(fx/registry.js)${NC}"
        echo ""
        echo -e "  ${BOLD}Other${NC}"
        echo -e "    ${BOLD}6)${NC}  Functions & patterns cheatsheet"
        echo -e "    ${BOLD}7)${NC}  Installation & setup"
        echo -e "    ${BOLD}8)${NC}  Composition engine"
        echo -e "    ${BOLD}9)${NC}  ${YELLOW}Keyboard shortcuts${NC}           ${GRAY}(all Ctrl/Alt/Shift combos)${NC}"
        echo -e "    ${BOLD}h)${NC}  Changelog                     ${GRAY}(all changes since live2026)${NC}"
        echo -e "    ${BOLD}r)${NC}  ${CYAN}Refresh all generated docs${NC}"
        echo ""
        echo -e "  ${BOLD}0)${NC}  Back"
        echo ""
        printf "  ${CYAN}Choice:${NC} "; read -r choice
        echo ""

        case "$choice" in
            1) _doc_viewer "${D}/add-synth-foxdot.md" ;;
            2) _doc_viewer "${D}/add-fx-foxdot.md" ;;
            3) _doc_viewer "${D}/radial-menu.md" ;;
            4) _doc_viewer "${D}/websocket-sends.md" ;;
            5) _doc_viewer "${WFD}/README.md" ;;
            a) _doc_viewer "${G}/synths.md" ;;
            b) _doc_viewer "${G}/fx.md" ;;
            c) _doc_viewer "${G}/attacks.md" ;;
            e) _doc_viewer "${G}/cells.md" ;;
            f) _doc_viewer "${G}/webfoxdot-synths.md" ;;
            g) _doc_viewer "${G}/webfoxdot-fx.md" ;;
            6) _doc_viewer "${D}/cheatsheet_fonctions_crash.md" ;;
            7) _doc_viewer "${D}/installation_and_setup.md" ;;
            8) _doc_viewer "${D}/composition-engine.md" ;;
            9) _doc_viewer "${D}/shortcuts.md" ;;
            h) _doc_viewer "${D}/changelog.md" ;;
            r) python3 "${REPO_DIR}/docs/generate.py" --force ;;
            0|q|"") return 0 ;;
            *) echo -e "  ${WARN}  Unknown option\n" ;;
        esac
    done
}

# ── Install ────────────────────────────────────────────────────────────────────

do_install_webfoxdot() {
    if [[ ! -f "${WEBFOXDOT_DIR}/install.sh" ]]; then
        echo -e "  ${CROSS}  ${WEBFOXDOT_DIR}/install.sh not found"
        return 1
    fi
    echo -e "  ${ARROW}  Running WebFoxDot installer...\n"
    bash "${WEBFOXDOT_DIR}/install.sh"
}

do_install_all() {
    if [[ ! -f "${REPO_DIR}/install/install.sh" ]]; then
        echo -e "  ${CROSS}  ${REPO_DIR}/install/install.sh not found"
        return 1
    fi
    echo -e "  ${ARROW}  Running full system installer...\n"
    bash "${REPO_DIR}/install/install.sh"
}

do_install_menu() {
    header "CrashFoxDot — Install"
    echo -e "  ${BOLD}1)${NC}  Full system install ${GRAY}(Python venv, npm, FoxDot, samples, SC)${NC}"
    echo -e "  ${BOLD}2)${NC}  WebFoxDot only      ${GRAY}(WASM engine, samples, synthdefs, web server)${NC}"
    echo -e "  ${BOLD}3)${NC}  Compile WebFoxDot SynthDefs only"
    echo -e "  ${BOLD}0)${NC}  Back"
    echo ""
    printf "  ${CYAN}Choice:${NC} "; read -r choice
    case "$choice" in
        1) do_install_all ;;
        2) do_install_webfoxdot ;;
        3)
            if [[ -f "${WEBFOXDOT_DIR}/scripts/build.sh" ]]; then
                echo -e "  ${ARROW}  Compiling SynthDefs..."
                bash "${WEBFOXDOT_DIR}/scripts/build.sh"
            else
                echo -e "  ${CROSS}  ${WEBFOXDOT_DIR}/scripts/build.sh not found"
            fi
            ;;
        0) return 0 ;;
        *) echo -e "  ${WARN}  Unknown option" ;;
    esac
}

# ── Interactive menu ───────────────────────────────────────────────────────────

do_menu() {
    # Detect if we're likely non-interactive (e.g. piped) and fall through to start
    if [[ ! -t 0 ]]; then
        do_start
        wait_for_ports 4444 1234 3000
        show_status
        wait
        return
    fi

    while true; do
        header "CrashFoxDot"

        # Quick status peek
        local troop_up webfox_up sc_up
        troop_up=$(port_up 3000); webfox_up=$(port_up 8765); sc_up=$(port_up 57110)
        echo -e "  webTroop: $( [[ "$troop_up"  == "yes" ]] && echo "${GREEN}UP${NC}" || echo "${RED}DOWN${NC}" )  " \
                "WebFoxDot: $( [[ "$webfox_up" == "yes" ]] && echo "${GREEN}UP${NC}" || echo "${RED}DOWN${NC}" )  " \
                "SC: $( [[ "$sc_up" == "yes" ]] && echo "${GREEN}UP${NC}" || echo "${RED}DOWN${NC}" )"
        echo ""
        echo -e "  ${BOLD}1)${NC}  Start webTroop                ${GRAY}(Vite :3000, server :1234, y-ws :4444, grid :1235)${NC}"
        echo -e "  ${BOLD}2)${NC}  Start webTroop + WebFoxDot    ${GRAY}(+ browser scsynth :8765)${NC}"
        echo -e "  ${BOLD}3)${NC}  Start WebFoxDot only          ${GRAY}(:8765)${NC}"
        echo -e "  ${BOLD}s)${NC}  Start SuperCollider headless  ${GRAY}(sclang → FoxDot.start + StageLimiter)${NC}"
        echo -e "  ${BOLD}4)${NC}  Stop all services             ${GRAY}(webTroop + WebFoxDot; SC kept running)${NC}"
        echo -e "  ${BOLD}S)${NC}  Stop SuperCollider"
        echo -e "  ${BOLD}k)${NC}  ${RED}Kill everything${NC}               ${GRAY}(sclang, scsynth, all servers — nuclear)${NC}"
        echo -e "  ${BOLD}5)${NC}  Status"
        echo -e "  ${BOLD}6)${NC}  Restart grid server"
        echo -e "  ${BOLD}7)${NC}  Restart WebFoxDot"
        echo -e "  ${BOLD}r)${NC}  Restart SuperCollider"
        echo -e "  ${BOLD}8)${NC}  Install..."
        echo -e "  ${BOLD}d)${NC}  Documentation"
        echo -e "  ${BOLD}0)${NC}  Exit"
        echo ""
        printf "  ${CYAN}Choice:${NC} "; read -r choice
        echo ""

        case "$choice" in
            1)
                do_start
                wait_for_ports 4444 1234 3000
                show_status
                echo -e "  ${GRAY}Tip: ./start.sh status | ./start.sh restart grid${NC}"
                echo -e "  Press ${BOLD}Ctrl+C${NC} to stop all services\n"
                wait
                break
                ;;
            2)
                do_start
                do_start_webfoxdot
                wait_for_ports 4444 1234 3000
                show_status
                echo -e "  Press ${BOLD}Ctrl+C${NC} to stop all services\n"
                wait
                break
                ;;
            3)
                do_start_webfoxdot
                echo ""
                echo -e "  Press ${BOLD}Ctrl+C${NC} to stop. ${GRAY}(WebFoxDot runs standalone — no webTroop needed)${NC}\n"
                trap 'do_stop_webfoxdot; exit 0' INT TERM
                wait
                break
                ;;
            s) do_start_sc ;;
            4) do_stop ;;
            S) do_stop_sc ;;
            k) do_killall ;;
            5) show_status; printf "  ${GRAY}press enter to continue${NC}"; read -r ;;
            6) do_restart_grid ;;
            7) do_restart_webfoxdot ;;
            r) do_stop_sc; sleep 0.5; do_start_sc ;;
            8) do_install_menu ;;
            d) do_doc_menu ;;
            0|q|"") exit 0 ;;
            *) echo -e "  ${WARN}  Unknown option '${choice}'\n" ;;
        esac
    done
}

# ═══════════════════════════════════════════════════════════════════════════════
#  Command dispatch
# ═══════════════════════════════════════════════════════════════════════════════

CMD="${1:-menu}"
shift || true

case "$CMD" in
    menu|"")
        do_menu
        ;;
    start)
        do_start "$@"
        wait_for_ports 4444 1234 3000
        show_status
        echo -e "  Tip: ${GRAY}./start.sh status${NC}  —  from another terminal"
        echo -e "  Tip: ${GRAY}./start.sh restart grid${NC}  —  restart grid only"
        echo -e "  Press ${BOLD}Ctrl+C${NC} to stop all services\n"
        wait
        ;;
    stop)
        do_stop
        ;;
    killall|kill)
        do_killall
        ;;
    doc|docs)
        do_doc_menu
        ;;
    status)
        show_status
        ;;
    restart)
        case "${1:-all}" in
            grid)       do_restart_grid; show_status ;;
            webfoxdot)  do_restart_webfoxdot; show_status ;;
            sc)         do_stop_sc; sleep 0.5; do_start_sc ;;
            *)
                do_stop
                sleep 0.5
                do_start
                wait_for_ports 4444 1234 3000
                show_status
                echo -e "  Press ${BOLD}Ctrl+C${NC} to stop all services\n"
                wait
                ;;
        esac
        ;;
    sc)
        case "${1:-start}" in
            start)   do_start_sc ;;
            stop)    do_stop_sc ;;
            restart) do_stop_sc; sleep 0.5; do_start_sc ;;
            *)       do_start_sc ;;
        esac
        ;;
    webfoxdot|wfd)
        case "${1:-start}" in
            start)   do_start_webfoxdot ;;
            stop)    do_stop_webfoxdot ;;
            restart) do_restart_webfoxdot ;;
            *)       do_start_webfoxdot ;;
        esac
        ;;
    install)
        case "${1:-menu}" in
            webfoxdot) do_install_webfoxdot ;;
            all)       do_install_all ;;
            *)         do_install_menu ;;
        esac
        ;;
    --no-sc)
        do_start --no-sc
        wait_for_ports 4444 1234 3000
        show_status
        echo -e "  Press ${BOLD}Ctrl+C${NC} to stop all services\n"
        wait
        ;;
    help|-h|--help)
        echo ""
        echo -e "${BOLD}CrashFoxDot — start.sh${NC}"
        echo ""
        echo -e "  ${CYAN}./start.sh${NC}                    interactive menu"
        echo -e "  ${CYAN}./start.sh start${NC} [--no-sc]    start webTroop services"
        echo -e "  ${CYAN}./start.sh stop${NC}               stop webTroop + WebFoxDot"
        echo -e "  ${CYAN}./start.sh status${NC}             service + version status"
        echo -e "  ${CYAN}./start.sh restart${NC} [svc]      restart all / grid / webfoxdot / sc"
        echo -e "  ${CYAN}./start.sh sc${NC} [start|stop|restart]"
        echo -e "                                SuperCollider headless (sclang)"
        echo -e "                                FoxDot.start → boot → StageLimiter"
        echo -e "                                ${GRAY}SC_BOOT_DELAY=5 ./start.sh sc  — custom delay${NC}"
        echo -e "  ${CYAN}./start.sh webfoxdot${NC} [start|stop|restart]"
        echo -e "                                WebFoxDot browser environment (:8765)"
        echo -e "  ${CYAN}./start.sh install${NC}            installation menu"
        echo -e "  ${CYAN}./start.sh install webfoxdot${NC}  install WebFoxDot only"
        echo -e "  ${CYAN}./start.sh install all${NC}        full system install"
        echo -e "  ${CYAN}./start.sh doc${NC}                documentation browser"
        echo ""
        ;;
    *)
        echo -e "  ${WARN}  Unknown command '${CMD}' — run ${CYAN}./start.sh help${NC}"
        exit 1
        ;;
esac
