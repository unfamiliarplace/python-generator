
from formula.pg_formula_pattern import FP
from mixins.pg_mixin_generatable import Mixin_Generatable
from mixins.pg_mixin_renderable import Mixin_Renderable

class Exception(Mixin_Generatable, Mixin_Renderable):

    def get_patterns(self) -> list[str|FP]:
        return [
            'ValueError',
            'TypeError',
            'ZeroDivisionError',
            'NotImplementedError',
            'SyntaxError',
            'NameError',
            'AssertionError',
            'EOFError',
            'IndexError',
            'KeyError',
            'ImportError',
            'KeyboardInterrupt',
        ]
