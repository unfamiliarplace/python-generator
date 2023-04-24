
import pg

class Exception(pg.Mixin_Generatable, pg.Mixin_Renderable):

    def get_patterns(self) -> list[str|pg.FP]:
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
