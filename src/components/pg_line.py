from components.pg_renderable import PG_Renderable
from js_random import JS_Random as R
from pg import PythonGenerator
from components.pg_statement import PG_Statement
from components.pg_expression import PG_Expression
from typing import Self

class PG_Line():

    def __init__(self: Self, pg: PythonGenerator) -> None:
        self.pg = pg

    def generate(self: Self) -> PG_Renderable:
        if self.pg.any('controls', 'functions') and R.flip_coin():
            return PG_Statement(self.pg)
        else:
            return PG_Expression(self.pg)

    def __str__(self: Self) -> str:
        line = str(self.generate())
        if self.pg.on('symbols') and R.flip_coin(0.05):
            line = '# ' + line
        return line
