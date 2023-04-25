from formula.pg_formula_pattern import FP
from mixins.pg_mixin_generatable import Mixin_Generatable
from mixins.pg_mixin_renderable import Mixin_Renderable

class Symbol_Practice(Mixin_Generatable, Mixin_Renderable):
    
    def get_patterns(self) -> list[str|FP]:
        return [
            "!", ":", ",", "()", "[]", "{}", "*", "<", ">", "==", "+", "-", "_", "#", "/", "\\", "//", ".", ";"
        ]
