from components.pg_mixin_renderable import PG_Mixin_Renderable
from typing import Self

# Oh my GOODNESS this is GODAWFUL there must be a better way
import importlib

class PG_Formula_Node():

    def __init__(self: Self, component_name: str, args: list=[], kwargs: dict={}) -> None:
        self.component_name = component_name
        self.args = args
        self.kwargs = kwargs

    def get_class(self: Self) -> type:
        module_name = f'components.{self.component_name.lower()}'
        module = importlib.import_module(module_name)
        return getattr(module, self.component_name)
    
    def evaluate(self: Self) -> PG_Mixin_Renderable:
        return self.get_class()(*self.args, **self.kwargs)
        
    def __str__(self: Self) -> str:
        return str(self.evaluate())

# Shorthand...
FN = PG_Formula_Node
