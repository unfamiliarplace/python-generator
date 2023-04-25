from mixins.pg_mixin_generatable import Mixin_Generatable
from mixins.pg_mixin_renderable import Mixin_Renderable
from statements.pg_statement import Statement
from expressions.pg_expression import Expression
from lines.pg_symbol_practice import Symbol_Practice
from lines.pg_real_world import Real_World
from lines.pg_decorator import Decorator
from lines.pg_comment import Comment
from formula.pg_formula_pattern import FP
from formula.pg_formula_node import FN
from formula.pg_formula_requirement import FR

class Line(Mixin_Generatable, Mixin_Renderable):

    def get_patterns(self) -> list[str|FP]:
        return [
            FP(FN(Statement), reqs=FR('statements'), weight=8),
            FP(FN(Expression), reqs=FR('expressions'), weight=10),
            FP(FN(Symbol_Practice), reqs=FR('symbol_practice'), weight=1),
            FP(FN(Real_World), reqs=FR('real_world'), weight=5),
            FP(FN(Decorator), reqs=FR('decorators'), weight=1),
            FP(FN(Comment), reqs=FR('comments'), weight=3),
        ]
