from components.pg_renderable import PG_Renderable
from components.pg_sequence import PG_Sequence
from js_random import JS_Random as R
from components.pg_formula import PG_Formula
from typing import Self

class PG_Control(PG_Renderable):
    
    formulae = [
        # TODO
        # PG_Formula('for i in', '<PG_Function|range;<PG_Variable|"number">'),
        # PG_Formula('for i in', '<PG_Function|range;[2,101]>'),
        PG_Formula('for', '<PG_Variable>', 'in', '<PG_Container>'),
        PG_Formula('for', '<PG_Variable>', 'in', '<PG_Variable|type="container">'),
        PG_Formula('while', '<PG_Boolean>'),
        PG_Formula('if', '<PG_Boolean>'),
    ]

    def __init__(self: Self) -> None:
        pass

    def generate(self: Self) -> PG_Sequence:
        return R.choose_from(self.formulae).parse()
    
    def __str__(self: Self) -> str:
        return f'{self.generate()}:'
