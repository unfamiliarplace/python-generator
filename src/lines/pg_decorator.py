from typing import Self
from formula.pg_formula_pattern import Formula_Pattern
from mixins.pg_mixin_generatable import Mixin_Generatable
from mixins.pg_mixin_renderable import Mixin_Renderable


class Decorator(Mixin_Generatable, Mixin_Renderable):

    def get_patterns(self: Self) -> list[str|Formula_Pattern]:
        return [
        'lru_cache', 'jit', 'count_calls', 'dataclass', 'singleton', 'use_unit', 'staticmethod', 'singledispatch', 'register'
    ]

    def __str__(self: Self) -> str:
        return f'@{self.generate()}'
