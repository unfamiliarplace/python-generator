
from expressions.pg_expression import Expression
from expressions.pg_integer import Integer
from expressions.pg_number import Number
from expressions.pg_string import String
from expressions.pg_variable import Variable
from formula.pg_formula_node import FN
from formula.pg_formula_pattern import FP
from mixins.pg_mixin_generatable import Mixin_Generatable
from mixins.pg_mixin_renderable import Mixin_Renderable

class Assignment(Mixin_Generatable, Mixin_Renderable):

    def get_patterns(self) -> list[str|FP]:
        return [
            # TODO variables should be matched with expressions of matching type
            FP(FN(Variable), '=', FN(Expression), weight=10),

            FP(FN(Variable, 'integer'), '+=', FN(Number), weight=5),
            FP(FN(Variable, 'float'), '+=', FN(Number), weight=5),
            FP(FN(Variable, 'string'), '+=', FN(String), weight=2),

            FP(FN(Variable, 'integer'), '-=', FN(Number), weight=5),
            FP(FN(Variable, 'float'), '-=', FN(Number), weight=5),

            FP(FN(Variable, 'integer'), '*=', FN(Number), weight=3),
            FP(FN(Variable, 'float'), '*=', FN(Number), weight=3),
            FP(FN(Variable, 'string'), '*=', FN(Integer), weight=1),
            FP(FN(Variable, 'integer'), '*=', FN(String), weight=1),

            FP(FN(Variable, 'integer'), '/=', FN(Number), weight=2),
            FP(FN(Variable, 'float'), '/=', FN(Number), weight=2),
             FP(FN(Variable, 'integer'), '//=', FN(Number), weight=2),
            FP(FN(Variable, 'float'), '//=', FN(Number), weight=2),
            FP(FN(Variable, 'integer'), '**=', FN(Number), weight=1),
            FP(FN(Variable, 'float'), '**=', FN(Number), weight=1),
        ]
