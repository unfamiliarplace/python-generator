from components.pg_expression import PG_Expression
from components.pg_sequence import PG_Sequence
from typing import Self
from components.pg_variable import PG_Variable
from components.pg_mixin_generatable import PG_Mixin_Generatable
from components.pg_mixin_renderable import PG_Mixin_Renderable

class PG_Assignment(PG_Mixin_Generatable, PG_Mixin_Renderable):

    def generate(self: Self) -> PG_Sequence:
        # TODO +=, -=, /=, *=, **=, //=, %=
        # TODO names corresponding to types
        return PG_Sequence(PG_Variable(), '=', PG_Expression())

    def __str__(self: Self) -> str:
        return str(self.generate())
