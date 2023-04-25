from js_random import JS_Random as R

from formula.pg_formula_pattern import FP
from mixins.pg_mixin_generatable import Mixin_Generatable
from mixins.pg_mixin_renderable import Mixin_Renderable

class Variable(Mixin_Generatable, Mixin_Renderable):

    type_to_names = {
        'integer': ['n', 'm', 'n_students', 'n_doughnuts', 'count', 'total'],
        'string': ['name', 'person', 'winner'],
        'float': ['fraction', 'proportion'],
        'boolean': ['is_valid', 'is_allowed', 'is_done', 'has_finished', 'has_loaded', 'exists'],
        'container': ['names', 'ages', 'people', 'pizzas', 'values'],
        'misc': ['x', 'y', 'z', 'a', 'b', 'c', 'value', 'key'],
        'index': ['i', 'j', 'k'],
        'element': ['item', 'elem', 'element', 'val', '_'],
        'placeholder': ['_'],
        'special': ['__name__', '__main__']
    }

    def __init__(self, type: str='any') -> None:
        self.type = type
        super().__init__()
    
    def get_patterns(self) -> list[str|FP]:
        return [
            'integer', 'string', 'float', 'boolean', 'container', 'misc', 'index', 'element', 'placeholder'
        ]

    def generate(self) -> str:
        type_ = self.type if self.type != 'any' else super().generate()
        name = R.choose_from(self.type_to_names[type_])

        # Constant?
        if R.flip_coin(0.1):
            return name.upper()
        else:
            return name
