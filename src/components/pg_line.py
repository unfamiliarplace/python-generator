from components.pg_decorator import PG_Decorator
from components.pg_real_world import PG_Real_World
from components.pg_mixin_featurized import PG_Mixin_Featurized
from components.pg_symbol_practice import PG_Symbol_Practice
from js_random import JS_Random as R
from components.pg_statement import PG_Statement
from components.pg_expression import PG_Expression
from typing import Self
from components.pg_mixin_generatable import PG_Mixin_Generatable
from components.pg_mixin_renderable import PG_Mixin_Renderable

class PG_Line(PG_Mixin_Generatable, PG_Mixin_Renderable, PG_Mixin_Featurized):

    patterns = {
        
    }

    option_to_class = {
        'statements': PG_Statement,
        'expressions': PG_Expression,
        'symbol_practice': PG_Symbol_Practice,
        'real_world': PG_Real_World,
        'decorators': PG_Decorator
    }

    def generate(self: Self) -> str:
        candidates = []

        for (option, cls) in self.option_to_class.items():
            if self.pg.on(option):
                candidate = cls()
                if isinstance(candidate, PG_Mixin_Featurized):
                    candidate.featurize(self.pg)

                candidate = str(candidate)
                candidates.append(candidate)

                # TODO What about """Comment"""?
                if self.pg.on('comments') and R.flip_coin(0.2) and cls is not PG_Symbol_Practice:
                    candidates.append('# ' + candidate)
        
        return R.choose_from(candidates)

    def __str__(self: Self) -> str:
        return self.generate()
