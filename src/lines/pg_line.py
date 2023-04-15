from js_random import JS_Random as R
from typing import Self
import pg

class Line(pg.Mixin_Generatable, pg.Mixin_Renderable):

    def get_patterns(self: Self) -> list[str|pg.FP]:
        return [
            pg.FP(pg.FN(pg.Statement), reqs=pg.FR('statements'), weight=4),
            pg.FP(pg.FN(pg.Expression), reqs=pg.FR('expressions'), weight=5),
            pg.FP(pg.FN(pg.Symbol_Practice), reqs=pg.FR('symbol_practice'), weight=1),
            pg.FP(pg.FN(pg.Real_World), reqs=pg.FR('real_world'), weight=3),
            pg.FP(pg.FN(pg.Decorator), reqs=pg.FR('decorators'), weight=1),
        ]

    def __str__(self: Self) -> str:
        pattern = self.generate()
        s = str(pattern)
        if pg.PythonGenerator().on('comments') and R.flip_coin(0.2):
            if not pattern.uses(pg.Symbol_Practice, pg.Real_World):
                s = '# ' + s
        return s
