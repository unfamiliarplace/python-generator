from components.pg_formula import PG_Formula
from js_random import JS_Random as R
from pg_operation import PG_Operation
from pg_sequence import PG_Sequence
from typing import Self

class PG_Boolean_Operation(PG_Operation):
    formulae = [
        PG_Formula('<PG_Boolean>', 'and', '<PG_Boolean>'),
        PG_Formula('<PG_Boolean>', 'or', '<PG_Boolean>'),
        PG_Formula('not', '<PG_Boolean>'),
    ]

    def __init__(self: Self) -> None:
        pass

    def generate(self: Self) -> PG_Sequence:
        return  R.choose_from(self.formulae).parse()

    def __str__(self: Self) -> str:
        return ''
