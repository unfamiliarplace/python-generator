
from expressions.pg_function_call import RT, Function_Call
from formula.pg_formula_node import FN
from formula.pg_formula_pattern import FP
from formula.pg_formula_requirement import FR
from mixins.pg_mixin_generatable import Mixin_Generatable
from mixins.pg_mixin_renderable import Mixin_Renderable

class None_Node(Mixin_Generatable, Mixin_Renderable):
    def get_patterns(self) -> list[str|FP]:
        return [
            FP('None', weight=3),
            FP(FN(Function_Call, args=[RT.NONE]), weight=1, reqs=FR('functions')),
        ]
