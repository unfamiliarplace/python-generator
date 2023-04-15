from typing import Self
from formula.pg_formula_pattern import Formula_Pattern

from js_random import JS_Random as R

class Mixin_Generatable():

    def __init__(self: Self) -> None:
        self.set_patterns()

    def get_patterns(self: Self) -> list[str|Formula_Pattern]:
        # Override
        return []

    def set_patterns(self: Self) -> None:
        self.patterns = self.get_patterns()

    def possible(self: Self) -> list[str|Formula_Pattern]:
        return list(filter(lambda p: (type(p) is str) or p.possible(), self.patterns))

    def generate(self: Self) -> Formula_Pattern:
        candidates = []

        for pattern in self.possible():
            weight = 1 if type(pattern) is str else pattern.weight
            for _ in range(weight):
                candidates.append(pattern)

        return R.choose_from(candidates)
