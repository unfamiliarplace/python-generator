from formula.pg_formula_node import Formula_Node
from formula.pg_formula_requirement import Formula_Requirement
from formula.pg_sequence import Sequence

from typing import Self

class Formula_Pattern():

    def __init__(self: Self, *nodes: str|Formula_Node, reqs: Formula_Requirement=None, weight: int=1) -> None:
        self.nodes = nodes
        self.reqs = reqs
        self.weight = weight

    def possible(self: Self) -> bool:
        return self.reqs is None or self.reqs.met()
    
    def uses(self: Self, *clses: type) -> bool:
        for cls in clses:
            if any(c.component_cls == cls for c in self.nodes):
                return True
        return False
    
    def generate(self: Self) -> Sequence:
        """Assumes possible"""
        return Sequence(*(str(c) for c in self.nodes))
        
    def __str__(self: Self) -> str:
        """Assumes possible"""
        return str(self.generate())

# Short name
FP = Formula_Pattern
