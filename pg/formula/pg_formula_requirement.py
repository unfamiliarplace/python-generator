import features

class Requirement_Mode():
    NONE = 0
    ANY = 1
    ALL = 2

RM = Requirement_Mode

class Formula_Requirement():

    def __init__(self, *reqs: str, req_mode: int=RM.ALL) -> None:

        # TODO in order for this to work we need to access the instantiated PG not the static class

        self.req_mode = req_mode
        self.reqs = reqs
    
    def met(self) -> bool:

        # argh
        req_checkers = {
            RM.NONE: features.none,
            RM.ANY: features.any,
            RM.ALL: features.all,
        }

        return req_checkers[self.req_mode](*self.reqs)

# Short name
FR = Formula_Requirement
