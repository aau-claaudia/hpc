# AAU HPC Documentation (`hpc.aau.dk`)

Documentation for AAU HPC, built with **Zensical**.

The project contains:
- content pages in `docs/`
- theme overrides in `overrides/`
- configuration in `zensical.toml`

## Requirements

- Python 3.10+ (recommended)
- `pip`

## Install

### Windows (PowerShell)

```powershell
python -m venv .venv
.\.venv\Scripts\python -m pip install -r requirements.txt
```

### macOS/Linux (bash/zsh)

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

## Serve locally

### Recommended (Windows)

Use the project helper script:

```powershell
.\serve.ps1
```

`serve.ps1` will:
- create `.venv` if missing
- install/update dependencies from `requirements.txt`
- start `zensical serve`

### Manual (all platforms)

Windows:

```powershell
.\.venv\Scripts\python -m zensical serve
```

macOS/Linux:

```bash
source .venv/bin/activate
python -m zensical serve
```

## Build static site

```bash
python -m zensical build
```

This generates the static output in `site/`.

## Notes

- Main navigation is defined in `zensical.toml` under `nav`.
- Custom styles and scripts are in:
  - `docs/stylesheets/extra.css`
  - `docs/javascripts/extra.js`
