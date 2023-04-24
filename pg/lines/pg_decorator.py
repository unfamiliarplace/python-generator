import pg


class Decorator(pg.Mixin_Generatable, pg.Mixin_Renderable):

    def get_patterns(self) -> list[str|pg.FP]:
        return [
        'lru_cache', 'jit', 'count_calls', 'dataclass', 'singleton', 'use_unit', 'staticmethod', 'singledispatch', 'register'
    ]

    def __str__(self) -> str:
        return f'@{self.generate()}'
