from pg import *

class Assignment(Mixin_Generatable, Mixin_Renderable):

    patterns = [
        FP(FN(Variable), '=', FN(Expression), weight=10),

        FP(FN(Number), '+=', FN(Number), weight=5),
        FP(FN(String), '+=', FN(String), weight=2),

        FP(FN(Number), '-=', FN(Number), weight=4),

        FP(FN(Number), '*=', FN(Number), weight=3),
        FP(FN(String), '*=', FN(Integer), weight=1),
        FP(FN(Integer), '*=', FN(String), weight=1),

        FP(FN(Number), '/=', FN(Number), weight=2),
        FP(FN(Number), '//=', FN(Number), weight=2),
        FP(FN(Number), '**=', FN(Number), weight=1),
    ]
