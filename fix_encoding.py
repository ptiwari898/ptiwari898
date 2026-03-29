"""Fix double-encoded UTF-8 in README.md caused by PowerShell 5.1."""
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# .NET's CP1252 decoder maps certain bytes (0x80-0x9F) to specific Unicode chars.
# For undefined positions (0x81, 0x8D, 0x8F, 0x90), .NET passes them through as-is.
# We need a reverse map: Unicode char -> original byte value
cp1252_special = {
    '\u20ac': 0x80, '\u201a': 0x82, '\u0192': 0x83, '\u201e': 0x84,
    '\u2026': 0x85, '\u2020': 0x86, '\u2021': 0x87, '\u02c6': 0x88,
    '\u2030': 0x89, '\u0160': 0x8a, '\u2039': 0x8b, '\u0152': 0x8c,
    '\u017d': 0x8e, '\u2018': 0x91, '\u2019': 0x92, '\u201c': 0x93,
    '\u201d': 0x94, '\u2022': 0x95, '\u2013': 0x96, '\u2014': 0x97,
    '\u02dc': 0x98, '\u2122': 0x99, '\u0161': 0x9a, '\u203a': 0x9b,
    '\u0153': 0x9c, '\u017e': 0x9e, '\u0178': 0x9f,
}

def reverse_net_cp1252(text):
    """Reverse .NET's CP1252 double-encoding."""
    result = bytearray()
    for c in text:
        cp = ord(c)
        if cp < 256:
            result.append(cp)
        elif c in cp1252_special:
            result.append(cp1252_special[c])
        else:
            raise ValueError(f"Can't reverse-map U+{cp:04X} ({c!r})")
    return bytes(result)

with open('README.md', 'rb') as f:
    raw = f.read()

# Strip UTF-8 BOM if present (PS 5.1 adds BOM with -Encoding UTF8)
if raw.startswith(b'\xef\xbb\xbf'):
    raw = raw[3:]

# Decode as UTF-8 (current double-encoded state)
text = raw.decode('utf-8')

# Reverse: each char -> original byte via .NET CP1252 reverse map -> UTF-8 decode
original_bytes = reverse_net_cp1252(text)
fixed_text = original_bytes.decode('utf-8')
fixed_text = original_bytes.decode('utf-8')

with open('README.md', 'w', encoding='utf-8', newline='') as f:
    f.write(fixed_text)

print("Fixed! Verifying...")

# Verify
with open('README.md', encoding='utf-8') as f:
    content = f.read()

import re
for i, line in enumerate(content.splitlines(), 1):
    urls = re.findall(r'(?:src="|!\[.*?\]\()([^"\)]+)', line)
    for url in urls:
        bad = [c for c in url if ord(c) > 127]
        if bad:
            print(f"  STILL BAD line {i}: {', '.join(f'U+{ord(c):04X}' for c in bad)}")

# Also check some known content
if '🤖' in content:
    print("  OK: robot emoji renders correctly")
if '⭐' in content and 'img.shields.io/badge/⭐' not in content:
    print("  OK: star emoji in text OK, not in badge URLs")
elif '⭐' not in content and '%E2%AD%90' in content:
    print("  OK: star emoji fully encoded in badge URLs (may be missing from text)")

print("Done.")
