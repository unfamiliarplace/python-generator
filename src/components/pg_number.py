from components.pg_renderable import PG_Renderable
from js_random import JS_Random as R
from pg_expression import PG_Expression
from pg_integer import PG_Integer
from pg_float import PG_Float
from typing import Self

class PG_Number(PG_Expression):

    def __init__(self: Self, lower: int=-50, upper: int=100, decimal: bool=False) -> None:
        self.lower = lower
        self.upper = upper
        self.decimal = decimal

    def generate(self: Self) -> PG_Renderable:
        if self.decimal:            
            return PG_Integer(self.lower, self.upper)
        else:
            return PG_Float(self.lower, self.upper)

    def __str__(self: Self) -> int:
        return str(self.generate())
    