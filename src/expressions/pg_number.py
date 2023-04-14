from pg import *

class Number(Mixin_Generatable, Mixin_Renderable):

    patterns = [
        FP(FN(Integer), weight=3),
        FP(FN(Float), weight=1)
    ]
