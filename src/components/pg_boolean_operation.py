from js_random import JS_Random as R
from components.pg_formula import PG_Formula
from pg_sequence import PG_Sequence
from typing import Self
from components.pg_mixin_generatable import PG_Mixin_Generatable
from components.pg_mixin_renderable import PG_Mixin_Renderable

class PG_Boolean_Operation(PG_Mixin_Generatable, PG_Mixin_Renderable):

    formulae = [
        # TODO Operations within operations?
        PG_Formula('<PG_Boolean>', 'and', '<PG_Boolean>'),
        PG_Formula('<PG_Boolean>', 'or', '<PG_Boolean>'),
        PG_Formula('not', '<PG_Boolean>'),
    ]

    def generate(self: Self) -> PG_Sequence:
        return  R.choose_from(self.formulae).parse()

    def __str__(self: Self) -> str:
        return ''
