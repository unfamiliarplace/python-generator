from components.pg_renderable import PG_Renderable
from js_random import JS_Random as R
from pg import PythonGenerator
from components.pg_control import PG_Control
from components.pg_return import PG_Return
from typing import Self

class PG_Statement():
    
    def __init__(self: Self, pg: PythonGenerator) -> None:
        self.pg = pg

    def generate(self: Self) -> PG_Renderable:
        candidates = []

        # TODO
        if self.pg.on('functions'):
            candidates.append(PG_Return())

        if self.pg.on('controls'):
            candidates.append(PG_Control())

        return R.choose_from(candidates)
    
    def __str__(self: Self) -> str:
        return str(self.generate())
