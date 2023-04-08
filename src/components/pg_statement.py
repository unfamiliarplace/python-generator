from components.pg_assignment import PG_Assignment
from js_random import JS_Random as R
from components.pg_control import PG_Control
from components.pg_return import PG_Return
from components.pg_mixin_featurized import PG_Mixin_Featurized
from components.pg_mixin_generatable import PG_Mixin_Generatable
from components.pg_mixin_renderable import PG_Mixin_Renderable
from typing import Self

class PG_Statement(PG_Mixin_Generatable, PG_Mixin_Renderable, PG_Mixin_Featurized):

    def generate(self: Self) -> object:
        candidates = []

        # TODO return only with functions? (like def will have to be)
        candidates.append(PG_Return().featurize(self.pg))
        candidates.append(PG_Control())
        
        if (self.pg.on('variables')):
            candidates.append(PG_Assignment().featurize(self.pg))

        return R.choose_from(candidates)
    
    def __str__(self: Self) -> str:
        return str(self.generate())
