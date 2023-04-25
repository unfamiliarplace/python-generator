from util.js_random import JS_Random as R
from data.real_world.real_world_lines import REAL_WORLD_LINES

from mixins.pg_mixin_generatable import Mixin_Generatable
from mixins.pg_mixin_renderable import Mixin_Renderable

class Real_World(Mixin_Generatable, Mixin_Renderable):
    """All candidate files combined in one for Transcryptability."""

    def generate(self) -> str:
        line = R.choose_from(REAL_WORLD_LINES)
        # typability
        line = line.strip()
        while '  ' in line:
            line = line.replace('  ', ' ')

        return line
