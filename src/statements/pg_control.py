from typing import Self
import pg


class Control(pg.Mixin_Generatable, pg.Mixin_Renderable):

    def get_patterns(self: Self) -> list[str|pg.FP]:
        return [
        # TODO for i in range(int)
        # TODO for i in range(len(container))

        pg.FP('for', pg.FN(pg.Variable, 'element'), 'in', pg.FN(pg.Container), reqs=pg.FR('containers'), suffix=':'),

        pg.FP('while', pg.FN(pg.Boolean), suffix=':'),
        pg.FP('break'),

        pg.FP('if', pg.FN(pg.Boolean), suffix=':'),
        pg.FP('elif', pg.FN(pg.Boolean), suffix=':'),
        pg.FP('else', suffix=':'),

        pg.FP('try', suffix=':'),
        pg.FP('except', suffix=':'),
        pg.FP('except', pg.FN(pg.Exception), suffix=':'),
    ]
