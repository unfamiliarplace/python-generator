from js_random import JS_Random as R
from typing import Self
from components.pg_mixin_generatable import PG_Mixin_Generatable
from components.pg_mixin_renderable import PG_Mixin_Renderable

class PG_Real_World(PG_Mixin_Generatable, PG_Mixin_Renderable):

    # TODO
    real_world_lines = [
        'real_world_code()'
    ]

    def generate(self: Self) -> str:
        return R.choose_from(self.real_world_lines)
    
    def __str__(self: Self) -> str:
        return self.generate()
