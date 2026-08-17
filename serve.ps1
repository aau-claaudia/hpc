param(
    [string[]]$ArgsToPass,
    [switch]$SkipDeps,
    [switch]$ReinstallDeps
)

$ErrorActionPreference = "Stop"

$repoRoot = $PSScriptRoot
$venvPath = Join-Path $repoRoot ".venv"
$venvPython = Join-Path $venvPath "Scripts\python.exe"
$requirementsFile = Join-Path $repoRoot "requirements.txt"
$depsStamp = Join-Path $venvPath ".requirements-installed"
$localConfig = Join-Path $repoRoot ".zensical-serve.toml"

if (-not (Test-Path $venvPython)) {
    Write-Host "Creating virtual environment (.venv)..."
    python -m venv "$venvPath"
}

function Install-Dependencies {
    Write-Host "Installing Python dependencies (first run may take a minute)..."
    & "$venvPython" -m pip install `
        --disable-pip-version-check `
        --no-input `
        -r "$requirementsFile"
    if ($LASTEXITCODE -ne 0) {
        Write-Host ""
        Write-Host "Dependency install failed. If ./serve.ps1 is already running, stop it with Ctrl+C and try again."
        exit $LASTEXITCODE
    }
    (Get-FileHash $requirementsFile -Algorithm SHA256).Hash | Set-Content -NoNewline $depsStamp
}

if ($ReinstallDeps) {
    Install-Dependencies
}
elseif (-not $SkipDeps) {
    $requirementsHash = (Get-FileHash $requirementsFile -Algorithm SHA256).Hash
    $installedHash = if (Test-Path $depsStamp) { Get-Content $depsStamp -Raw } else { "" }

    if ($installedHash -ne $requirementsHash) {
        Install-Dependencies
    }
}

# Fail fast with a clear message if a previous upgrade left Zensical in a broken state.
& "$venvPython" -m zensical --version *> $null
if ($LASTEXITCODE -ne 0) {
    Write-Host ""
    Write-Host "Zensical is not usable in the current virtual environment."
    Write-Host "Stop any running ./serve.ps1 window (Ctrl+C), then run:"
    Write-Host "  ./serve.ps1 -ReinstallDeps"
    exit 1
}

# Use a dedicated build folder inside the repo (not the synced `site/` tree).
$zensicalConfig = Get-Content (Join-Path $repoRoot "zensical.toml") -Raw -Encoding UTF8
if ($zensicalConfig -match '(?m)^site_dir\s*=') {
    $zensicalConfig = $zensicalConfig -replace '(?m)^site_dir\s*=.*$', 'site_dir = ".site"'
}
else {
    $zensicalConfig = $zensicalConfig -replace '(?m)^\[project\]', "[project]`nsite_dir = `".site`""
}

$utf8NoBom = New-Object System.Text.UTF8Encoding $false
[System.IO.File]::WriteAllText($localConfig, $zensicalConfig, $utf8NoBom)

if ($repoRoot -match 'OneDrive') {
    Write-Host "Note: repo is on OneDrive. Build output goes to .site/ (ignored by git)."
    Write-Host "If the server keeps reloading, pause OneDrive sync for this folder or move the repo off OneDrive."
}

Write-Host "Starting Zensical server..."
if ($ArgsToPass -and $ArgsToPass.Count -gt 0) {
    & "$venvPython" -m zensical serve -f "$localConfig" @ArgsToPass
}
else {
    & "$venvPython" -m zensical serve -f "$localConfig"
}
