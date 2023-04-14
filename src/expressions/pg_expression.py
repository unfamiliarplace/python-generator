from pg import *

class Expression(Mixin_Generatable, Mixin_Renderable):

    # TODO there might be more

    patterns = [
        FP(FN(String), reqs=FR('strings'), weight=3),
        FP(FN(Number), reqs=FR('math'), weight=3),
        FP(FN(Boolean), reqs=FR('booleans'), weight=2),
        FP(FN(Container), reqs=FR('containers'), weight=2),
        FP(FN(Function_Call, True), reqs=FR('functions'), weight=2),
        FP(FN(Variable, 'placeholder'), reqs=FR('variables'),weight=1)
    ]
