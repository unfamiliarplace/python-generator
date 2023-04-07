from typing import Iterable, Self
from js_random import JS_Random as R

class PG_Container():

    def __init__(self: Self, types: str='any') -> None:
        self.types = types

    def generate(self: Self) -> Iterable:
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
