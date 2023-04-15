from expressions.pg_expression import Expression
from formula.pg_formula_node import FN
from formula.pg_formula_pattern import FP, Formula_Pattern
from formula.pg_formula_requirement import FR
from js_random import JS_Random as R
from typing import Self
from lines.pg_decorator import Decorator
from lines.pg_real_world import Real_World
from lines.pg_symbol_practice import Symbol_Practice
from mixins.pg_mixin_generatable import Mixin_Generatable
from mixins.pg_mixin_renderable import Mixin_Renderable
from pg import PythonGenerator
from statements.pg_statement import Statement

class Line(Mixin_Generatable, Mixin_Renderable):

    def get_patterns(self: Self) -> list[str|Formula_Pattern]:
        return [
            FP(FN(Statement), reqs=FR('statements'), weight=4),
            FP(FN(Expression), reqs=FR('expressions'), weight=5),
            FP(FN(Symbol_Practice), reqs=FR('symbol_practice'), weight=1),
            FP(FN(Real_World), reqs=FR('real_world'), weight=3),
            FP(FN(Decorator), reqs=FR('decorators'), weight=1),
        ]

    def __str__(self: Self) -> str:
        pattern = self.generate()
        s = str(pattern)
        if PythonGenerator().on('comments') and R.flip_coin(0.2):
            if not pattern.uses(Symbol_Practice, Real_World):
                s = '# ' + s
        return s
