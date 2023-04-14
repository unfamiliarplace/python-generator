from typing import Self
import pg

class Function_Definition(pg.Mixin_Generatable, pg.Mixin_Renderable):
    # TODO

    def generate(self: Self) -> pg.Mixin_Renderable:
        return None
    
    def __str__(self: Self) -> str:
        return str(self.generate())
