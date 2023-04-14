from typing import Self
from js_random import JS_Random as R
from pg import *

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
        self.type = type

    def generate(self: Self) -> str:
        type_ = self.type if self.type != 'any' else super().generate()
        return R.choose_from(self.type_to_names[type_])
