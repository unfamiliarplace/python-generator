from components.pg_formula_node import PG_Formula_Node
from components.pg_formula_requirement import PG_Formula_Requirement
from components.pg_sequence import PG_Sequence
from typing import Self

class PG_Formula_Pattern():

    def __init__(self: Self, reqs: PG_Formula_Requirement=None, weight: int=1, *components: str|PG_Formula_Node) -> None:
        self.components = components
        self.reqs = reqs
        self.weight = weight

    def possible(self: Self) -> bool:
        return self.reqs is None or self.reqs.met()
    
    def uses(self: Self, cls: type) -> bool:
        return any(c.component_class == cls for c in self.components)
    
    def generate(self: Self) -> PG_Sequence:
        """Assumes possible"""
        return PG_Sequence(*(str(c) for c in self.components))
        
    def __str__(self: Self) -> str:
        """Assumes possible"""
        return str(self.generate())
    
# Shorthand...
FP = PG_Formula_Pattern
