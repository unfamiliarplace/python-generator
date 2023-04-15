from typing import Self
import pg


class Control(pg.Mixin_Generatable, pg.Mixin_Renderable):

    def get_patterns(self: Self) -> list[str|pg.FP]:
        return [
        # TODO for i in range(int)
        # TODO for i in range(len(container))

        pg.FP('for', pg.FN(pg.Variable, 'element'), 'in', pg.FN(pg.Container), reqs=pg.FR('containers')),

        # TODO instead, have container have a variable of type container as a pattern
        # pg.FP('for', pg.FN(Variable, 'element'), 'in', pg.FN(Variable, 'container'), reqs=pg.FR('containers')),

        pg.FP('while', pg.FN(pg.Boolean)),
        pg.FP('break'),

        pg.FP('if', pg.FN(pg.Boolean)),
        pg.FP('elif', pg.FN(pg.Boolean)),
        pg.FP('else'),

        pg.FP('try'),
        pg.FP('except'),
        pg.FP('except', pg.FN(pg.Exception)),
        
        pg.FP('assert', pg.FN(pg.Boolean)),
    ]
