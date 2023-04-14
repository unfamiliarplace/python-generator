import pg

class Boolean(pg.Mixin_Generatable, pg.Mixin_Renderable):
    pass

class Boolean_Operation(pg.Mixin_Generatable, pg.Mixin_Renderable_Operation):
    pass

class Boolean_Literal(pg.Mixin_Generatable, pg.Mixin_Renderable):
    pass

Boolean.patterns = [
    pg.FP(pg.FN(Boolean_Literal), weight=3),
    pg.FP(pg.FN(Boolean_Operation), weight=1),
    pg.FP(pg.FN(pg.Function_Call, args=[True, 'boolean']), weight=1, reqs=pg.FR('functions')),
    pg.FP(pg.FN(pg.Variable, 'boolean'), weight=2, reqs=pg.FR('booleans'))
]

Boolean_Operation.patterns = [
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

Boolean_Literal.patterns = [
    pg.FP(pg.FN('True'), weight=20),
    pg.FP(pg.FN('False'), weight=20),
    pg.FP(pg.FN(Boolean_Operation), weight=10),
    # TODO function bool(expression)
]
