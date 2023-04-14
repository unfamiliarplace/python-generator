from typing import Self
from pg import *

class Decorator(Mixin_Generatable, Mixin_Renderable):
    patterns = [
        'lru_cache', 'jit', 'count_calls', 'dataclass', 'singleton', 'use_unit', 'staticmethod', 'singledispatch', 'register'
    ]

    def __str__(self: Self) -> str:
        return f'@{self.generate()}'
