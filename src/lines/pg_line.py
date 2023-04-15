from expressions.pg_expression import Expression
from formula.pg_formula_node import FN
from formula.pg_formula_requirement import FR
from js_random import JS_Random as R
from typing import Self
from lines.pg_decorator import Decorator
from lines.pg_real_world import Real_World
from lines.pg_symbol_practice import Symbol_Practice
import pg
from pg import PythonGenerator
from statements.pg_statement import Statement

class Line(pg.Mixin_Generatable, pg.Mixin_Renderable):

    def get_patterns(self: Self) -> list[str|pg.FP]:
        return [
            pg.FP(pg.FN(Statement), reqs=pg.FR('statements'), weight=4),
            pg.FP(pg.FN(Expression), reqs=pg.FR('expressions'), weight=5),
            pg.FP(pg.FN(Symbol_Practice), reqs=pg.FR('symbol_practice'), weight=1),
            pg.FP(pg.FN(Real_World), reqs=pg.FR('real_world'), weight=3),
            pg.FP(pg.FN(Decorator), reqs=pg.FR('decorators'), weight=1),
        ]

    def __str__(self: Self) -> str:
        pattern = self.generate()
        s = str(pattern)
        if PythonGenerator().on('comments') and R.flip_coin(0.2):
            if not pattern.uses(Symbol_Practice, Real_World):
                s = '# ' + s
        return s
