# Gatekeeper
Makes a `.gitignore` from the files in a directory by fetching official GitHub templates.

### To Run (Development)
```bash
python3 -m venv .venv && source .venv/bin/activate
pip install requests certifi
python gatekeeper.py . -r
```

### To Build (Standalone Binary)
Building requires a C compiler (`gcc` or `clang`). On Linux, ensure `patchelf` is installed.
```bash
python3 -m venv .venv && source .venv/bin/activate
pip install requests certifi nuitka zstandard ordered-set
python -m nuitka \
    --standalone \
    --onefile \
    --lto=yes \
    --strip \
    --python-flag=-OO \
    --include-package=certifi \
    --output-filename=gatekeeper \
    --remove-output \
    gatekeeper.py
```
