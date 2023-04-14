import os
import sys

THIS = 'listify.py'
SAFE = '_original'

cwd = os.getcwd()
yn = input(f'About to listify {cwd}. Enter "Y" to proceed: ')
if yn.strip().upper().startswith('Y'):
    print('OK, going')
else:
    input('Did not listify. Hit Enter to quit')
    sys.exit()

if not os.path.exists(SAFE):
    os.mkdir(SAFE)

for _, _, files in os.walk('.'):
    for fname in files:
        if fname == THIS:
            continue
        
        os.rename(fname, f'{SAFE}/{fname}')
        with open(f'{fname}.txt', 'w') as f:
            f.write(fname)

    # Just top level ...
    break

print(f'Listified {cwd}')
input('Hit Enter to quit')
