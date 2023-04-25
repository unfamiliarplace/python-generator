
from expressions.pg_boolean import Boolean
from expressions.pg_container import Container
from expressions.pg_variable import Variable
from formula.pg_formula_node import FN
from formula.pg_formula_pattern import FP
from formula.pg_formula_requirement import FR
from mixins.pg_mixin_generatable import Mixin_Generatable
from mixins.pg_mixin_renderable import Mixin_Renderable

class Control(Mixin_Generatable, Mixin_Renderable):

    def get_patterns(self) -> list[str|FP]:
        return [
        # TODO for i in range(int)
        # TODO for i in range(len(container))

        FP('for', FN(Variable, 'element'), 'in', FN(Container), reqs=FR('containers'), suffix=':'),

        FP('while', FN(Boolean), suffix=':'),
        FP('break'),

        FP('if', FN(Boolean), suffix=':'),
        FP('elif', FN(Boolean), suffix=':'),
        FP('else', suffix=':'),

        FP('try', suffix=':'),
        FP('except', suffix=':'),
        FP('except', FN(Exception), suffix=':'),
    ]
