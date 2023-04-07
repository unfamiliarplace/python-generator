import random

class JS_Random():

    def flip_coin(chance: float) -> bool:
        return (random.randint(0, 100) / 100) >= chance
    
    def choose_from(items: list) -> object:
        return random.choice(items)
    
    def number_between(lower: int, upper: int, decimal: bool=False) -> int|float:
        if decimal:
            lower *= 10
            upper *= 10

        n = random.randint(lower, upper)
        if decimal:
            n /= 10
        
        return n

if __name__ == '__main__':
    R = JS_Random
    print(R.flip_coin(0.5))
    print(R.choose_from(['a', 'b', 'c']))
    print(R.number_between(-50, 100, False))
    print(R.number_between(-50, 100, True))
