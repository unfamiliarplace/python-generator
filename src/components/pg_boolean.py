from js_random import JS_Random as R
from typing import Self

class PG_Boolean():

    def __init__(self: Self, chance: float=0.5) -> None:
        self.chance = chance

    def generate(self: Self) -> bool:
        return R.flip_coin(self.chance)
    
    def __str__(self: Self) -> str:
        return f'{self.generate()}'
