from typing import Self
from formula.pg_formula_pattern import Formula_Pattern
from js_random import JS_Random as R
from mixins.pg_mixin_generatable import Mixin_Generatable
from mixins.pg_mixin_renderable import Mixin_Renderable


class Variable(Mixin_Generatable, Mixin_Renderable):

    patterns = [
        'integer', 'string', 'float', 'boolean', 'container', 'misc', 'index', 'element', 'placeholder'
    ]

    type_to_names = {
        'integer': ['n', 'm', 'n_students', 'n_doughnuts', 'count', 'total'],
        'string': ['name', 'person', 'winner'],
        'float': ['fraction', 'proportion'],
        'boolean': ['is_valid', 'is_allowed', 'is_done', 'has_finished', 'has_loaded', 'exists'],
        'container': ['names', 'ages', 'people', 'pizzas', 'values'],
        'misc': ['x', 'y', 'z', 'a', 'b', 'c', 'value', 'key'],
        'index': ['i', 'j', 'k'],
        'element': ['item', 'elem', 'element', 'val', '_'],
        'placeholder': ['_']
    }

    def __init__(self: Self, type: str='any') -> None:
        super().__init__()
        self.type = type

    
    def get_patterns(self: Self) -> list[str|Formula_Pattern]:
        return [
            'integer', 'string', 'float', 'boolean', 'container', 'misc', 'index', 'element', 'placeholder'
        ]

    def generate(self: Self) -> str:
        type_ = self.type if self.type != 'any' else super().generate()
        return R.choose_from(self.type_to_names[type_])
