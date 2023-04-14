from js_random import JS_Random as R
from typing import Self
from pg import *

class Float(Mixin_Generatable, Mixin_Renderable):
    pass

class Float_Operation(Mixin_Generatable, Mixin_Renderable_Operation):
    pass

class Float_Literal(Mixin_Generatable, Mixin_Renderable):

    def __init__(self: Self, lower: int=-50, upper: int=100) -> None:
        self.lower = lower
        self.upper = upper

    def generate(self: Self) -> int:
        return R.number_between(self.lower, self.upper, True)

Float.patterns = [
    FP(FN(Float_Literal), weight=4),
    FP(FN(Float_Operation), weight=1),
    FP(FN(Function_Call, args=[True, 'float']), weight=1, reqs=FR('functions')),
    FP(FN(Variable, 'float'), weight=2, reqs=FR('variables')),
    # TODO function float(number, bool, string???, input???)
]

Float_Operation.patterns = [
    FP(FN(Number), '+', FN(Float), weight=3),
    FP(FN(Float), '+', FN(Number), weight=3),

    FP(FN(Number), '-', FN(Float), weight=3),
    FP(FN(Float), '-', FN(Number), weight=3),

    FP(FN(Number), '*', FN(Float), weight=2),
    FP(FN(Float), '*', FN(Number), weight=2),

    FP(FN(Number), '/', FN(Number), weight=2),

    FP(FN(Number), '//', FN(Float), weight=2),
    FP(FN(Float), '//', FN(Number), weight=2),

    FP(FN(Number), '**', FN(Float)),
    FP(FN(Float), '**', FN(Number)),
]