from typing import Self
from components.pg_mixin_generatable import PG_Mixin_Generatable
from components.pg_mixin_renderable import PG_Mixin_Renderable

class PG_Function_Call(PG_Mixin_Generatable, PG_Mixin_Renderable):

    # TODO
    patterns = ['do_nothing()']
    
    def __init__(self: Self, returns: bool=None, args: list[str]=[], kwargs: dict[str, str]={}) -> None:
        self.returns = returns
        self.args = args
        self.kwargs = kwargs
