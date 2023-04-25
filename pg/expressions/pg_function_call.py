from formula.pg_formula_pattern import FP
from mixins.pg_mixin_generatable import Mixin_Generatable
from mixins.pg_mixin_renderable import Mixin_Renderable

# Return types
class Return_Type():
    ANY = 0
    NONE = 1
    BOOL = 2
    STR = 3
    INT = 4
    FLOAT = 5
    CONTAINER = 6

RT = Return_Type

class Function_Call(Mixin_Generatable, Mixin_Renderable):
    
    def __init__(self, return_type: int=RT.ANY, args: list[str]=[], kwargs: dict[str, str]={}) -> None:
        self.return_type = return_type
        self.args = args
        self.kwargs = kwargs
        super().__init__()

    def get_patterns(self) -> list[str|FP]:
        return [
            'do_nothing()'
        ]
