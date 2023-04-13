from components.pg_boolean import PG_Boolean
from components.pg_container import PG_Container
from components.pg_variable import PG_Variable
from components.pg_mixin_generatable import PG_Mixin_Generatable
from components.pg_mixin_renderable import PG_Mixin_Renderable
from components.pg_formula_node import FN
from components.pg_formula_requirement import FR
from components.pg_formula_pattern import FP

class PG_Control(PG_Mixin_Generatable, PG_Mixin_Renderable):

    patterns = [
        # TODO for i in range(int)
        # TODO for i in range(len(container))

        FP('for', FN(PG_Variable, 'element'), 'in', FN(PG_Container), reqs=FR('containers')),

        # TODO instead, have container have a variable of type container as a pattern
        # FP('for', FN(PG_Variable, 'element'), 'in', FN(PG_Variable, 'container'), reqs=FR('containers')),

        FP('while', FN(PG_Boolean)),
        FP('if', FN(PG_Boolean))
    ]
