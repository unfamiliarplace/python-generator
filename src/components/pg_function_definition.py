from typing import Self
from components.pg_mixin_generatable import PG_Mixin_Generatable
from components.pg_mixin_renderable import PG_Mixin_Renderable

class PG_Function_Definition(PG_Mixin_Generatable, PG_Mixin_Renderable):
    # TODO

    def generate(self: Self) -> PG_Mixin_Renderable:
        return None
    
    def __str__(self: Self) -> str:
        return str(self.generate())
