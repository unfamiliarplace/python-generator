from js_random import JS_Random as R
from typing import Self
import pg

class Integer(pg.Mixin_Generatable, pg.Mixin_Renderable):
    pass

class Integer_Operation(pg.Mixin_Generatable, pg.Mixin_Renderable_Operation):
    pass

class Integer_Literal(pg.Mixin_Generatable, pg.Mixin_Renderable):

    def __init__(self: Self, lower: int=-50, upper: int=100) -> None:
        self.lower = lower
        self.upper = upper

    def generate(self: Self) -> int:
        return R.number_between(self.lower, self.upper, False)

Integer.patterns = [
    pg.FP(pg.FN(Integer_Literal), weight=4),
    pg.FP(pg.FN(Integer_Operation), weight=1),
    pg.FP(pg.FN(pg.Function_Call, args=[True, 'integer']), weight=1, reqs=pg.FR('functions')),
    pg.FP(pg.FN(pg.Variable, 'integer'), weight=2, reqs=pg.FR('variables')),
    # TODO function int(number, bool, string???, input???)
]

Integer_Operation.patterns = [
    pg.FP(pg.FN(Integer), '+', pg.FN(Integer), weight=3),
    pg.FP(pg.FN(Integer), '-', pg.FN(Integer), weight=3),
    pg.FP(pg.FN(Integer), '*', pg.FN(Integer), weight=2),
    pg.FP(pg.FN(Integer), '//', pg.FN(Integer), weight=2),
    pg.FP(pg.FN(Integer), '**', pg.FN(Integer)),
]
