from formula.pg_formula_pattern import Formula_Pattern
from js_random import JS_Random as R
from typing import Self
from mixins.pg_mixin_generatable import Mixin_Generatable
from mixins.pg_mixin_renderable import Mixin_Renderable


class Symbol_Practice(Mixin_Generatable, Mixin_Renderable):
    
    def get_patterns(self: Self) -> list[str|Formula_Pattern]:
        return [
            "!", ":", ",", "()", "[]", "{}", "*", "<", ">", "==", "+", "-", "_", "#", "/", "\\", "//", ".", ";"
        ]
