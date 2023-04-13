from js_random import JS_Random as R
from typing import Self
from components.pg_mixin_generatable import PG_Mixin_Generatable
from components.pg_mixin_renderable import PG_Mixin_Renderable

class PG_Float(PG_Mixin_Generatable, PG_Mixin_Renderable):

    def __init__(self: Self, lower: int=-50, upper: int=100) -> None:
        self.lower = lower
        self.upper = upper

    def generate(self: Self) -> float:
        return R.number_between(self.lower, self.upper, True)
    
    def __str__(self: Self) -> str:
        return f'{self.generate()}'
