from mixins.pg_mixin_renderable import Mixin_Renderable

class Mixin_Renderable_Operation(Mixin_Renderable):

    def __str__(self) -> str:
        return f'({super().__str__()})'

    def render(self) -> str:
        """Alias of str."""
        return str(self)
