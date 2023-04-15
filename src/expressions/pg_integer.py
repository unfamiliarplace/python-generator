from expressions.pg_function_call import Function_Call
from expressions.pg_variable import Variable
from formula.pg_formula_node import FN
from formula.pg_formula_pattern import FP, Formula_Pattern
from formula.pg_formula_requirement import FR
from js_random import JS_Random as R
from typing import Self
from mixins.pg_mixin_generatable import Mixin_Generatable
from mixins.pg_mixin_renderable import Mixin_Renderable
from mixins.pg_mixin_renderable_operation import Mixin_Renderable_Operation


class Integer(Mixin_Generatable, Mixin_Renderable):

    def get_patterns(self: Self) -> list[str|Formula_Pattern]:
        return [
            FP(FN(Integer_Literal), weight=4),
            FP(FN(Integer_Operation), weight=1),
            FP(FN(Function_Call, args=[True, 'integer']), weight=1, reqs=FR('functions')),
            FP(FN(Variable, 'integer'), weight=2, reqs=FR('variables')),
            # TODO function int(number, bool, string???, input???)
        ]

class Integer_Operation(Mixin_Generatable, Mixin_Renderable_Operation):

    def get_patterns(self: Self) -> list[str|Formula_Pattern]:
        return [
            FP(FN(Integer), '+', FN(Integer), weight=3),
            FP(FN(Integer), '-', FN(Integer), weight=3),
            FP(FN(Integer), '*', FN(Integer), weight=2),
            FP(FN(Integer), '//', FN(Integer), weight=2),
            FP(FN(Integer), '**', FN(Integer)),
        ]

class Integer_Literal(Mixin_Generatable, Mixin_Renderable):

    def __init__(self: Self, lower: int=-50, upper: int=100) -> None:
        self.lower = lower
        self.upper = upper

    def generate(self: Self) -> int:
        return R.number_between(self.lower, self.upper, False)
