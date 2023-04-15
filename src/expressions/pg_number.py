
from typing import Self

class Number(Mixin_Generatable, Mixin_Renderable):

    def get_patterns(self: Self) -> list[str|Formula_Pattern]:
        return [
            FP(FN(Integer), weight=3),
            FP(FN(Float), weight=1)
        ]
