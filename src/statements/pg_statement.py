from typing import Self
from expressions.pg_expression import Expression
from formula.pg_formula_node import FN
from formula.pg_formula_requirement import FR
from lines.pg_assignment import Assignment
import pg

from statements.pg_control import Control
from statements.pg_import import Import

class Statement(pg.Mixin_Generatable, pg.Mixin_Renderable):

    def get_patterns(self: Self) -> list[str|pg.FP]:
        return [
            pg.FP('pass', weight=1),
            pg.FP(pg.FN(Control), reqs=pg.FR('control'), weight=4),
            pg.FP('return', pg.FN(Expression), reqs=pg.FR('functions'), weight=1),
            pg.FP(pg.FN(Assignment), reqs=pg.FR('variables'), weight=3),
            pg.FP(pg.FN(Import), reqs=pg.FR('imports'), weight=2),
        ]
