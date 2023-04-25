from js_random import JS_Random as R

from expressions.pg_function_call import RT, Function_Call
from expressions.pg_variable import Variable
from formula.pg_formula_node import FN
from formula.pg_formula_pattern import FP
from formula.pg_formula_requirement import FR
from mixins.pg_mixin_generatable import Mixin_Generatable
from mixins.pg_mixin_renderable import Mixin_Renderable
from mixins.pg_mixin_renderable_operation import Mixin_Renderable_Operation

class Integer(Mixin_Generatable, Mixin_Renderable):

    def __init__(self, lower: int=-50, upper: int=100) -> None:
        self.lower = lower
        self.upper = upper
        super().__init__()

    def get_patterns(self) -> list[str|FP]:
        return [
            FP(FN(Integer_Literal, self.lower, self.upper), weight=4),
            FP(FN(Integer_Operation, self.lower, self.upper), weight=1),
            FP(FN(Function_Call, args=[RT.INT]), weight=1, reqs=FR('functions')),
            FP(FN(Variable, 'integer'), weight=2, reqs=FR('variables')),
            # TODO function int(number, bool, string???, input???)
        ]

class Integer_Operation(Mixin_Generatable, Mixin_Renderable_Operation):

    def __init__(self, lower: int=-50, upper: int=100) -> None:
        self.lower = lower
        self.upper = upper
        super.__init__()

    def get_patterns(self) -> list[str|FP]:
        return [
            FP(FN(Integer, self.lower, self.upper), '+', FN(Integer, self.lower, self.upper), weight=3),
            FP(FN(Integer, self.lower, self.upper), '-', FN(Integer, self.lower, self.upper), weight=3),
            FP(FN(Integer, self.lower, self.upper), '*', FN(Integer, self.lower, self.upper), weight=2),
            FP(FN(Integer, self.lower, self.upper), '//', FN(Integer, self.lower, self.upper), weight=2),
            FP(FN(Integer, self.lower, self.upper), '**', FN(Integer, self.lower, self.upper), weight=1),
        ]

class Integer_Literal(Mixin_Generatable, Mixin_Renderable):

    def __init__(self, lower: int=-50, upper: int=100) -> None:
        self.lower = lower
        self.upper = upper

    def generate(self) -> int:
        return R.number_between(self.lower, self.upper, False)
