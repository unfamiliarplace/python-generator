from components.pg_boolean_operation import PG_Boolean_Operation
from js_random import JS_Random as R
from typing import Self
from components.pg_mixin_generatable import PG_Mixin_Generatable
from components.pg_mixin_renderable import PG_Mixin_Renderable
from components.pg_formula_node import FN
from components.pg_formula_requirement import FR
from components.pg_formula_pattern import FP

class PG_Boolean(PG_Mixin_Generatable, PG_Mixin_Renderable):

    patterns = [
        FP(FN('True'), weight=2),
        FP(FN('False'), weight=2),
        FP(FN(PG_Boolean_Operation), weight=1),
        # FP(FN()) # function bool(expression)
    ]
