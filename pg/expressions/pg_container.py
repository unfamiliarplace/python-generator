from js_random import JS_Random as R

from mixins.pg_mixin_generatable import Mixin_Generatable
from mixins.pg_mixin_renderable import Mixin_Renderable


class Container(Mixin_Generatable, Mixin_Renderable):

    def __init__(self, types: str='any') -> None:
        self.types = types
        super().__init__()

    def generate(self) -> str:
        # TODO
        values = [1, 2, 3]
        return str(values)[1:-1]
    
    def __str__(self) -> str:
        s = ', '.join(self.generate())

        if R.flip_coin(.33):
            return f'[{s}]'
        
        elif R.flip_coin(.5):
            return f'({s})'
        
        else:
            return  "{" + s + "}" # Transcrypt can't handle f'{{{}}}'
