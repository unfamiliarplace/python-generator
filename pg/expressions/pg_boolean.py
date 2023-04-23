from typing import Self
import pg

class Boolean(pg.Mixin_Generatable, pg.Mixin_Renderable):
    def get_patterns(self: Self) -> list[str|pg.FP]:
        return [
            pg.FP(pg.FN(Boolean_Literal), weight=3),
            pg.FP(pg.FN(Boolean_Operation), weight=1),
            pg.FP(pg.FN(pg.Function_Call, args=[pg.RT.BOOL]), weight=1, reqs=pg.FR('functions')),
            pg.FP(pg.FN(pg.Variable, 'boolean'), weight=2, reqs=pg.FR('booleans')),
            # TODO function bool(expression) ?
        ]

class Boolean_Operation(pg.Mixin_Generatable, pg.Mixin_Renderable_Operation):
    def get_patterns(self: Self) -> list[str|pg.FP]:
        return [
            pg.FP(pg.FN(Boolean), 'and', pg.FN(Boolean), weight=3),
            pg.FP(pg.FN(Boolean), 'or', pg.FN(Boolean), weight=3),
            pg.FP('not', pg.FN(Boolean), weight=2),

            pg.FP(pg.FN(pg.Expression), '==', pg.FN(pg.Expression), weight=2),
            pg.FP(pg.FN(pg.Expression), '>', pg.FN(pg.Expression), weight=2),
            pg.FP(pg.FN(pg.Expression), '<', pg.FN(pg.Expression), weight=2),
            pg.FP(pg.FN(pg.Expression), '<=', pg.FN(pg.Expression)),
            pg.FP(pg.FN(pg.Expression), '>=', pg.FN(pg.Expression)),
            pg.FP(pg.FN(pg.Expression), '!=', pg.FN(pg.Expression), weight=2),
            pg.FP(pg.FN(pg.Expression), 'is', pg.FN(pg.Expression)),
            pg.FP(pg.FN(pg.Expression), 'is not', pg.FN(pg.Expression)),
            pg.FP(pg.FN(pg.Expression), 'in', pg.FN(pg.Container), weight=2),
            pg.FP(pg.FN(pg.Expression), 'not in', pg.FN(pg.Container))
        ]

class Boolean_Literal(pg.Mixin_Generatable, pg.Mixin_Renderable):
    def get_patterns(self: Self) -> list[str|pg.FP]:
        return [
            pg.FP('True'),
            pg.FP('False'),
        ]
