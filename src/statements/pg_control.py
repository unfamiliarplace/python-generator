from typing import Self
from expressions.pg_boolean import Boolean
from expressions.pg_container import Container
from expressions.pg_variable import Variable
from formula.pg_formula_node import FN
from formula.pg_formula_pattern import FP, Formula_Pattern
from formula.pg_formula_requirement import FR
from mixins.pg_mixin_generatable import Mixin_Generatable
from mixins.pg_mixin_renderable import Mixin_Renderable


class Control(Mixin_Generatable, Mixin_Renderable):

    def get_patterns(self: Self) -> list[str|Formula_Pattern]:
        return [
        # TODO for i in range(int)
        # TODO for i in range(len(container))

        FP('for', FN(Variable, 'element'), 'in', FN(Container), reqs=FR('containers')),

        # TODO instead, have container have a variable of type container as a pattern
        # FP('for', FN(Variable, 'element'), 'in', FN(Variable, 'container'), reqs=FR('containers')),

        FP('while', FN(Boolean)),
        FP('if', FN(Boolean)),

        FP('break')
    ]
