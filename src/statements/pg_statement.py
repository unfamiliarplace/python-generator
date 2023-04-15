from typing import Self
from expressions.pg_expression import Expression
from formula.pg_formula_node import FN
from formula.pg_formula_pattern import FP, Formula_Pattern
from formula.pg_formula_requirement import FR
from lines.pg_assignment import Assignment
from mixins.pg_mixin_generatable import Mixin_Generatable
from mixins.pg_mixin_renderable import Mixin_Renderable

from statements.pg_control import Control
from statements.pg_import import Import

class Statement(Mixin_Generatable, Mixin_Renderable):

    def get_patterns(self: Self) -> list[str|Formula_Pattern]:
        return [
            FP('pass', weight=1),
            FP(FN(Control), reqs=FR('control'), weight=4),
            FP('return', FN(Expression), reqs=FR('functions'), weight=1),
            FP(FN(Assignment), reqs=FR('variables'), weight=3),
            FP(FN(Import), reqs=FR('imports'), weight=2),
        ]
