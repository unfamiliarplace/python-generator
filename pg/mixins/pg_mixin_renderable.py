class Mixin_Renderable():

    def __str__(self) -> str:
        if hasattr(self, 'generate'):
            return str(self.generate())
        else:
            return ''

    def render(self) -> str:
        """Alias of str."""
        return str(self)
