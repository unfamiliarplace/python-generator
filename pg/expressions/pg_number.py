
from typing import Self
import pg

class Number(pg.Mixin_Generatable, pg.Mixin_Renderable):

    def get_patterns(self: Self) -> list[str|pg.FP]:
        return [
            pg.FP(pg.FN(pg.Integer), weight=3),
            pg.FP(pg.FN(pg.Float), weight=1)
        ]
