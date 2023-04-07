from js_random import JS_Random as R
from pg_expression import PG_Expression
from pg_int import PG_Int
from pg_float import PG_Float

class PG_Number(PG_Expression):

    def __init__(self: Self, lower: int=-50, upper: int=100, decimal: bool=False) -> None:
        if decimal:            
            self.number = PG_Int(lower, upper)
        else:
            self.number = PG_Float(lower, upper)

    def evaluate(self: Self) -> int:
        return self.number.evaluate()
    