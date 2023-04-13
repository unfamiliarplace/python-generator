from components.pg_mixin_generatable import PG_Mixin_Generatable
from components.pg_mixin_renderable import PG_Mixin_Renderable
from components.pg_formula_node import FN
from components.pg_formula_requirement import FR
from components.pg_formula_pattern import FP
from components.pg_assignment import PG_Assignment
from components.pg_expression import PG_Expression
from components.pg_control import PG_Control

class PG_Statement(PG_Mixin_Generatable, PG_Mixin_Renderable):

    patterns = [
        FP(FN(PG_Control)),
        FP('return', FN(PG_Expression), reqs=FR('functions')),
        FP(FN(PG_Assignment), reqs=FR('variables'))
    ]
