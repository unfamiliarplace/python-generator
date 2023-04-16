from typing import Self
from enum import Enum
import pg

class Return_Type(Enum):
    ANY = 0
    NONE = 1
    BOOL = 2
    STR = 3
    INT = 4
    FLOAT = 5
    CONTAINER = 6

class Function_Call(pg.Mixin_Generatable, pg.Mixin_Renderable):
    
    def __init__(self: Self, return_type: Return_Type=Return_Type.ANY, args: list[str]=[], kwargs: dict[str, str]={}) -> None:
        super().__init__()
        self.return_type = return_type
        self.args = args
        self.kwargs = kwargs

    def get_patterns(self: Self) -> list[str|pg.FP]:
        return [
            'do_nothing()'
        ]
