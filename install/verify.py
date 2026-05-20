#!/usr/bin/env python3
"""
CrashServer post-install verifier.
Run after install.sh / install.ps1 to confirm everything is functional.
"""
import sys, os, json, shutil, socket, subprocess, importlib.util
from pathlib import Path

REPO = Path(__file__).parent.parent
SC_QUARKS   = Path.home() / ".local/share/SuperCollider/downloaded-quarks"
SC_EXTS     = Path.home() / ".local/share/SuperCollider/Extensions"
if sys.platform == "win32":
    SC_QUARKS = Path(os.environ["APPDATA"]) / "SuperCollider/downloaded-quarks"
    SC_EXTS   = Path(os.environ["APPDATA"]) / "SuperCollider/Extensions"

# ── ANSI colors ──────────────────────────────────────────────
OK   = "\033[92m✓\033[0m"
FAIL = "\033[91m✗\033[0m"
WARN = "\033[93m⚠\033[0m"
HEAD = "\033[1m\033[96m"
NC   = "\033[0m"

results = []

def check(label, passed, detail="", warn=False):
    sym = OK if passed else (WARN if warn else FAIL)
    status = "ok" if passed else ("warn" if warn else "FAIL")
    print(f"  {sym}  {label:<45} {detail}")
    results.append((label, status))

def cmd_exists(name):
    return shutil.which(name) is not None

def pip_pkg(name):
    import importlib
    pkg = name.replace("-","_").replace("python_rtmidi","rtmidi").replace("pyRFC3339","pyrfc3339").replace("edn_format","edn_format")
    try:
        importlib.import_module(pkg)
        return True
    except ImportError:
        return False

def section(title):
    print(f"\n{HEAD}{'━'*50}\n  {title}\n{'━'*50}{NC}")

# =============================================================
section("System tools")
# =============================================================
check("sclang",    cmd_exists("sclang"),  shutil.which("sclang") or "not found")
check("scsynth",   cmd_exists("scsynth"), shutil.which("scsynth") or "not found")
check("python3",   cmd_exists("python3"), sys.version.split()[0])
check("node",      cmd_exists("node"),    subprocess.getoutput("node --version") if cmd_exists("node") else "not found")
check("npm",       cmd_exists("npm"),     subprocess.getoutput("npm --version")  if cmd_exists("npm")  else "not found")
check("git",       cmd_exists("git"),     subprocess.getoutput("git --version")[:20] if cmd_exists("git") else "not found")

# JACK / PipeWire
jack_ok = cmd_exists("jackd") or cmd_exists("pipewire")
check("JACK / PipeWire", jack_ok, "jackd or pipewire found" if jack_ok else "not found")

# =============================================================
section("Python packages")
# =============================================================
REQUIRED = [
    "websockets", "rtmidi", "pyfiglet", "pyperclip", "LinkToPy",
    "requests", "numpy", "edn_format", "ply", "pyrfc3339", "pytz",
    "setuptools", "monotonic"
]
for pkg in REQUIRED:
    ok = pip_pkg(pkg)
    check(f"pip: {pkg}", ok, "" if ok else "missing — run: pip install " + pkg.replace("_","-"))

# FoxDot itself
try:
    import FoxDot
    check("FoxDot Python package", True, FoxDot.__file__)
except ImportError:
    check("FoxDot Python package", False, "pip install -e ./FoxDot")

# Optional
for pkg in ["librosa", "cv2"]:
    ok = pip_pkg(pkg)
    check(f"pip: {pkg} (optional)", ok, "optional — pass --optional to installer", warn=not ok)

# =============================================================
section("SuperCollider quarks")
# =============================================================
QUARKS = {
    "BatLib":            "https://github.com/supercollider-quarks/BatLib",
    "Feedback":          "https://github.com/supercollider-quarks/Feedback",
    "miSCellaneous_lib": "https://github.com/dkmayer/miSCellaneous_lib",
    "ddwWavetableSynth": "https://github.com/jamshark70/ddwWavetableSynth",
    "FoxDot":            "https://github.com/Qirky/FoxDotQuark",
}
for name, url in QUARKS.items():
    path = SC_QUARKS / name
    check(f"quark: {name}", path.exists(), str(path) if path.exists() else f"missing — git clone {url}")

# FoxDot.sc patch
foxdot_sc = SC_QUARKS / "FoxDot" / "FoxDot.sc"
if foxdot_sc.exists():
    content = foxdot_sc.read_text()
    patched = "stemDiskOut" in content
    check("FoxDot.sc patched (stems)", patched,
          "patched" if patched else "unpatched — copy config/FoxDot.sc")
else:
    check("FoxDot.sc patched", False, "FoxDot quark not installed")

# =============================================================
section("SuperCollider extensions")
# =============================================================
for ext in ["mi-UGens", "PortedPlugins", "Open303"]:
    path = SC_EXTS / ext
    # also check system-wide
    sys_path = Path("/usr/share/SuperCollider/Extensions") / ext
    found = path.exists() or sys_path.exists()
    detail = str(path if path.exists() else sys_path) if found else "not found in Extensions/"
    check(f"ext: {ext}", found, detail)

# =============================================================
section("Node / webTroop")
# =============================================================
nm = REPO / "webTroop" / "node_modules"
check("webTroop node_modules", nm.exists(), str(nm) if nm.exists() else "run: cd webTroop && npm install")
nm_hub = REPO / "hub" / "node_modules"
check("hub node_modules", nm_hub.exists(), str(nm_hub) if nm_hub.exists() else "run: cd hub && npm install")

# =============================================================
section("Samples")
# =============================================================
config_file = REPO / "webTroop" / "crash_config.json"
sample_path = None
if config_file.exists():
    try:
        cfg = json.loads(config_file.read_text())
        sample_path = Path(cfg.get("sample_path", ""))
    except Exception:
        pass

if sample_path:
    for bank in ["0", "1", "2"]:
        p = sample_path / bank
        check(f"samples bank {bank}", p.exists(), str(p) if p.exists() else f"missing at {p}")
else:
    check("samples (no config)", False, "crash_config.json not found or invalid")

# =============================================================
section("Configuration")
# =============================================================
if config_file.exists():
    try:
        cfg = json.loads(config_file.read_text())
        check("crash_config.json", True, str(config_file))

        # HOST_IP vs current LAN IP
        stored_ip = cfg.get("HOST_IP", "?")
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(("8.8.8.8", 80))
            current_ip = s.getsockname()[0]
            s.close()
        except Exception:
            current_ip = "unknown"
        ip_ok = stored_ip == current_ip
        check("HOST_IP matches current LAN IP",
              ip_ok,
              f"{stored_ip} (current: {current_ip})" + ("" if ip_ok else " — update crash_config.json!"),
              warn=not ip_ok)

        foxdot_path = Path(cfg.get("FOXDOT_PATH", ""))
        check("FOXDOT_PATH exists", foxdot_path.exists(), str(foxdot_path))

        api_key = cfg.get("freesoundApiKey", "")
        key_set = bool(api_key) and api_key != "REPLACE_WITH_YOUR_KEY"
        check("freesoundApiKey set", key_set, "set" if key_set else "not configured (optional)", warn=not key_set)

    except json.JSONDecodeError as e:
        check("crash_config.json valid JSON", False, str(e))
else:
    check("crash_config.json", False, f"not found at {config_file}")

# =============================================================
# SUMMARY
# =============================================================
print(f"\n{HEAD}{'━'*50}\n  Summary\n{'━'*50}{NC}")
n_ok   = sum(1 for _, s in results if s == "ok")
n_warn = sum(1 for _, s in results if s == "warn")
n_fail = sum(1 for _, s in results if s == "FAIL")
total  = len(results)

print(f"  {OK} {n_ok}/{total} passed    {WARN} {n_warn} warnings    {FAIL} {n_fail} failures\n")

if n_fail:
    print("  Failed items:")
    for label, status in results:
        if status == "FAIL":
            print(f"    {FAIL}  {label}")
    sys.exit(1)
elif n_warn:
    print("  \033[93mAll critical checks passed. Review warnings above.\033[0m")
else:
    print("  \033[92mAll checks passed — ready to run!\033[0m")
