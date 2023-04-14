import pg
from typing import Self

class Formula_Node():

    def __init__(self: Self, component_cls: type, args: list=[], kwargs: dict={}) -> None:
        self.component_cls = component_cls
        self.args = args
        self.kwargs = kwargs
    
    def evaluate(self: Self) -> pg.Mixin_Renderable:
        return self.component_cls(*self.args, **self.kwargs)
        
    def __str__(self: Self) -> str:
        return str(self.evaluate())
