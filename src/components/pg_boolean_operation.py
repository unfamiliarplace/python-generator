from components.pg_boolean import PG_Boolean
from components.pg_mixin_generatable import PG_Mixin_Generatable
from components.pg_mixin_renderable import PG_Mixin_Renderable
from components.pg_formula_node import FN
from components.pg_formula_requirement import FR
from components.pg_formula_pattern import FP

class PG_Boolean_Operation(PG_Mixin_Generatable, PG_Mixin_Renderable):

    patterns = [
        FP(FN(PG_Boolean), 'and', FN(PG_Boolean)),
        FP(FN(PG_Boolean), 'or', FN(PG_Boolean)),
        FP('not', FN(PG_Boolean)),
    ]
