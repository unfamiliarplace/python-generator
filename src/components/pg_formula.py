from components.pg_sequence import PG_Sequence

# Oh my GOODNESS this is GODAWFUL there must be a better way
import importlib
from typing import Self

class PG_Formula():

    def __init__(self: Self, *components: str) -> None:
        self.components = components
    
    def parse(self: Self) -> PG_Sequence:
        parsed_components = []

        for item in self.components:
            if item.startswith('<') and item.endswith('>'):
                item = item[1:-1]
                parts = item.split('|')
                component_key = parts[0]

                module_name = f'components.{component_key.lower()}'
                module = importlib.import_module(module_name)
                component_class = getattr(module, component_key)
     
                args = []
                kwargs = {}

                if len(parts) > 1:

                    for arg in parts[1].split(';'):
                        if '=' in arg:
                            k, v = arg.split('=')
                            kwargs[k] = eval(v)
                        else:
                            args.append(eval(arg))

                parsed_components.append(component_class(*args, **kwargs))
        
            else:
                parsed_components.append(item)
        
        return PG_Sequence(*parsed_components)
