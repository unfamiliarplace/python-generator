from js_random import JS_Random as R
from typing import Self
import pg

class Symbol_Practice(pg.Mixin_Generatable, pg.Mixin_Renderable):
    
    symbols = ["!", ":", ",", "()", "[]", "{}", "*", "<", ">", "==", "+", "-", "_", "#", "/", "\\", "//", ".", ";"]

    def generate(self: Self) -> str:
        return R.choose_from(self.symbols)
    
    def __str__(self: Self) -> str:
        return self.generate()
