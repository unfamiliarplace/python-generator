import pg

class Number(pg.Mixin_Generatable, pg.Mixin_Renderable):

    patterns = [
        pg.FP(pg.FN(pg.Integer), weight=3),
        pg.FP(pg.FN(pg.Float), weight=1)
    ]
