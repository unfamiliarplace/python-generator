from js_random import JS_Random as R
import pg
from data.real_world.real_world_lines import REAL_WORLD_LINES

class Real_World(pg.Mixin_Generatable, pg.Mixin_Renderable):
    """All candidate files combined in one for Transcryptability."""

    def generate(self) -> str:
        line = R.choose_from(REAL_WORLD_LINES)
        # typability
        line = line.strip()
        while '  ' in line:
            line = line.replace('  ', ' ')

        return line
