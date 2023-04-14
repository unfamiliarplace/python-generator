from js_random import JS_Random as R
from typing import Self
from pg import *
import os

class Real_World(Mixin_Generatable, Mixin_Renderable):

    def generate(self: Self) -> str:
        fnames = list(os.walk('data'))[0][2]
        fname = R.choose_from(fnames)

        with open(f'src/data/{fname}', 'r') as f:
            lines = f.readlines()
            return R.choose_from(lines)
