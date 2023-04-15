from js_random import JS_Random as R
from typing import Self
import pg


class String(pg.Mixin_Generatable, pg.Mixin_Renderable):
    def get_patterns(self: Self) -> list[str|pg.FP]:
        return [
            pg.FP(pg.FN(String_Literal), weight=4),
            pg.FP(pg.FN(String_Operation), weight=1),
            pg.FP(pg.FN(pg.Function_Call, [True, 'string']), weight=1, reqs=pg.FR('functions')),
            pg.FP(pg.FN(pg.Variable, 'string'), weight=2, reqs=pg.FR('variables')),
            # TODO function str(number, bool, string???, input???)
        ]

class String_Operation(pg.Mixin_Generatable, pg.Mixin_Renderable_Operation):
    def get_patterns(self: Self) -> list[str|pg.FP]:
        return [
            pg.FP(pg.FN(String), '+', pg.FN(String), weight=3),
            pg.FP(pg.FN(pg.Integer), '*', pg.FN(String), weight=1),
            pg.FP(pg.FN(String), '*', pg.FN(pg.Integer), weight=1),
        ]

class String_Literal(pg.Mixin_Generatable, pg.Mixin_Renderable):
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

# TODO String_Method
