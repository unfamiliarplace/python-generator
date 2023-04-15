from expressions.pg_function_call import Function_Call
from expressions.pg_number import Number
from expressions.pg_variable import Variable
from formula.pg_formula_node import FN
from formula.pg_formula_pattern import FP, Formula_Pattern
from formula.pg_formula_requirement import FR
from js_random import JS_Random as R
from typing import Self
import pg


class Float(pg.Mixin_Generatable, pg.Mixin_Renderable):
    def get_patterns(self: Self) -> list[str|pg.FP]:
        return [
            pg.FP(pg.FN(Float_Literal), weight=4),
            pg.FP(pg.FN(Float_Operation), weight=1),
            pg.FP(pg.FN(Function_Call, args=[True, 'float']), weight=1, reqs=pg.FR('functions')),
            pg.FP(pg.FN(Variable, 'float'), weight=2, reqs=pg.FR('variables')),
            # TODO function float(number, bool, string???, input???)
        ]

class Float_Operation(pg.Mixin_Generatable, pg.Mixin_Renderable_Operation):
    def get_patterns(self: Self) -> list[str|pg.FP]:
        return [
            pg.FP(pg.FN(Number), '+', pg.FN(Float), weight=3),
            pg.FP(pg.FN(Float), '+', pg.FN(Number), weight=3),

            pg.FP(pg.FN(Number), '-', pg.FN(Float), weight=3),
            pg.FP(pg.FN(Float), '-', pg.FN(Number), weight=3),

            pg.FP(pg.FN(Number), '*', pg.FN(Float), weight=2),
            pg.FP(pg.FN(Float), '*', pg.FN(Number), weight=2),

            pg.FP(pg.FN(Number), '/', pg.FN(Number), weight=2),

            pg.FP(pg.FN(Number), '//', pg.FN(Float), weight=2),
            pg.FP(pg.FN(Float), '//', pg.FN(Number), weight=2),

            pg.FP(pg.FN(Number), '**', pg.FN(Float)),
            pg.FP(pg.FN(Float), '**', pg.FN(Number)),
        ]

class Float_Literal(pg.Mixin_Generatable, pg.Mixin_Renderable):

    def __init__(self: Self, lower: int=-50, upper: int=100) -> None:
        self.lower = lower
        self.upper = upper

    def generate(self: Self) -> float:
        return R.number_between(self.lower, self.upper, True)
