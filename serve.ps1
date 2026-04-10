param(
    [string[]]$ArgsToPass
)

$ErrorActionPreference = "Stop"

$repoRoot = $PSScriptRoot
$venvPath = Join-Path $repoRoot ".venv"
$venvPython = Join-Path $venvPath "Scripts\python.exe"
$requirementsFile = Join-Path $repoRoot "requirements.txt"

if (-not (Test-Path $venvPython)) {
    Write-Host "Creating virtual environment (.venv)..."
    python -m venv "$venvPath"
}

# Ensure dependencies are available. This is safe to run repeatedly.
Write-Host "Ensuring Python dependencies are installed..."
& "$venvPython" -m pip install -r "$requirementsFile"

Write-Host "Starting Zensical server..."
if ($ArgsToPass -and $ArgsToPass.Count -gt 0) {
    & "$venvPython" -m zensical serve @ArgsToPass
} else {
    & "$venvPython" -m zensical serve
}
