from pg import PythonGenerator
from typing import Self
from enum import Enum

class PG_Requirement_Mode(Enum):
    NONE = 0
    ANY = 1
    ALL = 2

class PG_Formula_Requirement():

    req_checkers = {
        PG_Requirement_Mode.NONE: PythonGenerator.none,
        PG_Requirement_Mode.ANY: PythonGenerator.any,
        PG_Requirement_Mode.ALL: PythonGenerator.all,
    }

    def __init__(self: Self, reqs: list[str]=[], req_mode: int=PG_Requirement_Mode.ALL) -> None:

        # TODO in order for this to work we need to access the instantiated PG not the static class

        self.req_mode = req_mode
        self.reqs = reqs
    
    def met(self: Self) -> bool:
        return self.req_checkers[self.req_mode](*self.reqs)
    
# Shorthand...
FR = PG_Formula_Requirement
RM = PG_Requirement_Mode
