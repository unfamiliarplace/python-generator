import os

comments = set()

msg = \
"""Comments from NLTK (https://github.com/nltk/nltk).

Bird, Steven, Edward Loper and Ewan Klein (2009).
Natural Language Processing with Python.  O'Reilly Media Inc.

See NLTK_LICENSE.txt.

"""

def remove(s: str, sub: str) -> str:
    return s.replace(sub, '')

def deduplicate(s: str, sub: str) -> str:
    dupe = sub + sub
    while dupe in s:
        s = s.replace(dupe, sub)
    return s

for dir_ in list(os.walk('nltk'))[0][1]:
    for fname in list(os.walk(f'nltk/{dir_}'))[0][2]:
        if (not fname.endswith('.py')) or (fname == '__init__.py'):
            continue
        
        with open(f'nltk/{dir_}/{fname}', 'r', encoding='utf-8') as f:
            for line in f.readlines():
                line = line.strip()
                if line.startswith('#'):
                    if line.strip('#').strip():
                        if ('@' not in line): # no emails
                            line = deduplicate(line, '#')
                            line = deduplicate(line, '=')
                            line = deduplicate(line, '_')
                            line = deduplicate(line, ' ')
                            line = remove(line, '`')

                            comments.add(line)

with open('nltk/_comments/comments.txt', 'w', encoding='utf-8') as f:
    f.write(comments[0])
    for c in comments[1:]:
        f.write(f'\n{c}')
