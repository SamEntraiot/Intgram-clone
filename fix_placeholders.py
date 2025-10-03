#!/usr/bin/env python3
"""
Fix all via.placeholder.com references in templates
Replace with inline SVG data URIs to prevent ERR_NAME_NOT_RESOLVED errors
"""

import os
import re

# Template directory
TEMPLATES_DIR = r'c:\Users\Nisha\Desktop\instgram clone\templates'

# Replacement patterns
REPLACEMENTS = [
    # Pattern 1: Direct image src
    (
        r"'https://via\.placeholder\.com/(\d+)'",
        r"getDefaultAvatar(\1)"
    ),
    # Pattern 2: In template strings
    (
        r'"https://via\.placeholder\.com/(\d+)"',
        r"${safeImageSrc(null, \1)}"
    ),
    # Pattern 3: Fallback in onerror
    (
        r"onerror=\"this\.src='https://via\.placeholder\.com/(\d+)'\"",
        r'onerror="this.src=getDefaultAvatar(\1)"'
    ),
    # Pattern 4: In string concatenation
    (
        r"\|\| 'https://via\.placeholder\.com/(\d+)'",
        r"|| getDefaultAvatar(\1)"
    ),
    # Pattern 5: Comparison
    (
        r"!== 'https://via\.placeholder\.com/(\d+)'",
        r"&& profile.avatar"  # Just check if avatar exists
    ),
]

def fix_file(filepath):
    """Fix placeholder references in a single file"""
    print(f"Processing: {filepath}")
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    changes = 0
    
    for pattern, replacement in REPLACEMENTS:
        new_content = re.sub(pattern, replacement, content)
        if new_content != content:
            changes += content.count(re.search(pattern, content).group(0) if re.search(pattern, content) else '')
            content = new_content
    
    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"  ✅ Fixed {changes} occurrences")
        return True
    else:
        print(f"  ℹ️ No changes needed")
        return False

def main():
    """Process all HTML files in templates directory"""
    print("=" * 60)
    print("FIXING via.placeholder.com REFERENCES")
    print("=" * 60)
    
    fixed_count = 0
    
    for filename in os.listdir(TEMPLATES_DIR):
        if filename.endswith('.html'):
            filepath = os.path.join(TEMPLATES_DIR, filename)
            if fix_file(filepath):
                fixed_count += 1
    
    print("=" * 60)
    print(f"✅ Fixed {fixed_count} files")
    print("=" * 60)
    print("\n🔄 Please refresh your browser (Ctrl+F5) to see changes")

if __name__ == '__main__':
    main()
