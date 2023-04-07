from components.pg_expression import PG_Expression
from components.pg_renderable import PG_Renderable
from typing import Self

class PG_Return():

    def generate(self: Self) -> PG_Renderable:
        return PG_Expression()
    
    def __str__(self: Self) -> str:
        return f'return {self.generate()}'
