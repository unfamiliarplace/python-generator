import random

R = 'ROCK'
P = 'PAPER'
S = 'SCISSORS'

class Player:
    def __init__(self, name: str):
        self.name = name
        self.roll = None

    def fight(self, other):
        if self.roll == other.roll:
            return None

        if self.roll == R:
            return self if other.roll == S else other
        elif self.roll == P:
            return self if other.roll == R else other
        elif self.roll == S:
            return self if other.roll == P else other

def run():
    name = input('Your name: ').strip()
    user = Player(name)
    comp = Player('ATM')

    wins = 0
    go = ''

    while go != 'Q':
        roll = input('R/P/S: ').strip().upper()
        user.roll = eval(roll)
        comp.roll = random.choice((R, P, S))
        print('{} rolled {}'.format(comp.name, comp.roll))

        winner = user.fight(comp)
        wins += winner == user
        winner = 'Tie!' if not winner else winner.name
        print('Winner: {}'.format(winner))
        print('Your wins: {}'.format(wins))

        go = input('\nEnter to play again, Q to quit: ').strip().upper()

if __name__ == '__main__':
    run()
    
