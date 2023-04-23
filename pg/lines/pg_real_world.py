from js_random import JS_Random as R
from typing import Self
import pg

import os

class Real_World(pg.Mixin_Generatable, pg.Mixin_Renderable):
    """Separate candidate files."""

    def generate(self: Self) -> str:
        fnames = list(os.walk('data/real_world'))[0][2]
        fname = R.choose_from(fnames)

        with open(f'data/real_world/{fname}', 'r') as f:
            lines = list(filter(lambda p: bool(p.strip()), f.readlines()))
            line = R.choose_from(lines)

            # typability
            line = line.strip()
            while '  ' in line:
                line = line.replace('  ', ' ')

            return line