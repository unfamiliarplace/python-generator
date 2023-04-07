from components.pg_boolean import PG_Boolean
from pg import PythonGenerator
from components.pg_float import PG_Float
from components.pg_integer import PG_Integer
from components.pg_string import PG_String
from js_random import JS_Random as R
from components.pg_renderable import PG_Renderable
from typing import Self

class PG_Expression():

    def __init__(self: Self, pg: PythonGenerator) -> None:
        self.pg = pg

    def generate(self: Self) -> PG_Renderable:
        candidates = []

        if self.pg.on('strings'):
            candidates.append(PG_String())
        
        if self.pg.on('math'):
            if R.flip_coin(.33):
                candidates.append(PG_Float())
            else:
                candidates.append(PG_Integer())

        if self.pg.on('boolean'):
            candidates.append(PG_Boolean())

        return R.choose_from(candidates)

    def __str__(self: Self) -> str:
        return str(self.generate())
