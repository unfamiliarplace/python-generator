from js_random import JS_Random as R
from typing import Self
import pg

class Real_World(pg.Mixin_Generatable, pg.Mixin_Renderable):
    """All candidate files combined in one for Transcryptability."""

    def generate(self: Self) -> str:        

        with open(f'data/real_world/_real_world_combined.txt', 'r') as f:
            lines = list(filter(lambda p: bool(p.strip()), f.readlines()))
            line = R.choose_from(lines)

            # typability
            line = line.strip()
            while '  ' in line:
                line = line.replace('  ', ' ')

            return line
