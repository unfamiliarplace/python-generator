from components.pg_expression import PG_Expression
from typing import Self
from components.pg_mixin_generatable import PG_Mixin_Generatable
from components.pg_mixin_renderable import PG_Mixin_Renderable

class PG_Return(PG_Mixin_Generatable, PG_Mixin_Renderable):

    def generate(self: Self) -> PG_Expression:
        return PG_Expression()
    
    def __str__(self: Self) -> str:
        return f'return {self.generate()}'
