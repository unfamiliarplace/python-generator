import pg

class None_Node(pg.Mixin_Generatable, pg.Mixin_Renderable):
    def get_patterns(self) -> list[str|pg.FP]:
        return [
            pg.FP('None', weight=3),
            pg.FP(pg.FN(pg.Function_Call, args=[pg.RT.NONE]), weight=1, reqs=pg.FR('functions')),
        ]
