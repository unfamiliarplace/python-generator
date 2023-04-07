from components.pg_renderable import PG_Renderable
from components.pg_statement import PG_Statement
from typing import Self

class PG_Assignment(PG_Statement):

    def __init__(self: Self) -> None:
        pass

    def generate(self: Self) -> PG_Renderable:
        return PG_Renderable()

    def __str__(self: Self) -> str:
        return ''