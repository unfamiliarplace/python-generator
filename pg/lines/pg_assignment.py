
import pg

class Assignment(pg.Mixin_Generatable, pg.Mixin_Renderable):

    def get_patterns(self) -> list[str|pg.FP]:
        return [
            # TODO variables should be matched with expressions of matching type
            pg.FP(pg.FN(pg.Variable), '=', pg.FN(pg.Expression), weight=10),

            pg.FP(pg.FN(pg.Number), '+=', pg.FN(pg.Number), weight=5),
            pg.FP(pg.FN(pg.String), '+=', pg.FN(pg.String), weight=2),

            pg.FP(pg.FN(pg.Number), '-=', pg.FN(pg.Number), weight=4),

            pg.FP(pg.FN(pg.Number), '*=', pg.FN(pg.Number), weight=3),
            pg.FP(pg.FN(pg.String), '*=', pg.FN(pg.Integer), weight=1),
            pg.FP(pg.FN(pg.Integer), '*=', pg.FN(pg.String), weight=1),

            pg.FP(pg.FN(pg.Number), '/=', pg.FN(pg.Number), weight=2),
            pg.FP(pg.FN(pg.Number), '//=', pg.FN(pg.Number), weight=2),
            pg.FP(pg.FN(pg.Number), '**=', pg.FN(pg.Number), weight=1),
        ]
