from js_random import JS_Random as R

from expressions.pg_function_call import RT, Function_Call
import expressions.pg_number as PG_N
from expressions.pg_variable import Variable
from formula.pg_formula_node import FN
from formula.pg_formula_pattern import FP
from formula.pg_formula_requirement import FR
from mixins.pg_mixin_generatable import Mixin_Generatable
from mixins.pg_mixin_renderable import Mixin_Renderable
from mixins.pg_mixin_renderable_operation import Mixin_Renderable_Operation

class Float(Mixin_Generatable, Mixin_Renderable):
    def get_patterns(self) -> list[str|FP]:
        return [
            FP(FN(Float_Literal), weight=4),
            FP(FN(Float_Operation), weight=1),
            FP(FN(Function_Call, args=[RT.FLOAT]), weight=1, reqs=FR('functions')),
            FP(FN(Variable, 'float'), weight=2, reqs=FR('variables')),
            # TODO function float(number, bool, string???, input???)
        ]

class Float_Operation(Mixin_Generatable, Mixin_Renderable_Operation):
    def get_patterns(self) -> list[str|FP]:
        return [
            FP(FN(PG_N.Number), '+', FN(Float), weight=3),
            FP(FN(Float), '+', FN(PG_N.Number), weight=3),

            FP(FN(PG_N.Number), '-', FN(Float), weight=3),
            FP(FN(Float), '-', FN(PG_N.Number), weight=3),

            FP(FN(PG_N.Number), '*', FN(Float), weight=2),
            FP(FN(Float), '*', FN(PG_N.Number), weight=2),

            FP(FN(PG_N.Number), '/', FN(PG_N.Number), weight=2),

            FP(FN(PG_N.Number), '//', FN(Float), weight=2),
            FP(FN(Float), '//', FN(PG_N.Number), weight=2),

            FP(FN(PG_N.Number), '**', FN(Float)),
            FP(FN(Float), '**', FN(PG_N.Number)),
        ]

class Float_Literal(Mixin_Generatable, Mixin_Renderable):

    def __init__(self, lower: int=-50, upper: int=100) -> None:
        super().__init__()
        self.lower = lower
        self.upper = upper

    def generate(self) -> float:
        return R.number_between(self.lower, self.upper, True)
