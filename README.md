Makes a .gitignore from the files in a directory.  
To run:  
`python3 -m venv .venv && source .venv/bin/activate && pip install requests && python gatekeeper.py . -r`
To build:  
`python3 -m venv .venv && source .venv/bin/activate && pip install nuitka zstandard && python -m nuitka \
    --standalone \
    --onefile \
    --lto=yes \
    --strip \
    --python-flag=-OO \
    --include-package=certifi \
    --remove-output \
    gatekeeper.py`
