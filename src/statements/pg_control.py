from pg import *

class Control(Mixin_Generatable, Mixin_Renderable):

    patterns = [
        # TODO for i in range(int)
        # TODO for i in range(len(container))

        FP('for', FN(Variable, 'element'), 'in', FN(Container), reqs=FR('containers')),

        # TODO instead, have container have a variable of type container as a pattern
        # FP('for', FN(Variable, 'element'), 'in', FN(Variable, 'container'), reqs=FR('containers')),

        FP('while', FN(Boolean)),
        FP('if', FN(Boolean)),

        FP('break')
    ]
