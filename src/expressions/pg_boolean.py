from expressions.pg_container import Container
from expressions.pg_expression import Expression
from expressions.pg_function_call import Function_Call
from expressions.pg_variable import Variable
from formula.pg_formula_node import FN
from formula.pg_formula_pattern import FP, Formula_Pattern
from formula.pg_formula_requirement import FR
from mixins.pg_mixin_generatable import Mixin_Generatable
from mixins.pg_mixin_renderable import Mixin_Renderable
from mixins.pg_mixin_renderable_operation import Mixin_Renderable_Operation

from typing import Self

class Boolean(Mixin_Generatable, Mixin_Renderable):
    def get_patterns(self: Self) -> list[str|Formula_Pattern]:
        return [
            FP(FN(Boolean_Literal), weight=3),
            FP(FN(Boolean_Operation), weight=1),
            FP(FN(Function_Call, args=[True, 'boolean']), weight=1, reqs=FR('functions')),
            FP(FN(Variable, 'boolean'), weight=2, reqs=FR('booleans'))
        ]

class Boolean_Operation(Mixin_Generatable, Mixin_Renderable_Operation):
    def get_patterns(self: Self) -> list[str|Formula_Pattern]:
        return [
            FP(FN(Boolean), 'and', FN(Boolean), weight=3),
            FP(FN(Boolean), 'or', FN(Boolean), weight=3),
            FP('not', FN(Boolean), weight=2),

            FP(FN(Expression), '==', FN(Expression), weight=2),
            FP(FN(Expression), '>', FN(Expression), weight=2),
            FP(FN(Expression), '<', FN(Expression), weight=2),
            FP(FN(Expression), '<=', FN(Expression)),
            FP(FN(Expression), '>=', FN(Expression)),
            FP(FN(Expression), '!=', FN(Expression), weight=2),
            FP(FN(Expression), 'is', FN(Expression)),
            FP(FN(Expression), 'is not', FN(Expression)),
            FP(FN(Expression), 'in', FN(Container), weight=2),
            FP(FN(Expression), 'not in', FN(Container))
        ]

class Boolean_Literal(Mixin_Generatable, Mixin_Renderable):
    def get_patterns(self: Self) -> list[str|Formula_Pattern]:
        return [
            FP(FN('True'), weight=20),
            FP(FN('False'), weight=20),
            FP(FN(Boolean_Operation), weight=10),
            # TODO function bool(expression)
        ]
