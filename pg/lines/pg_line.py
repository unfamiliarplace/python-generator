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

def brackets_are_good(s: str) -> bool:
    depth_b = 0
    depth_s = 0
    depth_c = 0

    for c in s:
        depth_b += (c == '(')
        depth_s += (c == '[')
        depth_c += (c == '{')

        if c == ')':
            if depth_b < 1:
                return False
            depth_b -= 1

        if c == ']':
            if depth_s < 1:
                return False
            depth_s -= 1

        if c == '}':
            if depth_c < 1:
                return False
            depth_c -= 1
    
    return (depth_b + depth_s + depth_c) == 0

def strip_unnecessary_brackets(s: str) -> str:
    if (s[0] + s[-1]) == '()':
        inner = s[1:-1]
        if brackets_are_good(inner):
            return inner
    return s

class Line(Mixin_Generatable, Mixin_Renderable):

    def get_patterns(self) -> list[str|FP]:
        return [
            FP(FN(Statement), reqs=FR('statements'), weight=8),
            FP(FN(Expression), reqs=FR('expressions'), weight=10),
            FP(FN(Symbol_Practice), reqs=FR('symbol_practice'), weight=1),
            FP(FN(Real_World), reqs=FR('real_world'), weight=5),
            FP(FN(Decorator), reqs=FR('decorators'), weight=1),
            FP(FN(Comment), reqs=FR('comments'), weight=3)
        ]

    def str(self) -> str:
        return strip_unnecessary_brackets(str(self.generate()))
