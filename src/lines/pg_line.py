from js_random import JS_Random as R
from typing import Self
from pg import *

class Line(Mixin_Generatable, Mixin_Renderable):

    patterns = [
        FP(FN(Statement), reqs=FR('statements'), weight=4),
        FP(FN(Expression), reqs=FR('expressions'), weight=5),
        FP(FN(Symbol_Practice), reqs=FR('symbol_practice'), weight=1),
        FP(FN(Real_World), reqs=FR('real_world'), weight=3),
        FP(FN(Decorator), reqs=FR('decorators'), weight=1),
    ]

    def __str__(self: Self) -> str:
        pattern = self.generate()
        s = str(pattern)
        if PythonGenerator().on('comments') and R.flip_coin(0.2) and not pattern.uses(Symbol_Practice):
            s = '# ' + s
        return s
