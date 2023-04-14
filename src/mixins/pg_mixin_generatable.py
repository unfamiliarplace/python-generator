from typing import Self
import pg
from js_random import JS_Random as R

class Mixin_Generatable():

    patterns = []

    def possible(self: Self) -> list[pg.Formula_Pattern]:
        return list(filter(lambda p: (type(p) is str) or p.possible(), self.patterns))

    def generate(self: Self) -> pg.Formula_Pattern:
        candidates = []

        for pattern in self.possible():
            weight = 1 if type(pattern) is str else pattern.weight
            for _ in range(weight):
                candidates.append(pattern)

        return R.choose_from(candidates)
