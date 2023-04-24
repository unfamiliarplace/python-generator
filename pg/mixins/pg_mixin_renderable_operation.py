import pg

class Mixin_Renderable_Operation(pg.Mixin_Renderable):

    def __str__(self) -> str:
        return f'({super().__str__()})'

    def render(self) -> str:
        """Alias of str."""
        return str(self)
