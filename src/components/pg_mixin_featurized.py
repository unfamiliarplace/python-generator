from typing import Self
from pg import PythonGenerator

class PG_Mixin_Featurized():

    def featurize(self: Self, pg: PythonGenerator=None) -> Self:
        self.pg = pg
        return self
