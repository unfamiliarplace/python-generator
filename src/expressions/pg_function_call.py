from typing import Self
from formula.pg_formula_pattern import Formula_Pattern
from mixins.pg_mixin_generatable import Mixin_Generatable
from mixins.pg_mixin_renderable import Mixin_Renderable


class Function_Call(Mixin_Generatable, Mixin_Renderable):
    
    def __init__(self: Self, returns: bool=None, args: list[str]=[], kwargs: dict[str, str]={}) -> None:
        super().__init__()
        self.returns = returns
        self.args = args
        self.kwargs = kwargs

    def get_patterns(self: Self) -> list[str|Formula_Pattern]:
        return [
            'do_nothing()'
        ]
