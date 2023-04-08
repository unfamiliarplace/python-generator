from js_random import JS_Random as R
from typing import Self
from components.pg_mixin_generatable import PG_Mixin_Generatable
from components.pg_mixin_renderable import PG_Mixin_Renderable

class PG_Decorator(PG_Mixin_Generatable, PG_Mixin_Renderable):

    decorators = ['lru_cache', 'jit', 'count_calls', 'dataclass', 'singleton', 'use_unit', 'staticmethod', 'singledispatch', 'register']

    def generate(self: Self) -> str:
        return R.choose_from(self.decorators)
    
    def __str__(self: Self) -> str:
        return f'@{self.generate()}'
