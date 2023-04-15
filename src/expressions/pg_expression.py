import pg
from typing import Self

class Expression(pg.Mixin_Generatable, pg.Mixin_Renderable):

    # TODO there might be more

    def get_patterns(self: Self) -> list[str|pg.FP]:
        return [
            pg.FP(pg.FN(pg.String), reqs=pg.FR('strings'), weight=3),
            pg.FP(pg.FN(pg.Number), reqs=pg.FR('math'), weight=3),
            pg.FP(pg.FN(pg.Boolean), reqs=pg.FR('booleans'), weight=2),
            pg.FP(pg.FN(pg.Container), reqs=pg.FR('containers'), weight=2),
            pg.FP(pg.FN(pg.Function_Call, True), reqs=pg.FR('functions'), weight=2),
            pg.FP(pg.FN(pg.Variable), reqs=pg.FR('variables'),weight=1)
        ]
