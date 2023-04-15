from typing import Self
from formula.pg_formula_pattern import Formula_Pattern
from mixins.pg_mixin_generatable import Mixin_Generatable
from mixins.pg_mixin_renderable import Mixin_Renderable

from js_random import JS_Random as R

class Import(Mixin_Generatable, Mixin_Renderable):

    def get_patterns(self: Self) -> list[str|Formula_Pattern]:
        return [
            'math', 'random', 'itertools', 'functools', 'tkinter', 'PIL', 'nltk', 'pandas', 'numpy', 'turtle', 'sys', 'os', 'urllib', 'requests', 'shutil'
        ]

    lib_to_names = {
        'math': ['pi', 'inf'],
        'random': ['randint', 'randrange', 'choice', 'shuffle'],
        'itertools': ['combinations', 'permutations', 'accumulate', 'chain', 'pairwise'],
        'tkinter': ['Tk', 'font', 'messagebox', 'ttk', 'filedialog'],
        'PIL': ['Image'],
        'pandas': ['Series', 'DataFrame'],
        'numpy': ['array'],
        'sys': ['exit'],
        'os': ['copy', 'move', 'mkdir', 'rename', 'walk'],
        'shutil': ['copy'],
        'requests': ['get'],
    }

    def __str__(self: Self) -> str:
        lib = self.generate()
        has_name = lib in self.lib_to_names

        if has_name and R.flip_coin(.2):
            name = R.choose_from(self.lib_to_names[lib])

            if R.flip_coin(.25):
                append = f' as {name[0]}'

            return f'from {lib} import {name}{append}'
        
        elif R.flip_coin(.15):
            return f'from {lib} import *'
        
        else:
            if R.flip_coin(.2):
                append = f' as {lib[0]}'

            return f'import {lib}{append}'
