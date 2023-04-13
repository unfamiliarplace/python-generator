from typing import Self
from components.pg_formula_pattern import PG_Formula_Pattern
from components.pg_mixin_renderable import PG_Mixin_Renderable
from js_random import JS_Random as R

class PG_Mixin_Generatable():

    patterns = []

    def possible(self: Self) -> list[PG_Formula_Pattern]:
        return list(filter(lambda p: p.possible(), self.patterns))

    def generate(self: Self) -> PG_Formula_Pattern:
        candidates = []

        for pattern in self.possible():
            for _ in range(pattern.weight):
                candidates.append(pattern)

        return R.choose_from(candidates)
