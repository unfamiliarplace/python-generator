import pg

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

class Function_Call(pg.Mixin_Generatable, pg.Mixin_Renderable):
    
    def __init__(self, return_type: int=RT.ANY, args: list[str]=[], kwargs: dict[str, str]={}) -> None:
        super().__init__()
        self.return_type = return_type
        self.args = args
        self.kwargs = kwargs

    def get_patterns(self) -> list[str|pg.FP]:
        return [
            'do_nothing()'
        ]
