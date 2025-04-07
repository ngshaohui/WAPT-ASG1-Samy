"""
build the mysite.zip file

code primarily generated with chatgpt and edited from there
"""

import zipfile
import os

# Configuration
# Replace with your actual folder names
folders_to_zip = ['mysite', 'configs']
output_zip = 'mysite.zip'
gitignore_path = '.gitignore'


def parse_gitignore(path):
    patterns = []
    if os.path.exists(path):
        with open(path) as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith('#'):
                    patterns.append(line.rstrip('/'))  # Normalize folder names
    return patterns

def match_ignore(path, patterns):
    norm_path = path.replace(os.sep, '/')
    return any(ext in norm_path for ext in patterns)

def zip_folders(folders, output_zip, ignore_patterns):
    with zipfile.ZipFile(output_zip, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for folder in folders:
            for root, dirs, files in os.walk(folder):
                rel_root = os.path.relpath(root, '.').replace(os.sep, '/')
                
                # Prune ignored directories from os.walk traversal
                dirs[:] = [d for d in dirs if not match_ignore(f"{rel_root}/{d}", ignore_patterns)]
                
                # Skip adding the ignored root itself
                if match_ignore(rel_root, ignore_patterns):
                    continue
                
                for file in files:
                    file_path = os.path.join(root, file)
                    rel_path = os.path.relpath(file_path, '.').replace(os.sep, '/')
                    if not match_ignore(rel_path, ignore_patterns):
                        zipf.write(file_path, arcname=rel_path)


def main():
    ignore_patterns = parse_gitignore(gitignore_path)
    zip_folders(folders_to_zip, output_zip, ignore_patterns)
    print(f"Created {output_zip} excluding patterns from {gitignore_path}")


if __name__ == "__main__":
    main()
