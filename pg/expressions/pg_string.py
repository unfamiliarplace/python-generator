from js_random import JS_Random as R

from expressions.pg_function_call import RT, Function_Call
from expressions.pg_integer import Integer
from expressions.pg_variable import Variable
from formula.pg_formula_node import FN
from formula.pg_formula_pattern import FP
from formula.pg_formula_requirement import FR
from mixins.pg_mixin_generatable import Mixin_Generatable
from mixins.pg_mixin_renderable import Mixin_Renderable
from mixins.pg_mixin_renderable_operation import Mixin_Renderable_Operation

class String(Mixin_Generatable, Mixin_Renderable):
    def get_patterns(self) -> list[str|FP]:
        return [
            FP(FN(String_Literal), weight=4),
            FP(FN(String_Operation), weight=1),
            FP(FN(Function_Call, [RT.STR]), weight=1, reqs=FR('functions')),
            FP(FN(Variable, 'string'), weight=2, reqs=FR('variables')),
            # TODO function str(number, bool, string???, input???)
        ]

class String_Operation(Mixin_Generatable, Mixin_Renderable_Operation):
    def get_patterns(self) -> list[str|FP]:
        return [
            FP(FN(String), '+', FN(String), weight=5),
            FP(FN(Integer, 0, 100), '*', FN(String), weight=1),
            FP(FN(String), '*', FN(Integer, 0, 100), weight=1),
        ]

class String_Literal(Mixin_Generatable, Mixin_Renderable):
    
    words = ";hello;world;day;find;eat;student;huge;goodbye;math;english;physics;chemistry;biology;french;stem;art;drama;music;geography;history;philosophy;cs;eblock;aps;periwinkle;first;second;violin;piano;sun;snow;rain;sleet;hail;fog;breeze;a;b;c;d;e;f;g;h;i;j;k;l;m;n;o;p;q;r;s;t;u;v;w;x;y;z;foo;bar;baz;mark;matthew;luke;john;sawczak;groot;kim;robinson;peters;van schepen;dykxhoorn;hoving;petrusma;gretton;brown;black;red;fuchsia;green;yellow;white;grey;black;blue;teal;turquoise;purple;violet;indigo;orange;gold;forest;beach;hills;mountains;desert;plains;prairie;sky"

    def __init__(self) -> None:
        # TODO generate dynamically?
        self.words = self.words.split(';')

    def generate(self) -> str:
        s = R.choose_from(self.words)
        n = 1
        chance = 0.5

        while (n < 4) and (R.flip_coin(chance)):
            s += ' ' + R.choose_from(self.words)
            n += 1
            chance = 1 / ((n * 2) + 2)
        
        return s

    def __str__(self) -> str:
        s = self.generate()
        q = "'"
        if R.flip_coin(0.5):
            q = '"'
        elif R.flip_coin(0.25):
            q = '"""'

        return f'{q}{s}{q}'

# TODO String_Method
