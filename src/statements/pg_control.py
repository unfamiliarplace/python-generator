import pg

class Control(pg.Mixin_Generatable, pg.Mixin_Renderable):

    patterns = [
        # TODO for i in range(int)
        # TODO for i in range(len(container))

        pg.FP('for', pg.FN(pg.Variable, 'element'), 'in', pg.FN(pg.Container), reqs=pg.FR('containers')),

        # TODO instead, have container have a variable of type container as a pattern
        # pg.FP('for', pg.FN(pg.Variable, 'element'), 'in', pg.FN(pg.Variable, 'container'), reqs=pg.FR('containers')),

        pg.FP('while', pg.FN(pg.Boolean)),
        pg.FP('if', pg.FN(pg.Boolean)),

        pg.FP('break')
    ]
