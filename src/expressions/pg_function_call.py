from typing import Self
import pg

class Function_Call(pg.Mixin_Generatable, pg.Mixin_Renderable):
    
    def __init__(self: Self, returns: bool=None, args: list[str]=[], kwargs: dict[str, str]={}) -> None:
        super().__init__()
        self.returns = returns
        self.args = args
        self.kwargs = kwargs

    def get_patterns(self: Self) -> list[str|pg.FP]:
        return [
            'do_nothing()'
        ]
