from components.pg_boolean import PG_Boolean
from components.pg_container import PG_Container
from components.pg_float import PG_Float
from components.pg_function_call import PG_Function_Call
from components.pg_integer import PG_Integer
from components.pg_string import PG_String
from components.pg_variable import PG_Variable
from components.pg_mixin_generatable import PG_Mixin_Generatable
from components.pg_mixin_renderable import PG_Mixin_Renderable
from components.pg_formula_node import FN
from components.pg_formula_requirement import FR
from components.pg_formula_pattern import FP

class PG_Expression(PG_Mixin_Generatable, PG_Mixin_Renderable):

    # TODO there might be more

    patterns = [
        FP(FN(PG_String), reqs=FR('strings'), weight=3),
        FP(FN(PG_Float), reqs=FR('math'), weight=2),
        FP(FN(PG_Integer), reqs=FR('math'), weight=3),
        FP(FN(PG_Boolean), reqs=FR('booleans'), weight=2),
        FP(FN(PG_Container), reqs=FR('containers'), weight=2),
        FP(FN(PG_Function_Call, True), reqs=FR('functions'), weight=2),
        FP(FN(PG_Variable, 'placeholder'), reqs=FR('variables'),weight=1)
    ]
