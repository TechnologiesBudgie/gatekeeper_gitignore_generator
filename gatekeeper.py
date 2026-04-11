import os
import requests
import argparse
from pathlib import Path

# Mapping common extensions to GitHub's .gitignore template names
# You can expand this dictionary as needed.
EXTENSION_MAP = {
    '.py': 'Python',
    '.js': 'Node',
    '.jsx': 'Node',
    '.ts': 'Node',
    '.tsx': 'Node',
    '.c': 'C',
    '.cpp': 'C++',
    '.java': 'Java',
    '.rs': 'Rust',
    '.go': 'Go',
    '.rb': 'Ruby',
    '.php': 'PHP',
    '.swift': 'Swift',
    '.kt': 'Kotlin',
    '.dart': 'Dart',
}

GITHUB_RAW_URL = "https://raw.githubusercontent.com/github/gitignore/main/{}.gitignore"

def detect_languages(directory, recurse=False):
    detected_langs = set()
    path_root = Path(directory)
    
    # Define search pattern
    pattern = "**/*" if recurse else "*"
    
    print(f"--- Scanning {path_root.absolute()} ---")
    
    for file_path in path_root.glob(pattern):
        if file_path.is_file():
            ext = file_path.suffix.lower()
            if ext in EXTENSION_MAP:
                detected_langs.add(EXTENSION_MAP[ext])
    
    return detected_langs

def generate_gitignore(languages, output_path):
    with open(output_path, "w") as f:
        f.write(f"# Generated .gitignore for: {', '.join(languages)}\n\n")
        
        for lang in languages:
            print(f"Fetching template for: {lang}...")
            response = requests.get(GITHUB_RAW_URL.format(lang))
            
            if response.status_code == 200:
                f.write(f"\n# --- {lang} Templates ---\n")
                f.write(response.text)
                f.write("\n")
            else:
                print(f"Warning: Could not find template for {lang}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Auto-generate .gitignore based on project files.")
    parser.add_argument("dir", nargs="?", default=".", help="Directory to scan (default: current)")
    parser.add_argument("-r", "--recursive", action="store_true", help="Recurse into subdirectories")
    args = parser.parse_args()

    langs = detect_languages(args.dir, args.recursive)
    
    if not langs:
        print("No supported languages detected based on file extensions.")
    else:
        print(f"Detected: {', '.join(langs)}")
        generate_gitignore(langs, os.path.join(args.dir, ".gitignore"))
        print(f"\nDone! .gitignore created at {os.path.abspath(args.dir)}")
