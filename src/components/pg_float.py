from js_random import JS_Random as R
from pg_expression import PG_Expression

class PG_Float(PG_Expression):

    def __init__(self: Self, lower: int=-50, upper: int=100) -> None:
        self.lower = lower
        self.upper = upper

    def evaluate(self: Self) -> int:
        return R.number_between(self.lower, self.upper, True)
