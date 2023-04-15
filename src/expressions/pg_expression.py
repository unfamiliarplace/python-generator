from expressions.pg_boolean import Boolean
from expressions.pg_container import Container
from expressions.pg_function_call import Function_Call
from expressions.pg_number import Number
from expressions.pg_string import String
from expressions.pg_variable import Variable
from formula.pg_formula_node import FN
from formula.pg_formula_pattern import FP, Formula_Pattern
from formula.pg_formula_requirement import FR
import pg

from typing import Self

class Expression(pg.Mixin_Generatable, pg.Mixin_Renderable):

    # TODO there might be more

    def get_patterns(self: Self) -> list[str|pg.FP]:
        return [
            pg.FP(pg.FN(String), reqs=pg.FR('strings'), weight=3),
            pg.FP(pg.FN(Number), reqs=pg.FR('math'), weight=3),
            pg.FP(pg.FN(Boolean), reqs=pg.FR('booleans'), weight=2),
            pg.FP(pg.FN(Container), reqs=pg.FR('containers'), weight=2),
            pg.FP(pg.FN(Function_Call, True), reqs=pg.FR('functions'), weight=2),
            pg.FP(pg.FN(Variable, 'placeholder'), reqs=pg.FR('variables'),weight=1)
        ]
