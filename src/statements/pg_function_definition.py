from typing import Self
from pg import *

class Function_Definition(Mixin_Generatable, Mixin_Renderable):
    # TODO

    def generate(self: Self) -> Mixin_Renderable:
        return None
    
    def __str__(self: Self) -> str:
        return str(self.generate())
