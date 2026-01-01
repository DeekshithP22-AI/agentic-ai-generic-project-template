#!/usr/bin/env python3
"""
Generate a tree diagram of the current repository structure.
"""
import os
from pathlib import Path

def should_ignore(path: Path, gitignore_patterns: list = None) -> bool:
    """Check if a path should be ignored."""
    ignore_patterns = [
        '.git', '__pycache__', '.pytest_cache', '.mypy_cache',
        'node_modules', '.venv', 'venv', 'env', '.env',
        '*.pyc', '*.pyo', '*.pyd', '.DS_Store', 'Thumbs.db',
        'dist', 'build', '*.egg-info', '.coverage', 'htmlcov',
        '.idea', '.vscode', '.cursor'
    ]
    
    path_str = str(path)
    for pattern in ignore_patterns:
        if pattern in path_str or path.name.startswith('.'):
            # Allow .env.example and similar important dotfiles
            if path.name in ['.env.example', '.gitignore', '.dockerignore']:
                continue
            if path.name.startswith('.') and path.name not in ['.env.example', '.gitignore', '.dockerignore']:
                return True
        if pattern in path_str:
            return True
    return False

def generate_tree(root_dir: Path, prefix: str = "", is_last: bool = True, max_depth: int = None, current_depth: int = 0):
    """Recursively generate tree structure."""
    if max_depth is not None and current_depth >= max_depth:
        return []
    
    items = []
    try:
        entries = sorted([e for e in root_dir.iterdir() if not should_ignore(e)])
        # Separate directories and files
        dirs = [e for e in entries if e.is_dir()]
        files = [e for e in entries if e.is_file()]
        all_entries = dirs + files
    except PermissionError:
        return []
    
    for i, entry in enumerate(all_entries):
        is_last_item = (i == len(all_entries) - 1)
        connector = "+-- " if is_last_item else "+-- "
        items.append(f"{prefix}{connector}{entry.name}")
        
        if entry.is_dir():
            extension = "    " if is_last_item else "|   "
            items.extend(generate_tree(
                entry,
                prefix + extension,
                is_last_item,
                max_depth,
                current_depth + 1
            ))
    
    return items

def main():
    """Main function to generate and print tree."""
    import argparse
    
    parser = argparse.ArgumentParser(description='Generate a tree diagram of the repository')
    parser.add_argument('-d', '--depth', type=int, default=None, help='Maximum depth to traverse')
    parser.add_argument('-o', '--output', type=str, help='Output file path (optional)')
    parser.add_argument('--root', type=str, default='.', help='Root directory to start from')
    
    args = parser.parse_args()
    
    root_path = Path(args.root).resolve()
    if not root_path.exists():
        print(f"Error: Path {root_path} does not exist")
        return
    
    print(f"{root_path.name}/")
    tree_lines = generate_tree(root_path, "", True, args.depth, 0)
    
    output = "\n".join(tree_lines)
    print(output)
    
    if args.output:
        with open(args.output, 'w', encoding='utf-8') as f:
            f.write(f"{root_path.name}/\n")
            f.write(output)
        print(f"\nTree diagram saved to {args.output}")

if __name__ == "__main__":
    main()

