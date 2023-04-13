# Imports
import random

# Constants
HEALTHY = ':)'
SICK = ':('

SPREAD = 1
RESISTANCE = .99
DISTANCE = 50
DAYS = 10
SEED = 1000
POP = 1000000

# Initial report
print(f'{POP} people; {SEED} start sick ({SEED / POP * 100:.2f}%)')
print(f'R={SPREAD}; distance={DISTANCE}. Running for {DAYS} days')
print()

# Set up people
people = [HEALTHY] * POP
sick = set()

# Initialize seed
for i in range(SEED):
    victim = random.randint(0, POP - 1)
    people[victim] = SICK
    sick.add(victim)

# Run simulation
for i in range(DAYS):
    n = len(sick)
    for spreader in sick.copy():
        for r in range(SPREAD):
            lower = max(0, spreader - DISTANCE // 2)
            upper = min(len(people) - 1, spreader + DISTANCE // 2)
            target = random.randint(lower, upper)

            if (random.randint(0, 100) / 100) > RESISTANCE:
                people[target] = SICK
                sick.add(target)
                
    print(f'Day {i+1}: {len(sick) - n} people newly sick (total {len(sick)})')
                
# Print report
n = len(sick)
print()
print(f'Ran for {DAYS} days. Total sick: {n} ({n / POP * 100:.1f}%)')
print(f'Average new cases per day: {(n - SEED) / DAYS:.1f}')
print()
input('Enter to quit')
