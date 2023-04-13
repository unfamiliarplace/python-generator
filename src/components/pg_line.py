from components.pg_decorator import PG_Decorator
from components.pg_real_world import PG_Real_World
from components.pg_symbol_practice import PG_Symbol_Practice
from js_random import JS_Random as R
from components.pg_statement import PG_Statement
from components.pg_expression import PG_Expression
from typing import Self
from components.pg_mixin_generatable import PG_Mixin_Generatable
from components.pg_mixin_renderable import PG_Mixin_Renderable
from components.pg_formula_node import FN
from components.pg_formula_requirement import FR
from components.pg_formula_pattern import FP
from pg import PythonGenerator

class PG_Line(PG_Mixin_Generatable, PG_Mixin_Renderable):

    patterns = [
        FP(FN(PG_Statement), reqs=FR('statements'), weight=4),
        FP(FN(PG_Expression), reqs=FR('expressions'), weight=5),
        FP(FN(PG_Symbol_Practice), reqs=FR('symbol_practice'), weight=1),
        FP(FN(PG_Real_World), reqs=FR('real_world'), weight=3),
        FP(FN(PG_Decorator), reqs=FR('decorators'), weight=1),
    ]

    def __str__(self: Self) -> str:
        pattern = self.generate()
        s = str(pattern)
        if PythonGenerator().on('comments') and R.flip_coin(0.2) and not pattern.uses(PG_Symbol_Practice):
            s = '# ' + s
        return s
