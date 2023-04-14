from pg import *

class Statement(Mixin_Generatable, Mixin_Renderable):

    patterns = [
        FP('pass', weight=1),
        FP(FN(Control), reqs=FR('control'), weight=4),
        FP('return', FN(Expression), reqs=FR('functions'), weight=1),
        FP(FN(Assignment), reqs=FR('variables'), weight=3),
        FP(FN(Import), reqs=FR('imports'), weight=2),
    ]
