from js_random import JS_Random as R
import pg

class Container(pg.Mixin_Generatable, pg.Mixin_Renderable):

    def __init__(self, types: str='any') -> None:
        self.types = types

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
