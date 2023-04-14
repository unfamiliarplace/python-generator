import pg

class Statement(pg.Mixin_Generatable, pg.Mixin_Renderable):

    patterns = [
        pg.FP('pass', weight=1),
        pg.FP(pg.FN(pg.Control), reqs=pg.FR('control'), weight=4),
        pg.FP('return', pg.FN(pg.Expression), reqs=pg.FR('functions'), weight=1),
        pg.FP(pg.FN(pg.Assignment), reqs=pg.FR('variables'), weight=3),
        pg.FP(pg.FN(pg.Import), reqs=pg.FR('imports'), weight=2),
    ]
