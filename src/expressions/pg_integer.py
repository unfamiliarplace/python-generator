from js_random import JS_Random as R
from typing import Self
import pg


class Integer(pg.Mixin_Generatable, pg.Mixin_Renderable):

    def __init__(self: Self, lower: int=-50, upper: int=100) -> None:
        self.lower = lower
        self.upper = upper

    def get_patterns(self: Self) -> list[str|pg.FP]:
        return [
            pg.FP(pg.FN(Integer_Literal, self.lower, self.upper), weight=4),
            pg.FP(pg.FN(Integer_Operation, self.lower, self.upper), weight=1),
            pg.FP(pg.FN(pg.Function_Call, args=[pg.Return_Type.INT]), weight=1, reqs=pg.FR('functions')),
            pg.FP(pg.FN(pg.Variable, 'integer'), weight=2, reqs=pg.FR('variables')),
            # TODO function int(number, bool, string???, input???)
        ]

class Integer_Operation(pg.Mixin_Generatable, pg.Mixin_Renderable_Operation):

    def __init__(self: Self, lower: int=-50, upper: int=100) -> None:
        self.lower = lower
        self.upper = upper

    def get_patterns(self: Self) -> list[str|pg.FP]:
        return [
            pg.FP(pg.FN(Integer, self.lower, self.upper), '+', pg.FN(Integer, self.lower, self.upper), weight=3),
            pg.FP(pg.FN(Integer, self.lower, self.upper), '-', pg.FN(Integer, self.lower, self.upper), weight=3),
            pg.FP(pg.FN(Integer, self.lower, self.upper), '*', pg.FN(Integer, self.lower, self.upper), weight=2),
            pg.FP(pg.FN(Integer, self.lower, self.upper), '//', pg.FN(Integer, self.lower, self.upper), weight=2),
            pg.FP(pg.FN(Integer, self.lower, self.upper), '**', pg.FN(Integer, self.lower, self.upper), weight=1),
        ]

class Integer_Literal(pg.Mixin_Generatable, pg.Mixin_Renderable):

    def __init__(self: Self, lower: int=-50, upper: int=100) -> None:
        self.lower = lower
        self.upper = upper

    def generate(self: Self) -> int:
        return R.number_between(self.lower, self.upper, False)
