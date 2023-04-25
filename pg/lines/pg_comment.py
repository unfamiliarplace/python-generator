
from js_random import JS_Random as R
from data.comments.comment_lines import COMMENT_LINES
from expressions.pg_expression import Expression

from formula.pg_formula_node import FN
from formula.pg_formula_pattern import FP
from formula.pg_formula_requirement import FR
from lines.pg_decorator import Decorator
from mixins.pg_mixin_generatable import Mixin_Generatable
from mixins.pg_mixin_renderable import Mixin_Renderable
from statements.pg_statement import Statement

class Comment(Mixin_Generatable, Mixin_Renderable):

    postfixes = [
        # TODO lol
        'TODO',
        'Not sure what this does',
        'Yes this does work',
        'foobar',
    ]

    def get_patterns(self) -> list[str|FP]:
        return [
            FP(FN(Statement), reqs=FR('statements'), weight=4),
            FP(FN(Expression), reqs=FR('expressions'), weight=5),
            FP(FN(Decorator), reqs=FR('decorators'), weight=1),
        ]
    
    def generate(self) -> str:
        if R.flip_coin(0.4):
            return self._generate_type_1()
        elif R.flip_coin(0.8):
            return self._generate_type_2()
        else:
            return self._generate_type_3()

    def _generate_type_1(self) -> str:
        """# line of code"""
        line = str(super().generate())
        return '# ' + line

    def _generate_type_2(self) -> str:
        """# English comment"""

        if R.flip_coin(0.001):
            return '# TODO'
        else:
            return R.choose_from(COMMENT_LINES)

    def _generate_type_3(self) -> str:
        """line of code # English comment"""
        line = super().generate()
        return f'{line} # {R.choose_from[self.postfixes]}'
