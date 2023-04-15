from js_random import JS_Random as R
from typing import Self

import os

class Real_World(Mixin_Generatable, Mixin_Renderable):

    def generate(self: Self) -> str:
        fnames = list(os.walk('data'))[0][2]
        fname = R.choose_from(fnames)
        print(fname)

        with open(f'data/{fname}', 'r') as f:
            lines = list(filter(lambda p: bool(p.strip()), f.readlines()))
            return R.choose_from(lines)
