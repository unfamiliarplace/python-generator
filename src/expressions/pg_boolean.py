from pg import *

class Boolean(Mixin_Generatable, Mixin_Renderable):
    pass

class Boolean_Operation(Mixin_Generatable, Mixin_Renderable_Operation):
    pass

class Boolean_Literal(Mixin_Generatable, Mixin_Renderable):
    pass

Boolean.patterns = [
    FP(FN(Boolean_Literal), weight=3),
    FP(FN(Boolean_Operation), weight=1),
    FP(FN(Function_Call, args=[True, 'boolean']), weight=1, reqs=FR('functions')),
    FP(FN(Variable, 'boolean'), weight=2, reqs=FR('booleans'))
]

Boolean_Operation.patterns = [
    FP(FN(Boolean), 'and', FN(Boolean), weight=3),
    FP(FN(Boolean), 'or', FN(Boolean), weight=3),
    FP('not', FN(Boolean), weight=2),

    FP(FN(Expression), '==', FN(Expression), weight=2),
    FP(FN(Expression), '>', FN(Expression), weight=2),
    FP(FN(Expression), '<', FN(Expression), weight=2),
    FP(FN(Expression), '<=', FN(Expression)),
    FP(FN(Expression), '>=', FN(Expression)),
    FP(FN(Expression), '!=', FN(Expression), weight=2),
    FP(FN(Expression), 'is', FN(Expression)),
    FP(FN(Expression), 'is not', FN(Expression)),
    FP(FN(Expression), 'in', FN(Container), weight=2),
    FP(FN(Expression), 'not in', FN(Container))
]

Boolean_Literal.patterns = [
    FP(FN('True'), weight=20),
    FP(FN('False'), weight=20),
    FP(FN(Boolean_Operation), weight=10),
    # TODO function bool(expression)
]
