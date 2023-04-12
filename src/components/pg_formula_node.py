from components.pg_mixin_renderable import PG_Mixin_Renderable
from pg import *
from components.pg_sequence import PG_Sequence
from typing import Self

# Oh my GOODNESS this is GODAWFUL there must be a better way
import importlib

class PG_Formula_Node():

    req_checkers = {
        REQ_NONE: PythonGenerator.none,
        REQ_ANY: PythonGenerator.any,
        REQ_ALL: PythonGenerator.all,
    }

    def __init__(self: Self, component: str, reqs: list[str]=[], req_mode: int=REQ_NONE, weight: int=1, args: list=[], kwargs: dict={}) -> None:
        self.component = component
        self.reqs = reqs
        self.req_mode = req_mode
        self.weight = weight
        self.args = args
        self.kwargs = kwargs

    def get_class(self: Self) -> type:
        module_name = f'components.{self.component.lower()}'
        module = importlib.import_module(module_name)
        return getattr(module, self.component)
    
    def evaluate(self: Self) -> None|PG_Mixin_Renderable:
        if not self.req_checkers[self.req_mode](*self.reqs):
            return None
        
        else: 
            return self.get_class()(*self.args, **self.kwargs)
        
    def render(self: Self) -> str:
        node = self.evaluate()
        if node is not None:
            return node.render()
        else:
            # TODO
            return ''
