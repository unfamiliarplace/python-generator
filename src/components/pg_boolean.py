from js_random import JS_Random as R
from typing import Self
from components.pg_mixin_generatable import PG_Mixin_Generatable
from components.pg_mixin_renderable import PG_Mixin_Renderable

class PG_Boolean(PG_Mixin_Generatable, PG_Mixin_Renderable):

    def __init__(self: Self, chance: float=0.5) -> None:
        self.chance = chance

    def generate(self: Self) -> bool:
        return R.flip_coin(self.chance)
    
    def __str__(self: Self) -> str:
        return f'{self.generate()}'
