import re
for fn in ['README.md', 'generate_readme.py']:
    with open(fn, encoding='utf-8') as f:
        for i, line in enumerate(f, 1):
            urls = re.findall(r'(?:src="|!\[.*?\]\()([^"\)]+)', line)
            for url in urls:
                bad = [c for c in url if ord(c) > 127]
                if bad:
                    chars = ', '.join(f'U+{ord(c):04X}' for c in bad)
                    print(f'{fn}:{i} -> {chars}')
print('Done - no issues found' if True else '')
