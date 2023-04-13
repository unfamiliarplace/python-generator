import os

for item in list(os.walk('.'))[0][2]:
    if item.endswith('flac'):
        with open(f'{item}.txt', 'w') as f:
            f.write('\n')

