
from expressions.pg_float import Float
from expressions.pg_integer import Integer
from formula.pg_formula_node import FN
from formula.pg_formula_pattern import FP
from mixins.pg_mixin_generatable import Mixin_Generatable
from mixins.pg_mixin_renderable import Mixin_Renderable

class Number(Mixin_Generatable, Mixin_Renderable):

    def get_patterns(self) -> list[str|FP]:
        return [
            FP(FN(Integer), weight=3),
            FP(FN(Float), weight=1)
        ]
