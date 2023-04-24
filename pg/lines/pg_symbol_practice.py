import pg


class Symbol_Practice(pg.Mixin_Generatable, pg.Mixin_Renderable):
    
    def get_patterns(self) -> list[str|pg.FP]:
        return [
            "!", ":", ",", "()", "[]", "{}", "*", "<", ">", "==", "+", "-", "_", "#", "/", "\\", "//", ".", ";"
        ]
