from components.pg_expression import PG_Expression
from components.pg_mixin_featurized import PG_Mixin_Featurized
from typing import Self
from components.pg_mixin_generatable import PG_Mixin_Generatable
from components.pg_mixin_renderable import PG_Mixin_Renderable

class PG_Return(PG_Mixin_Generatable, PG_Mixin_Renderable, PG_Mixin_Featurized):

    def generate(self: Self) -> PG_Expression:
        return PG_Expression().featurize(self.pg)
    
    def __str__(self: Self) -> str:
        return f'return {self.generate()}'
