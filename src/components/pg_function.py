from components.pg_expression import PG_Expression
from typing import Self

class PG_Function(PG_Expression):
    # TODO

    def __init__(self: Self) -> None:
        pass

    def generate(self: Self) -> object:
        return None
    
    def __str__(self: Self) -> str:
        return str(self.generate())
