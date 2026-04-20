# Gatekeeper
Makes a `.gitignore` from the files in a directory by fetching official GitHub templates, resolving symlinks, and deduplicating rules.

### To Run (Development)
```bash
python3 -m venv .venv && source .venv/bin/activate
pip install requests certifi
python gatekeeper.py . -r
```

### To Build (Standalone Binary)
Building requires a C compiler (`gcc` or `clang`). On Arch/Pop!_OS, ensure `patchelf` is installed for standalone linking.
```bash
python3 -m venv .venv && source .venv/bin/activate
pip install requests certifi nuitka zstandard ordered-set
python -m nuitka \
    --standalone \
    --onefile \
    --lto=yes \
    --python-flag=-OO \
    --include-package=certifi \
    --output-filename=gatekeeper \
    --remove-output \
    gatekeeper.py
```
*This software comes with ABSOLUTELY NO WARRANTY, to the extent permitted by applicable law.*
