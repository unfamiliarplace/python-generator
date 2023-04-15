from typing import Self
from expressions.pg_boolean import Boolean
from expressions.pg_container import Container
from expressions.pg_variable import Variable
from formula.pg_formula_node import FN
from formula.pg_formula_requirement import FR
import pg


class Control(pg.Mixin_Generatable, pg.Mixin_Renderable):

    def get_patterns(self: Self) -> list[str|pg.FP]:
        return [
        # TODO for i in range(int)
        # TODO for i in range(len(container))

        pg.FP('for', pg.FN(Variable, 'element'), 'in', pg.FN(Container), reqs=pg.FR('containers')),

        # TODO instead, have container have a variable of type container as a pattern
        # pg.FP('for', pg.FN(Variable, 'element'), 'in', pg.FN(Variable, 'container'), reqs=pg.FR('containers')),

        pg.FP('while', pg.FN(Boolean)),
        pg.FP('if', pg.FN(Boolean)),

        pg.FP('break')
    ]
