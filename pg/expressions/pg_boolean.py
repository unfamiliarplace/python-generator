
from expressions.pg_container import Container
import expressions.pg_expression as PG_E
from expressions.pg_function_call import RT, Function_Call
from expressions.pg_variable import Variable
from formula.pg_formula_node import FN
from formula.pg_formula_pattern import FP
from formula.pg_formula_requirement import FR
from mixins.pg_mixin_generatable import Mixin_Generatable
from mixins.pg_mixin_renderable import Mixin_Renderable
from mixins.pg_mixin_renderable_operation import Mixin_Renderable_Operation


class Boolean(Mixin_Generatable, Mixin_Renderable):
    def get_patterns(self) -> list[str|FP]:
        return [
            FP(FN(Boolean_Literal), weight=3),
            FP(FN(Boolean_Operation), weight=1),
            FP(FN(Function_Call, args=[RT.BOOL]), weight=1, reqs=FR('functions')),
            FP(FN(Variable, 'boolean'), weight=2, reqs=FR('booleans')),
            # TODO function bool(expression) ?
        ]

class Boolean_Operation(Mixin_Generatable, Mixin_Renderable_Operation):
    def get_patterns(self) -> list[str|FP]:
        return [
            FP(FN(Boolean), 'and', FN(Boolean), weight=3),
            FP(FN(Boolean), 'or', FN(Boolean), weight=3),
            FP('not', FN(Boolean), weight=2),

            FP(FN(PG_E.Expression), '==', FN(PG_E.Expression), weight=2),
            FP(FN(PG_E.Expression), '>', FN(PG_E.Expression), weight=2),
            FP(FN(PG_E.Expression), '<', FN(PG_E.Expression), weight=2),
            FP(FN(PG_E.Expression), '<=', FN(PG_E.Expression)),
            FP(FN(PG_E.Expression), '>=', FN(PG_E.Expression)),
            FP(FN(PG_E.Expression), '!=', FN(PG_E.Expression), weight=2),
            FP(FN(PG_E.Expression), 'is', FN(PG_E.Expression)),
            FP(FN(PG_E.Expression), 'is not', FN(PG_E.Expression)),
            FP(FN(PG_E.Expression), 'in', FN(Container), reqs=FR('containers'), weight=2),
            FP(FN(PG_E.Expression), 'not in', FN(Container), reqs=FR('containers'))
        ]

class Boolean_Literal(Mixin_Generatable, Mixin_Renderable):
    def get_patterns(self) -> list[str|FP]:
        return [
            FP('True'),
            FP('False'),
        ]
