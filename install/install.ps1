# =============================================================
#  CrashServer / live2027_grid — Full Windows Installer
#  Run in PowerShell as Administrator:
#    Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
#    .\install\install.ps1 [-SkipSystem] [-SkipSamples] [-Optional] [-Yes]
# =============================================================
param(
    [switch]$SkipSystem,
    [switch]$SkipSamples,
    [switch]$Optional,
    [switch]$Yes
)

$ErrorActionPreference = "Continue"

# ── Colors ───────────────────────────────────────────────────
function Ok($msg, $key)   { Write-Host "  [OK] $msg" -ForegroundColor Green;  $script:STATUS[$key] = "ok" }
function Fail($msg, $key) { Write-Host "  [!!] $msg" -ForegroundColor Red;    $script:STATUS[$key] = "FAILED" }
function Skip($msg, $key) { Write-Host "  [->] $msg" -ForegroundColor Yellow; $script:STATUS[$key] = "skipped" }
function Info($msg)       { Write-Host "  [ ] $msg"  -ForegroundColor Cyan }
function Warn($msg)       { Write-Host "  [?] $msg"  -ForegroundColor Yellow }
function Section($msg)    { Write-Host "`n=== $msg ===" -ForegroundColor Cyan }

function Confirm-Step($msg) {
    if ($Yes) { return $true }
    $reply = Read-Host "  [?] $msg [y/N]"
    return ($reply -match '^[Yy]$')
}

$script:STATUS = @{}

$REPO_DIR    = Split-Path -Parent $PSScriptRoot
$SC_QUARKS   = "$env:APPDATA\SuperCollider\downloaded-quarks"
$SC_EXTS     = "$env:APPDATA\SuperCollider\Extensions"
$SAMPLE_PATH = "$env:USERPROFILE\UltimateSamples"

Write-Host "`nCrashServer — Full Windows Installer" -ForegroundColor White
Write-Host "  Repo:      $REPO_DIR"
Write-Host "  SC quarks: $SC_QUARKS"
Write-Host "  Samples:   $SAMPLE_PATH`n"

# =============================================================
#  1. SYSTEM PACKAGES (winget)
# =============================================================
Section "1 / 7 — System packages"

function Install-Winget($id, $name) {
    Info "Installing $name via winget..."
    $result = winget install --id $id --silent --accept-package-agreements --accept-source-agreements 2>&1
    if ($LASTEXITCODE -eq 0 -or $result -match "already installed") {
        Ok "$name installed" "pkg_$name"
    } else {
        Fail "$name install failed — install manually" "pkg_$name"
    }
}

if ($SkipSystem) {
    Skip "System packages skipped" "system_packages"
} elseif (Confirm-Step "Install system packages (SuperCollider, Python, Node, Git)?") {
    Install-Winget "PKGID.SuperCollider"   "SuperCollider"
    Install-Winget "Python.Python.3.12"    "Python 3.12"
    Install-Winget "OpenJS.NodeJS.LTS"     "Node.js LTS"
    Install-Winget "Git.Git"               "Git"
} else {
    Skip "System packages skipped" "system_packages"
}

# Refresh PATH
$env:PATH = [System.Environment]::GetEnvironmentVariable("PATH", "Machine") + ";" +
            [System.Environment]::GetEnvironmentVariable("PATH", "User")

# =============================================================
#  2. PYTHON PACKAGES
# =============================================================
Section "2 / 7 — Python packages"

$PYTHON_REQUIRED = @(
    "websockets", "python-rtmidi", "pyfiglet", "pyperclip", "LinkToPy",
    "requests", "numpy", "edn-format", "ply", "pyRFC3339", "pytz",
    "setuptools", "monotonic"
)

Info "Installing FoxDot Python package (editable)..."
$r = pip install -e "$REPO_DIR\FoxDot" --quiet 2>&1
if ($LASTEXITCODE -eq 0) { Ok "FoxDot Python package" "foxdot_python" }
else                      { Fail "FoxDot Python package failed" "foxdot_python"; Write-Host $r }

Info "Installing required Python dependencies..."
$r = pip install @PYTHON_REQUIRED --quiet 2>&1
if ($LASTEXITCODE -eq 0) { Ok "Python required packages" "python_required" }
else                      { Fail "Python required packages (partial?)" "python_required"; Write-Host $r }

if ($Optional) {
    Info "Installing optional packages (librosa, opencv)..."
    $r = pip install librosa opencv-python --quiet 2>&1
    if ($LASTEXITCODE -eq 0) { Ok "Python optional packages" "python_optional" }
    else                      { Warn "Optional packages failed — non-critical" }
} else {
    Skip "Optional packages skipped (pass -Optional to include)" "python_optional"
}

# =============================================================
#  3. NODE PACKAGES
# =============================================================
Section "3 / 7 — Node packages"

$nodeVer = (node --version 2>$null) -replace 'v(\d+).*','$1'
if ([int]$nodeVer -lt 18) {
    Warn "Node $nodeVer < 18. Install Node 20 LTS from nodejs.org"
    $script:STATUS["node_version"] = "needs upgrade"
} else {
    Ok "Node $(node --version)" "node_version"
}

Info "webTroop npm install..."
Push-Location "$REPO_DIR\webTroop"
npm install --silent
if ($LASTEXITCODE -eq 0) { Ok "webTroop npm install" "node_webroop" }
else                      { Fail "webTroop npm install failed" "node_webroop" }
Pop-Location

Info "hub npm install..."
Push-Location "$REPO_DIR\hub"
npm install --silent
if ($LASTEXITCODE -eq 0) { Ok "hub npm install" "node_hub" }
else                      { Fail "hub npm install failed" "node_hub" }
Pop-Location

# =============================================================
#  4. SUPERCOLLIDER QUARKS
# =============================================================
Section "4 / 7 — SuperCollider quarks"

New-Item -ItemType Directory -Force -Path $SC_QUARKS | Out-Null

function Install-Quark($name, $url) {
    $dest = "$SC_QUARKS\$name"
    if (Test-Path $dest) {
        Info "$name already present — pulling latest..."
        git -C $dest pull --quiet
        Ok "$name updated" "quark_$name"
    } else {
        Info "Cloning $name..."
        git clone --depth 1 --quiet $url $dest
        if ($LASTEXITCODE -eq 0) { Ok "$name installed" "quark_$name" }
        else                      { Fail "$name clone failed" "quark_$name" }
    }
}

Install-Quark "BatLib"            "https://github.com/supercollider-quarks/BatLib"
Install-Quark "Feedback"          "https://github.com/supercollider-quarks/Feedback"
Install-Quark "miSCellaneous_lib" "https://github.com/dkmayer/miSCellaneous_lib"
Install-Quark "ddwWavetableSynth" "https://github.com/jamshark70/ddwWavetableSynth"

$foxdotQuark = "$SC_QUARKS\FoxDot"
if (-not (Test-Path $foxdotQuark)) {
    Info "Cloning FoxDot SC quark..."
    git clone --depth 1 --quiet "https://github.com/Qirky/FoxDotQuark" $foxdotQuark
    if ($LASTEXITCODE -eq 0) { Ok "FoxDot SC quark cloned" "quark_FoxDot_clone" }
    else                      { Fail "FoxDot SC quark clone failed" "quark_FoxDot_clone" }
} else {
    Ok "FoxDot SC quark already present" "quark_FoxDot_clone"
}

Info "Patching FoxDot.sc..."
Copy-Item "$REPO_DIR\config\FoxDot.sc" "$foxdotQuark\FoxDot.sc" -Force
if ($LASTEXITCODE -eq 0) { Ok "FoxDot.sc patched" "foxdot_sc_patch" }
else                      { Fail "FoxDot.sc patch failed" "foxdot_sc_patch" }

# =============================================================
#  5. SUPERCOLLIDER EXTENSIONS
# =============================================================
Section "5 / 7 — SuperCollider extensions"

New-Item -ItemType Directory -Force -Path $SC_EXTS | Out-Null

# NOTE: The bundled extensions in config/SC_Extensions/ are Linux .so binaries.
# On Windows, .dll versions must be downloaded from the GitHub releases pages:
#   mi-UGens:     https://github.com/v7b1/mi-UGens/releases
#   PortedPlugins: https://github.com/madskjeldgaard/portedplugins/releases
#   Open303:      https://github.com/schollz/open303/releases

function Get-GitHubLatestAsset($repo, $pattern) {
    try {
        $rel = Invoke-RestMethod "https://api.github.com/repos/$repo/releases/latest"
        $asset = $rel.assets | Where-Object { $_.name -match $pattern } | Select-Object -First 1
        return $asset.browser_download_url
    } catch { return $null }
}

function Install-Extension($name, $repo, $pattern) {
    $dest = "$SC_EXTS\$name"
    if (Test-Path $dest) {
        Ok "$name already installed" "ext_$name"
        return
    }
    Info "Downloading $name Windows binaries..."
    $url = Get-GitHubLatestAsset $repo $pattern
    if (-not $url) {
        Warn "$name: could not find Windows release. Download manually from: https://github.com/$repo/releases"
        $script:STATUS["ext_$name"] = "manual install needed"
        return
    }
    $zip = "$env:TEMP\$name.zip"
    Invoke-WebRequest $url -OutFile $zip
    Expand-Archive $zip -DestinationPath "$SC_EXTS\" -Force
    Remove-Item $zip
    Ok "$name installed" "ext_$name"
}

Install-Extension "mi-UGens"      "v7b1/mi-UGens"              "win"
Install-Extension "PortedPlugins" "madskjeldgaard/portedplugins" "Win"
Install-Extension "Open303"       "schollz/open303"             "[Ww]in"

# =============================================================
#  6. SAMPLES
# =============================================================
Section "6 / 7 — Samples"

function Clone-SampleBank($bank) {
    $dest = "$SAMPLE_PATH\$bank"
    if (Test-Path $dest) {
        Ok "Sample bank $bank already present" "samples_$bank"
    } else {
        Info "Cloning sample bank $bank (may take a long time — several GB)..."
        git clone --depth 1 --quiet "https://github.com/CrashServer/$bank" $dest
        if ($LASTEXITCODE -eq 0) { Ok "Sample bank $bank downloaded" "samples_$bank" }
        else                      { Fail "Sample bank $bank download failed" "samples_$bank" }
    }
}

if ($SkipSamples) {
    Skip "Samples skipped" "samples_0"
    $script:STATUS["samples_1"] = "skipped"; $script:STATUS["samples_2"] = "skipped"
} elseif (Test-Path $SAMPLE_PATH) {
    Ok "Samples directory already present at $SAMPLE_PATH" "samples_0"
    $script:STATUS["samples_1"] = "ok (existing)"; $script:STATUS["samples_2"] = "ok (existing)"
} elseif (Confirm-Step "Download samples from GitHub (~8 GB total — banks 0, 1, 2)?") {
    New-Item -ItemType Directory -Force -Path $SAMPLE_PATH | Out-Null
    Clone-SampleBank "0"; Clone-SampleBank "1"; Clone-SampleBank "2"
} else {
    Skip "Samples skipped" "samples_0"
    $script:STATUS["samples_1"] = "skipped"; $script:STATUS["samples_2"] = "skipped"
}

# =============================================================
#  7. CONFIGURATION
# =============================================================
Section "7 / 7 — Configuration"

$configFile = "$REPO_DIR\webTroop\crash_config.json"

if (Test-Path $configFile) {
    Ok "crash_config.json already exists — not overwriting" "config"
    $cfg = Get-Content $configFile | ConvertFrom-Json
    Warn "Current HOST_IP: $($cfg.HOST_IP)"
} else {
    $lanIP = (Get-NetIPAddress -AddressFamily IPv4 |
              Where-Object { $_.IPAddress -notmatch '^127\.' -and $_.PrefixOrigin -ne 'WellKnown' } |
              Select-Object -First 1).IPAddress

    $config = @{
        HOST_IP         = $lanIP
        FOXDOT_PATH     = "$REPO_DIR\FoxDot" -replace '\\','/'
        sample_path     = $SAMPLE_PATH -replace '\\','/'
        FOXDOT_WS_PORT  = 20000
        freesoundApiKey = "REPLACE_WITH_YOUR_KEY"
        SC_CPU_PORT     = 2887
        showTodo        = 0
        ARDUINO         = 0
    }
    $config | ConvertTo-Json | Set-Content $configFile
    Ok "crash_config.json generated (HOST_IP=$lanIP)" "config"
}

# =============================================================
#  SUMMARY
# =============================================================
Write-Host "`n=== Installation Summary ===" -ForegroundColor Cyan

$keys = @(
    "system_packages","foxdot_python","python_required","python_optional",
    "node_version","node_webroop","node_hub",
    "quark_BatLib","quark_Feedback","quark_miSCellaneous_lib","quark_ddwWavetableSynth",
    "quark_FoxDot_clone","foxdot_sc_patch",
    "ext_mi-UGens","ext_PortedPlugins","ext_Open303",
    "samples_0","samples_1","samples_2","config"
)

$allOk = $true
foreach ($key in $keys) {
    $val = if ($script:STATUS.ContainsKey($key)) { $script:STATUS[$key] } else { "not run" }
    if ($val -eq "ok" -or $val -match "existing") {
        Write-Host "  [OK] ${key}: $val" -ForegroundColor Green
    } elseif ($val -match "skip") {
        Write-Host "  [->] ${key}: $val" -ForegroundColor Yellow
    } elseif ($val -eq "FAILED") {
        Write-Host "  [!!] ${key}: $val" -ForegroundColor Red
        $allOk = $false
    } else {
        Write-Host "  [?]  ${key}: $val" -ForegroundColor Yellow
    }
}

Write-Host ""
if ($allOk) {
    Write-Host "All done! Run: python install\verify.py" -ForegroundColor Green
} else {
    Write-Host "Completed with issues. Check FAILED items above." -ForegroundColor Yellow
}

Write-Host "`nNext steps:"
Write-Host "  1. Edit webTroop\crash_config.json — set HOST_IP, freesoundApiKey"
Write-Host "  2. Recompile SC class library in SuperCollider IDE (Language > Recompile)"
Write-Host "  3. Open config\startuplive.scd in SuperCollider IDE"
Write-Host "  4. cd webTroop && node server.js"
Write-Host "  5. cd webTroop && npm run dev"
