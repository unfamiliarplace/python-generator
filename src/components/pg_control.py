from pg_statement import PG_Statement

controls = [
    'for i in range(<PG_Variable|PG_Int[2, 101]>):',
    'for <PG_Variable> in <PG_Container|PG_Variable[plural=True]>:',
    'while <Boolean>:',
    'if <Boolean>:',
]

class PG_Control(PG_Statement):
    pass
