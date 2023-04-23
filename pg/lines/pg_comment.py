
from typing import Self
import pg
from js_random import JS_Random as R

class Comment(pg.Mixin_Generatable, pg.Mixin_Renderable):

    postfixes = [
        # TODO lol
        'TODO',
        'Not sure what this does',
        'Yes this does work',
        'foobar',
    ]

    def get_patterns(self: Self) -> list[str|pg.FP]:
        return [
            pg.FP(pg.FN(pg.Statement), reqs=pg.FR('statements'), weight=4),
            pg.FP(pg.FN(pg.Expression), reqs=pg.FR('expressions'), weight=5),
            pg.FP(pg.FN(pg.Decorator), reqs=pg.FR('decorators'), weight=1),
        ]
    
    def generate(self: Self) -> str:
        if R.flip_coin(0.4):
            return self._generate_type_1()
        elif R.flip_coin(0.8):
            return self._generate_type_2()
        else:
            return self._generate_type_3()

    def _generate_type_1(self: Self) -> str:
        """# line of code"""
        line = super().generate()
        return '# ' + line

    def _generate_type_2(self: Self) -> str:
        """# English comment"""

        if R.flip_coin(0.001):
            return '# TODO'
        else:
            with open('data/comments/comments.txt', 'r', encoding='utf-8') as f:          
                return R.choose_from(list(f.readlines())).strip()

    def _generate_type_3(self: Self) -> str:
        """line of code # English comment"""
        line = super().generate()
        return f'{line} # {R.choose_from[self.postfixes]}'
