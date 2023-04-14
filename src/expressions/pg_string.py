from js_random import JS_Random as R
from typing import Self
from pg import *

class String(Mixin_Generatable, Mixin_Renderable):
    pass

class String_Operation(Mixin_Generatable, Mixin_Renderable_Operation):
    pass

class String_Literal(Mixin_Generatable, Mixin_Renderable):
    # TODO generate?
    words = "hello;world;day;find;eat;student;huge;goodbye;math;english;physics;chemistry;biology;french;stem;art;drama;music;geography;history;philosophy;cs;eblock;aps;periwinkle;first;second;violin;piano;sun;snow;rain;sleet;hail;fog;breeze;a;b;c;d;e;f;g;h;i;j;k;l;m;n;o;p;q;r;s;t;u;v;w;x;y;z;foo;bar;baz;mark;matthew;luke;john;sawczak;groot;kim;robinson;peters;van schepen;dykxhoorn;hoving;petrusma;gretton;brown;black;red;fuchsia;green;yellow;white;grey;black;blue;teal;turquoise;purple;violet;indigo;orange;gold;forest;beach;hills;mountains;desert;plains;prairie;sky"
    words = words.split(';')

    def generate(self: Self) -> str:
        s = R.choose_from(self.words)
        n = 1
        chance = 0.5

        while (n < 4) and (R.flip_coin(chance)):
            s += ' ' + R.choose_from(self.words)
            n += 1
            chance = 1 / ((n * 2) + 2)
        
        return s  

    def __str__(self: Self) -> str:
        s = self.generate()
        q = "'"
        if R.flip_coin(0.5):
            q = '"'
        elif R.flip_coin(0.25):
            q = '"""'

        return f'{q}{s}{q}'

String.patterns = [
    FP(FN(String_Literal), weight=4),
    FP(FN(String_Operation), weight=1),
    FP(FN(Function_Call, [True, 'string']), weight=1, reqs=FR('functions')),
    FP(FN(Variable, 'string'), weight=2, reqs=FR('variables')),
    # TODO function str(number, bool, string???, input???)
]

String_Operation.patterns = [
    FP(FN(String), '+', FN(String), weight=3),
    FP(FN(Integer), '*', FN(String), weight=1),
    FP(FN(String), '*', FN(Integer), weight=1),
]

# TODO String_Method
