from typing import Self


class Function_Lambda(Mixin_Generatable, Mixin_Renderable):
    # TODO

    def generate(self: Self) -> Mixin_Renderable:
        return None
    
    def __str__(self: Self) -> str:
        return str(self.generate())
