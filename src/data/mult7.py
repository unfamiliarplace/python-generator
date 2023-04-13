import os, time
os.chdir('C:\')

ROWS = 15000
VARS = 34
MULT = 7

T_1 = time.time()
print(f'Started at {T_1}')

f = open('test.csv', 'w')

for i in range(ROWS):
    row = ''
    for v in range(VARS):
        row += f'{v};'
    f.write(row + '\n')

f.close()

T_2 = time.time()
print(f'Time to finish original seed: {T_2 - T_1}')

f = open('test.csv', 'r')
f2 = open('testx7.csv', 'w')

for line in f.readlines():
    rows = [''] * MULT
    
    for item in line.split(';'):
        if item != '\n':
            div = int(item) / MULT
            for i in range(MULT):
                rows[i] += f'{div};'

    for row in rows:
        f2.write(row + '\n')

f.close()
f2.close()

T_3 = time.time()
print(f'Time to finish multiplication: {T_3 - T_2}')

print('Finished at {T_3}')

