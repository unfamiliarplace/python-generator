from js_random import JS_Random as R
from typing import Self
from components.pg_mixin_generatable import PG_Mixin_Generatable
from components.pg_mixin_renderable import PG_Mixin_Renderable

words = "hello;world;day;find;eat;student;huge;goodbye;math;english;physics;chemistry;biology;french;stem;art;drama;music;geography;history;philosophy;cs;eblock;aps;periwinkle;first;second;violin;piano;sun;snow;rain;sleet;hail;fog;breeze;a;b;c;d;e;f;g;h;i;j;k;l;m;n;o;p;q;r;s;t;u;v;w;x;y;z;foo;bar;baz;mark;matthew;luke;john;sawczak;groot;kim;robinson;peters;van schepen;dykxhoorn;hoving;petrusma;gretton;brown;black;red;fuchsia;green;yellow;white;grey;black;blue;teal;turquoise;purple;violet;indigo;orange;gold;forest;beach;hills;mountains;desert;plains;prairie;sky"
words = words.split(';');

class PG_String(PG_Mixin_Generatable, PG_Mixin_Renderable):

    def generate(self: Self) -> str:
        s = R.choose_from(words)
        n = 1
        chance = 0.5

        while (n < 4) and (R.flip_coin(chance)):
            s += ' ' + R.choose_from(words)
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
