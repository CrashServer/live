#!/bin/bash
cd "$(dirname "$0")"

# ============================================================================
# Color & Style Definitions
# ============================================================================
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
MAGENTA='\033[0;35m'
CYAN='\033[0;36m'
WHITE='\033[1;37m'
GRAY='\033[0;90m'
NC='\033[0m'
BOLD='\033[1m'

# Box drawing characters
BOX_H='─'

# ============================================================================
# Helper Functions
# ============================================================================

print_line() {
    local length=${1:-80}
    printf "${GRAY}"
    for i in $(seq 1 $length); do printf "${BOX_H}"; done
    printf "${NC}\n"
}

print_header() {
    local text="$1"
    echo -e "\n${RED}┌──────────────────────────────────────────────────────────────────────────────┐${NC}"
    printf "${RED}│${NC}%30s${BOLD}${WHITE}%s${NC}%30s${RED}│${NC}\n" "" "$text" ""
    echo -e "${RED}└──────────────────────────────────────────────────────────────────────────────┘${NC}\n"
}

get_local_ip() {
    # Simple fallback approach
    hostname -I 2>/dev/null | awk '{print $1}' || echo "127.0.0.1"
}

print_config() {
    local config_file="$1"

    if [[ ! -f "$config_file" ]]; then
        echo -e "${RED}Configuration file not found: $config_file${NC}"
        return
    fi

    echo -e "${MAGENTA}${BOLD}Configuration (crash_config.json):${NC}"
    print_line 80

    # Parse and display JSON (pure bash, no jq needed)
    while IFS= read -r line; do
        # Skip empty lines and braces
        [[ "$line" =~ ^[[:space:]]*[\{\}]?[[:space:]]*$ ]] && continue

        # Extract key-value pairs
        if [[ "$line" =~ \"([^\"]+)\":[[:space:]]*\"?([^,\"]+)\"? ]]; then
            key="${BASH_REMATCH[1]}"
            value="${BASH_REMATCH[2]}"

            printf "${CYAN}  %-20s${NC} ${YELLOW}→${NC} ${WHITE}%s${NC}\n" "$key" "$value"
        fi
    done < "$config_file"

    print_line 80
}

print_network_info() {
    local ip=$(get_local_ip)
    local port="3000"

    echo -e "${GREEN}${BOLD}Network Information:${NC}"
    print_line 80
    printf "${CYAN}  %-20s${NC} ${YELLOW}→${NC} ${WHITE}%s${NC}\n" "Local IP" "$ip"
    printf "${CYAN}  %-20s${NC} ${YELLOW}→${NC} ${WHITE}%s${NC}\n" "Local URL" "http://localhost:$port"
    printf "${CYAN}  %-20s${NC} ${YELLOW}→${NC} ${WHITE}%s${NC}\n" "Network URL" "http://$ip:$port"
    printf "${CYAN}  %-20s${NC} ${YELLOW}→${NC} ${WHITE}%s${NC}\n" "Sync Server" "ws://$ip:4444"
    print_line 80
}

print_process_status() {
    local name="$1"
    local pid="$2"

    if kill -0 "$pid" 2>/dev/null; then
        printf "${GREEN}  [OK]${NC} ${BOLD}%-30s${NC} ${GRAY}PID: ${WHITE}%-8s${NC} ${GREEN}RUNNING${NC}\n" "$name" "$pid"
    else
        printf "${RED}  [FAIL]${NC} ${BOLD}%-30s${NC} ${GRAY}PID: ${WHITE}%-8s${NC} ${RED}STOPPED${NC}\n" "$name" "$pid"
    fi
}

show_process_monitor() {
    echo -e "\n${YELLOW}${BOLD}Process Monitor:${NC}"
    print_line 80
    print_process_status "Main Server" "$SERVER_PID"
    print_process_status "Y-WebSocket Sync" "$YSOCKET_PID"
    print_process_status "Dev Client" "$DEV_PID"
    print_line 80
}

# ============================================================================
# Cleanup Handler
# ============================================================================
cleanup() {
    echo -e "\n\n${YELLOW}${BOLD}>> INITIATING SHUTDOWN <<${NC}"
    print_line 80

    if [[ -n "$SERVER_PID" ]] && kill -0 "$SERVER_PID" 2>/dev/null; then
        echo -e "${GRAY}  [STOP] Main server (PID: $SERVER_PID)${NC}"
        kill $SERVER_PID 2>/dev/null
    fi

    if [[ -n "$YSOCKET_PID" ]] && kill -0 "$YSOCKET_PID" 2>/dev/null; then
        echo -e "${GRAY}  [STOP] Y-websocket (PID: $YSOCKET_PID)${NC}"
        kill $YSOCKET_PID 2>/dev/null
    fi

    if [[ -n "$DEV_PID" ]] && kill -0 "$DEV_PID" 2>/dev/null; then
        echo -e "${GRAY}  [STOP] Dev client (PID: $DEV_PID)${NC}"
        kill $DEV_PID 2>/dev/null
    fi

    # Kill any remaining child processes
    pkill -P $$ 2>/dev/null

    echo -e "${RED}>> CRASH SERVER TERMINATED <<${NC}\n"
    exit 0
}

trap cleanup SIGINT SIGTERM EXIT

# ============================================================================
# Main Execution
# ============================================================================

clear
print_header "CRASH SERVER"

# Display configuration
print_config "crash_config.json"
echo ""

# Display network info
print_network_info
echo ""

# Start processes
echo -e "${CYAN}${BOLD}Starting Services:${NC}"
print_line 80

# Phase 1: Main server
echo -e "${YELLOW}${BOLD}[1/3]${NC} Starting ${WHITE}Main Server${NC} ${GRAY}(node server.js)${NC}"
node server.js &
SERVER_PID=$!
sleep 2

# Phase 2: Y-websocket sync server
echo -e "${YELLOW}${BOLD}[2/3]${NC} Starting ${WHITE}Y-WebSocket Sync${NC} ${GRAY}(port 4444)${NC}"
HOST=0.0.0.0 PORT=4444 YPERSISTENCE=./dbDir node ./node_modules/y-websocket/bin/server.cjs &
YSOCKET_PID=$!
sleep 2

# Phase 3: Dev client
echo -e "${YELLOW}${BOLD}[3/3]${NC} Starting ${WHITE}Dev Client${NC} ${GRAY}(npm run dev)${NC}"
print_line 80
echo ""

npm run dev &
DEV_PID=$!

sleep 2

# Show process status
show_process_monitor

# Success message
echo -e "\n${GREEN}${BOLD}>> ALL SYSTEMS OPERATIONAL <<${NC}"
echo -e "${WHITE}Press ${RED}Ctrl+C${WHITE} to stop all servers${NC}\n"
print_line 80
echo ""

# Keep script running and allow npm run dev to show output
wait $DEV_PID
