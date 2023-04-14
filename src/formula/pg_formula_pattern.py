import pg
from typing import Self

class Formula_Pattern():

    def __init__(self: Self, *nodes: str|pg.Formula_Node, reqs: pg.Formula_Requirement=None, weight: int=1) -> None:
        self.nodes = nodes
        self.reqs = reqs
        self.weight = weight

    def possible(self: Self) -> bool:
        return self.reqs is None or self.reqs.met()
    
    def uses(self: Self, cls: type) -> bool:
        return any(c.component_cls == cls for c in self.nodes)
    
    def generate(self: Self) -> pg.Sequence:
        """Assumes possible"""
        return pg.Sequence(*(str(c) for c in self.nodes))
        
    def __str__(self: Self) -> str:
        """Assumes possible"""
        return str(self.generate())
