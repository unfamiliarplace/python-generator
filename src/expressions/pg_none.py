from typing import Self
import pg

class None_Node(pg.Mixin_Generatable, pg.Mixin_Renderable):
    def get_patterns(self: Self) -> list[str|pg.FP]:
        return [
            pg.FP('None', weight=3),
            pg.FP(pg.FN(pg.Function_Call, args=[pg.Return_Type.NONE]), weight=1, reqs=pg.FR('functions')),
        ]
