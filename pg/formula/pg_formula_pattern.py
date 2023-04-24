import pg

class Formula_Pattern():

    def __init__(self, *nodes: str|pg.FN, reqs: pg.Formula_Requirement=None, weight: int=1, brackets: bool=False, prefix: str='', suffix: str='') -> None:
        self.nodes = nodes
        self.reqs = reqs
        self.weight = weight
        self.brackets = brackets
        self.prefix = prefix
        self.suffix = suffix

        self.bracket_open = '(' if self.brackets else ''
        self.bracket_close = '(' if self.brackets else ''

    def possible(self) -> bool:
        return self.reqs is None or self.reqs.met()
    
    def uses(self, *clses: type) -> bool:
        for cls in clses:
            if any(c.component_cls == cls for c in self.nodes):
                return True
        return False
    
    def generate(self) -> pg.Sequence:
        return pg.Sequence(*(str(c) for c in self.nodes))
        
    def __str__(self) -> str:
        s = self.generate()
        return f'{self.prefix}{self.bracket_open}{s}{self.bracket_close}{self.suffix}'

# Short name
FP = Formula_Pattern
