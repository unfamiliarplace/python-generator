
from typing import Self
from enum import Enum
from pg import PythonGenerator

class Requirement_Mode(Enum):
    NONE = 0
    ANY = 1
    ALL = 2

class Formula_Requirement():

    req_checkers = {
        Requirement_Mode.NONE: PythonGenerator().none,
        Requirement_Mode.ANY: PythonGenerator().any,
        Requirement_Mode.ALL: PythonGenerator().all,
    }

    def __init__(self: Self, *reqs: str, req_mode: int=Requirement_Mode.ALL) -> None:

        # TODO in order for this to work we need to access the instantiated PG not the static class

        self.req_mode = req_mode
        self.reqs = reqs
    
    def met(self: Self) -> bool:
        return self.req_checkers[self.req_mode](*self.reqs)

# Short name
FR = Formula_Requirement
