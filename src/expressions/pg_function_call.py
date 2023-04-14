from typing import Self
from pg import *

class Function_Call(Mixin_Generatable, Mixin_Renderable):

    # TODO
    patterns = ['do_nothing()']
    
    def __init__(self: Self, returns: bool=None, args: list[str]=[], kwargs: dict[str, str]={}) -> None:
        self.returns = returns
        self.args = args
        self.kwargs = kwargs
