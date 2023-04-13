from components.pg_decorator import PG_Decorator
from components.pg_real_world import PG_Real_World
from components.pg_mixin_featurized import PG_Mixin_Featurized
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

class PG_Line(PG_Mixin_Generatable, PG_Mixin_Renderable, PG_Mixin_Featurized):

    patterns = [
        FP(FR('statements'), 5, FN(PG_Statement)),
        FP(FR('expressions'), 5, FN(PG_Expression)),
        FP(FR('symbol_practice'), 1, FN(PG_Symbol_Practice)),
        FP(FR('real_world'), 3, FN(PG_Real_World)),
        FP(FR('decorators'), 1, FN(PG_Decorator)),
    ]

    def __str__(self: Self) -> str:
        pattern = self.generate()
        s = str(pattern)
        if self.pg.on('comments') and R.flip_coin(0.2) and not pattern.uses(PG_Symbol_Practice):
            s = '# ' + s
        return s
