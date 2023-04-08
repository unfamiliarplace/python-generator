from js_random import JS_Random as R
from typing import Self
from components.pg_mixin_generatable import PG_Mixin_Generatable
from components.pg_mixin_renderable import PG_Mixin_Renderable

class PG_Symbol_Practice(PG_Mixin_Generatable, PG_Mixin_Renderable):
    
    symbols = ["!", ":", ",", "()", "[]", "{}", "*", "<", ">", "==", "+", "-", "_", "#", "/", "\\", "//", ".", ";"]

    def generate(self: Self) -> str:
        return R.choose_from(self.symbols)
    
    def __str__(self: Self) -> str:
        return self.generate()
