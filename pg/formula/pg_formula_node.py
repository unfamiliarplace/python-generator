import pg


class Formula_Node():

    def __init__(self, component_cls: type, *args, **kwargs) -> None:
        self.component_cls = component_cls
        self.args = args
        self.kwargs = kwargs
    
    def evaluate(self) -> pg.Mixin_Renderable:
        return self.component_cls(*self.args, **self.kwargs)
        
    def __str__(self) -> str:
        return str(self.evaluate())

# Short name
FN = Formula_Node
