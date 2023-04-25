import expressions.pg_boolean as PG_B
from expressions.pg_container import Container
from expressions.pg_function_call import Function_Call
from expressions.pg_none import None_Node
from expressions.pg_number import Number
from expressions.pg_string import String
from expressions.pg_variable import Variable
from formula.pg_formula_node import FN
from formula.pg_formula_pattern import FP
from formula.pg_formula_requirement import FR
from mixins.pg_mixin_generatable import Mixin_Generatable
from mixins.pg_mixin_renderable import Mixin_Renderable

class Expression(Mixin_Generatable, Mixin_Renderable):

    # TODO there might be more

    def get_patterns(self) -> list[str|FP]:
        return [
            FP(FN(String), reqs=FR('strings'), weight=6),
            FP(FN(Number), reqs=FR('math'), weight=6),
            FP(FN(PG_B.Boolean), reqs=FR('booleans'), weight=4),
            FP(FN(Container), reqs=FR('containers'), weight=3),
            FP(FN(Function_Call, True), reqs=FR('functions'), weight=4),
            FP(FN(Variable), reqs=FR('variables'),weight=2),
            FP(FN(None_Node), weight=1),
        ]
