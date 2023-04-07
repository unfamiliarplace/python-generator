from pg_expression import PG_Expression

class PG_Function(PG_Expression):
    
    def evaluate(self: Self) -> str:
        return 'function'
