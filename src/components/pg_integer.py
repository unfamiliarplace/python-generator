from js_random import JS_Random as R
from components.pg_literal import PG_Literal
from typing import Self

class PG_Integer(PG_Literal):

    def __init__(self: Self, lower: int=-50, upper: int=100) -> None:
        self.lower = lower
        self.upper = upper

    def generate(self: Self) -> int:
        return R.number_between(self.lower, self.upper, False)
    
    def __str__(self: Self) -> str:
        return f'{self.generate()}'
    