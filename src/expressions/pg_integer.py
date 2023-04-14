from js_random import JS_Random as R
from typing import Self
from pg import *

class Integer(Mixin_Generatable, Mixin_Renderable):
    pass

class Integer_Operation(Mixin_Generatable, Mixin_Renderable_Operation):
    pass

class Integer_Literal(Mixin_Generatable, Mixin_Renderable):

    def __init__(self: Self, lower: int=-50, upper: int=100) -> None:
        self.lower = lower
        self.upper = upper

    def generate(self: Self) -> int:
        return R.number_between(self.lower, self.upper, False)

Integer.patterns = [
    FP(FN(Integer_Literal), weight=4),
    FP(FN(Integer_Operation), weight=1),
    FP(FN(Function_Call, args=[True, 'integer']), weight=1, reqs=FR('functions')),
    FP(FN(Variable, 'integer'), weight=2, reqs=FR('variables')),
    # TODO function int(number, bool, string???, input???)
]

Integer_Operation.patterns = [
    FP(FN(Integer), '+', FN(Integer), weight=3),
    FP(FN(Integer), '-', FN(Integer), weight=3),
    FP(FN(Integer), '*', FN(Integer), weight=2),
    FP(FN(Integer), '//', FN(Integer), weight=2),
    FP(FN(Integer), '**', FN(Integer)),
]
