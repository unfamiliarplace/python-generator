import pg


class Sequence(pg.Mixin_Renderable):

    def __init__(self, *components: object) -> None:
        self.components = components

    def __str__(self) -> str:
        return ' '.join(f'{c}' for c in self.components)
