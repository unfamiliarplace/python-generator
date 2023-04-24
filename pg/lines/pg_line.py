import pg

class Line(pg.Mixin_Generatable, pg.Mixin_Renderable):

    def get_patterns(self) -> list[str|pg.FP]:
        return [
            pg.FP(pg.FN(pg.Statement), reqs=pg.FR('statements'), weight=4),
            pg.FP(pg.FN(pg.Expression), reqs=pg.FR('expressions'), weight=5),
            pg.FP(pg.FN(pg.Symbol_Practice), reqs=pg.FR('symbol_practice'), weight=1),
            pg.FP(pg.FN(pg.Real_World), reqs=pg.FR('real_world'), weight=3),
            pg.FP(pg.FN(pg.Decorator), reqs=pg.FR('decorators'), weight=1),
            pg.FP(pg.FN(pg.Comment), reqs=pg.FR('comments'), weight=2),
        ]
