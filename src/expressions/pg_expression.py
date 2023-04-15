from expressions.pg_boolean import Boolean
from expressions.pg_container import Container
from expressions.pg_function_call import Function_Call
from expressions.pg_number import Number
from expressions.pg_string import String
from expressions.pg_variable import Variable
from formula.pg_formula_node import FN
from formula.pg_formula_pattern import FP, Formula_Pattern
from formula.pg_formula_requirement import FR
from mixins.pg_mixin_generatable import Mixin_Generatable
from mixins.pg_mixin_renderable import Mixin_Renderable

from typing import Self

class Expression(Mixin_Generatable, Mixin_Renderable):

    # TODO there might be more

    def get_patterns(self: Self) -> list[str|Formula_Pattern]:
        return [
            FP(FN(String), reqs=FR('strings'), weight=3),
            FP(FN(Number), reqs=FR('math'), weight=3),
            FP(FN(Boolean), reqs=FR('booleans'), weight=2),
            FP(FN(Container), reqs=FR('containers'), weight=2),
            FP(FN(Function_Call, True), reqs=FR('functions'), weight=2),
            FP(FN(Variable, 'placeholder'), reqs=FR('variables'),weight=1)
        ]
