from components.pg_expression import PG_Expression
from components.pg_sequence import PG_Sequence
from typing import Self
from components.pg_variable import PG_Variable
from components.pg_mixin_generatable import PG_Mixin_Generatable
from components.pg_mixin_renderable import PG_Mixin_Renderable
from components.pg_formula_node import FN
from components.pg_formula_pattern import FP

class PG_Assignment(PG_Mixin_Generatable, PG_Mixin_Renderable):

    patterns = [
        FP(FN(PG_Variable), '=', FN(PG_Expression))
    ]
