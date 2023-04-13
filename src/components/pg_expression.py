from components.pg_boolean import PG_Boolean
from components.pg_float import PG_Float
from components.pg_integer import PG_Integer
from components.pg_string import PG_String
from js_random import JS_Random as R
from typing import Self
from components.pg_mixin_generatable import PG_Mixin_Generatable
from components.pg_mixin_renderable import PG_Mixin_Renderable
from pg import PythonGenerator

class PG_Expression(PG_Mixin_Generatable, PG_Mixin_Renderable):

    def generate(self: Self) -> PG_Mixin_Renderable:
        candidates = []

        if PythonGenerator().on('strings'):
            candidates.append(PG_String())
        
        if PythonGenerator().on('math'):
            if R.flip_coin(.33):
                candidates.append(PG_Float())
            else:
                candidates.append(PG_Integer())

        if PythonGenerator().on('boolean'):
            candidates.append(PG_Boolean())

        return R.choose_from(candidates)

    def __str__(self: Self) -> str:
        return str(self.generate())
