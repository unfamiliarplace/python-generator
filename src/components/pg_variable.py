from typing import Self
from js_random import JS_Random as R

class PG_Variable():

    type_to_names = {
        'number': ['n', 'n_students', 'n_doughnuts'],
        'string': ['name', 'person', 'winner'],
        'float': ['fraction', 'proportion'],
        'container': ['names', 'ages', 'people', 'pizzas', 'values'],
        'misc': ['x', 'y', 'z', 'a', 'b', 'c']
    }

    def __init__(self: Self, type: str='any', plural: bool=False) -> None:
        self.type = type

    def generate(self: Self) -> str:
        candidates = []
        if self.type == 'any':
            for v in self.type_to_names.values():
                candidates.extend(v)
        else:
            candidates = self.type_to_names[self.type]
        
        return R.choose_from(candidates)
    
    def __str__(self: Self) -> str:
        return self.generate()
