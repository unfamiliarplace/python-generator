from typing import Iterable, Self
from js_random import JS_Random as R
from components.pg_mixin_generatable import PG_Mixin_Generatable
from components.pg_mixin_renderable import PG_Mixin_Renderable

class PG_Container(PG_Mixin_Generatable, PG_Mixin_Renderable):

    def __init__(self: Self, types: str='any') -> None:
        self.types = types

    def generate(self: Self) -> Iterable:
        # TODO
        values = []
        return values
    
    def __str__(self: Self) -> str:
        s = ', '.join(self.generate())

        if R.flip_coin(.33):
            return f'[{s}]'
        
        elif R.flip_coin(.5):
            return f'({s})'
        
        else:
            return f'{{{s}}}'
