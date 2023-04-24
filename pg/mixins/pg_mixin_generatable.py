import pg

from js_random import JS_Random as R

class Mixin_Generatable():

    def __init__(self) -> None:
        self.set_patterns()

    def get_patterns(self) -> list[str|pg.FP]:
        # Override
        return []

    def set_patterns(self) -> None:
        self.patterns = self.get_patterns()

    def possible(self) -> list[str|pg.FP]:
        return list(filter(lambda p: (type(p) is str) or p.possible(), self.patterns))
    
    def weighted_candidates(self) -> list[str|pg.FP]:
        candidates = []

        for pattern in self.possible():
            weight = 1 if type(pattern) is str else pattern.weight
            for _ in range(weight):
                candidates.append(pattern)
        
        return candidates

    def generate(self) -> pg.FP:
        candidates = self.weighted_candidates()
        return R.choose_from(candidates)
