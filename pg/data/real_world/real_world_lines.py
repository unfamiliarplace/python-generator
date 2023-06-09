REAL_WORLD_TEXT = """
import timeit
import random
from pandas import Series
from numpy import array

_L = [random.randint(1, 1_000) for _ in range(1_000)]

def _plus5(n):
    return n + 5

def loop_build_add(L):
    L2 = []
    for elem in L:
        L2 = L2 + [elem + 5]

def loop_build_increment(L):
    L2 = []
    for elem in L:
        L2 += [elem + 5]

def loop_build_append(L):
    L2 = []
    for elem in L:
        L2.append(elem + 5)

def loop_build_extend(L):
    L2 = []
    for elem in L:
        L2.extend([elem + 5])

def loop_build_zeroes(L):
    L2 = [0] * len(L)
    for i in range(len(L)):
        L2[i] = L[i] + 5

def loop_inplace_add(L):
    for i in range(len(L)):
        L[i] = L[i] + 5

def loop_inplace_increment(L):
    for i in range(len(L)):
        L[i] += 5

def map_gen(L):
    map(_plus5, L)

def map_cast(L):
    list(map(_plus5, L))

def listcomp_gen(L):
    (elem + 5 for elem in L)

def listcomp_cast(L):
    [elem + 5 for elem in L]

def pandas_series(L):
    Series(L) + 5

def pandas_series_cast(L):
    (Series(L) + 5).tolist()

def numpy_array(L):
    array(L) + 5

def numpy_array_cast(L):
    (array(L) + 5).tolist()

methods = [
    loop_build_add,       # takes obnoxiously long, about 1 order of magnitude more
    loop_build_increment,
    loop_build_append,
    loop_build_extend,
    loop_build_zeroes,
    loop_inplace_add,
    loop_inplace_increment,
    map_gen,
    map_cast,
    listcomp_gen,
    listcomp_cast,
    pandas_series,
    pandas_series_cast,
    numpy_array,
    numpy_array_cast
]

for cb in methods:
    result = timeit.timeit(lambda: cb(_L[:]), number=10_000)
    print(f'{cb.__name__: <25}{result:.5f}')
# This script allows you modify a subtitle file by a given offset.

# IMPORTS

import re

# CONSTANTS

# Example line: 00:00:33,159 --> 00:00:35,999
MARKER      = '-->'
MIN         = 60000
HR          = 60 * MIN
TS          = r'<p begin="(.*?)" end="(.*?)" region="AmazonDefaultRegion" style="AmazonDefaultStyle">(.*?)</p>'

# WORKING WITH TIMESTAMPS

def parse_ts(ts: str) -> int:
    \"\"\"Return the number of milliseconds in a given timestamp.\"\"\"

    # Get the separate parts
    hrs, mins, ms = ts.split(':')
    ms = ms.replace('.', '')

    # Turn them into a single int
    ms = int(ms)
    ms += int(mins) * MIN
    ms += int(hrs) * HR

    return ms


def format_ts(ms: int) -> str:
    \"\"\"Format the given milliseconds as a timestamp.\"\"\"

    hrs = 0
    mins = 0

    # Count hours
    while ms > HR:
        ms -= HR
        hrs += 1

    # Count minutes
    while ms > MIN:
        ms -= MIN
        mins += 1

    # Format
    ts = '{}:{}:{}'.format(
        str(hrs).zfill(2),
        str(mins).zfill(2),
        str(ms).zfill(5)
    )

    ts = ts[:-3] + ',' + ts[-3:]
    return ts

def format_sub(start, end, sub) -> str:
    \"\"\"Return a formatted subtitle.\"\"\"

    sub = sub.replace('<br />', '\\]n')
    if sub.startswith("'") and sub.endswith("'"):
        sub = f'<i>{sub[1:-1]}</i>'

    start = format_ts(parse_ts(start))
    end = format_ts(parse_ts(end))

    return f'{start} --> {end}\\n{sub}'

# WORKING WITH LINES

def convert_line(line: str) -> str:
    match = re.search(TS, line)
    if match:
        start, end, sub = match.group(1), match.group(2), match.group(3)
        return format_sub(start, end, sub)    

def convert_lines(lines: list) -> iter:
    i = 1
    for line in lines:
        conv = convert_line(line)
        if conv:
            yield f'{i}\\n{conv}'
            i += 1

# RUNNING

def prompt_fname() -> str:
    \"\"\"Return a str (filename).\"\"\"

    fname = input('Enter the name of a subtitle file: ').strip()
    return fname

def prompt_offset() -> int:
    \"\"\"Return an int (milliseconds offset).\"\"\"

    offset = int(input('Enter an offset in milliseconds: ').strip())
    return offset

def get_fix_fname(fname: str) -> str:
    \"\"\"Return the filename for the fixed version.\"\"\"
    
    return f'{fname[:fname.rfind(".")]}_fix.srt'
    

def run() -> None:
    \"\"\"Open file, correct each line, save to new file.\"\"\"

    # Determine filenames and offset
    fname = prompt_fname()
    fname_fix = get_fix_fname(fname)

    with open(fname, 'r') as f, open(fname_fix, 'w') as f_fix:
        lines = convert_lines(f.readlines())
        f_fix.write('\\n\\n'.join(lines))

    # Report 
    input('Saved to {}\\nPress Enter to quit.'.format(fname_fix))


# PROGRAM

if __name__ == '__main__':
    run()
def count_lines():
    
    while True:
        filename = input('Enter a filename: ')
        
        try:
            file = open(filename, 'r')
            break
        except(FileNotFoundError):
            print("Couldn't find that file.")
            
    lines = 0
    for line in file:
        line = line.strip()
        lines += bool(line)
    file.close()
    
    print('{} non-empty lines.'.format(lines))
        
count_lines()
# Imports
import random

print()
input('Enter to quit')
import requests
import os
import shutil

dir_out = './output'
if not os.path.exists(dir_out):
    os.mkdir(dir_out)

placeholder = '****'

stem_host = 'https://ia803205.us.archive.org'
stem_dir = 'BookReader/BookReaderPreview.php'
stem_data = {
    'id'        : 'seizeday0000bell_x5c5',
    'subPrefix' : 'seizeday0000bell_x5c5',
    'itemPath'  : '/13/items/seizeday0000bell_x5c5',
    'server'    : 'ia803205.us.archive.org',
    'page'      : f'leaf{placeholder}',
    'fail'      : 'preview',
    'scale'     : '1',
    'rotate'    : '0'
}

stem2_host = 'https://ia903205.us.archive.org'
stem2_dir = 'BookReader/BookReaderImages.php'
stem2_data = {
    'zip'       : '/13/items/seizeday0000bell_x5c5/seizeday0000bell_x5c5_jp2.zip',
    'file'      : f'seizeday0000bell_x5c5_jp2/seizeday0000bell_x5c5_{placeholder}.jp2',
    'id'        : 'id=seizeday0000bell_x5c5',
    'scale'     : '1',
    'rotate'    : '0'
}


def construct_url(n: int) -> str:
    url = f'{stem_host}/{stem_dir}'
    data = stem_data.copy()
    data['page'] = data['page'].replace(placeholder, str(n))
    argstr = '&'.join(f'{k}={v}' for (k, v) in data.items())
    return f'{url}?{argstr}'

def construct_url2(n: int) -> str:
    url = f'{stem2_host}/{stem2_dir}'
    data = stem2_data.copy()
    data['file'] = data['file'].replace(placeholder, f'{n:0>4}')
    argstr = '&'.join(f'{k}={v}' for (k, v) in data.items())
    return f'{url}?{argstr}'    

def construct_a(url: str, n: int) -> str:
    return f'<a href="{url}">{n:0>4}.jpg</a>'


for i in range(8, 149):
    url = construct_url2(i)
    a = construct_a(url, i)
    print(a)

    
    continue
    
    r = requests.get(url, stream=True)
    
    if r.status_code == 200:    
        fname = f'{dir_out}/{i:0>4}.jpg'
        with open(fname, 'wb') as f:
            shutil.copyfileobj(r.raw, f)
        print(f'Downloaded {i:0>4}')
    else:
        print(f'Unable to download {i:0>4}')

    
# https://zeldauniverse.net/media/music/links-awakening-original-soundtrack/

import urllib.request
import requests
DIR_DL = 'E:/Luke/Desktop/link'
SRC_LIST = 'E:/Luke/Desktop/src.txt'
EXT = 'mp3'

# gather urls

urls = []
with open(SRC_LIST, 'r') as f:
    urls = (L.strip() for L in f.readlines())

        
# download over https
            
for url in urls:
    fname = url[url.rfind('/')+1:]
    
    r = requests.get(url)
    if r.status_code != 200:
        print(f'Could not access {fname}. trying other method')
        urllib.request.urlretrieve(url, f'{DIR_DL}/{fname}')
    else:
        with open(f'{DIR_DL}/{fname}', 'wb') as f:
            f.write(r.content)
        print(f'Downloaded {fname}')


# download over http
           
##for url in urls:
##    fname = url[url.rfind('/')+1:]
##    urllib.request.urlretrieve(url, f'{DIR_DL}/{fname}')
# https://zeldauniverse.net/media/music/links-awakening-original-soundtrack/

import urllib.request
import requests
import os

DIR_DL = 'link'
SRC_HTML = 'src.txt'
REL_BASE = 'http://galactic-voyage.com'
EXT = 'mp3'

# gather urls

urls = []
with open(SRC_HTML, 'r') as f:
    content = f.read()
    i = 0
    url = ''
    while i < len(content):
        if content[i] == 'a' and content[i:i+8] == 'a href="':
            url = content[i+8:content.find('"', i+8)]
            if EXT in url:
                urls.append(url)
        i += 1

# get src as inputs instead of constants
# TODO

# make output folder
if not os.path.exists(DIR_DL):
    os.mkdir(DIR_DL)
        
# download over https
            
for url in urls:
    if not url.startswith('http'):
        url = f'{REL_BASE}/{url}'
    fname = url[url.rfind('/')+1:]
    
    r = requests.get(url)
    if r.status_code != 200:
        print(f'Could not access {fname}')
    else:
        with open(f'{DIR_DL}/{fname}', 'wb') as f:
            f.write(r.content)
        print(f'Downloaded {fname}')


# download over http
           
##for url in urls:
##    fname = url[url.rfind('/')+1:]
##    urllib.request.urlretrieve(url, f'{DIR_DL}/{fname}')
no_words = {
    1: set(),
    2: set(),
    3: set(),
    4: set()
}

yes_words = {
    1: set(),
    2: set(),
    3: set(),
    4: set()
}

# load already filtered
with open('cmudict_no.txt', 'r') as f:
    adding_to = no_words
    for line in f.readlines():
        word = line.strip()

        # skip comment
        if word.startswith('#'):
            continue

        # switch if we hit the blank line
        if not word:
            adding_to = yes_words
        else:  
            adding_to[len(word)].add(word)

# go through rest
with open('cmudict.txt', 'r') as f:
    i = 0
    lines = f.readlines()
    while i < len(lines):
        line = lines[i]
        word = line.split(' ')[0]
        
        if (len(word) in no_words) and all(c.isalpha() for c in word):
            if word not in no_words[len(word)] and word not in yes_words[len(word)]:
                keep = input(f'Q | Enter | . | +WORD | -WORD < {word.lower()} : ').lower().strip()

                if keep == 'q':
                    i = len(lines)
                    
                elif keep == '.':
                    yes_words[len(word)].add(word)
                    
                elif keep.startswith('+'):
                    restore = keep.split('+')[1].strip().upper()
                    if restore in yes_words[len(restore)]:
                        yes_words[len(restore)].add(restore)
                    if restore in no_words[len(restore)]:
                        no_words[len(restore)].remove(restore)
                    print(f'restored {restore}')
                    i -= 1
                    
                elif keep.startswith('-'):
                    drop = keep.split('-')[1].strip().upper()
                    if drop in no_words[len(drop)]:
                        no_words[len(drop)].add(drop)
                    if drop in yes_words[len(drop)]:
                        yes_words[len(drop)].remove(drop)
                    print(f'dropped {drop}')
                    i -= 1
                    
                else:
                    no_words[len(word)].add(word)
        i += 1

# save all
with open('cmudict_no.txt', 'w') as f:
    f.write('# no words\\n')
    for length in sorted(no_words.keys()):
        for word in sorted(no_words[length]):
            f.write(word + '\\n')
    f.write('\\n# yes words\\n')
    for length in sorted(yes_words.keys()):
        for word in sorted(yes_words[length]):
            f.write(word + '\\n')

for i in range(1, 101):
    th = bool(i % 3)
    fi = bool(i % 5)
    p = str(i) * (not (th or fi))
    p += 'Fizz' * (not th)
    p += 'Buzz' * (not fi)
    print(p)
    
import os

for item in list(os.walk('.'))[0][2]:
    if item.endswith('flac'):
        with open(f'{item}.txt', 'w') as f:
            f.write('\\n')

import os

for item in list(os.walk('.'))[0][2]:
    if item.endswith('flac'):
        with open(f'{item}.txt', 'w') as f:
            f.write('\\n')

import os
import sys

THIS = 'listify.py'
SAFE = '_original'

cwd = os.getcwd()
yn = input(f'About to listify {cwd}. Enter "Y" to proceed: ')
if yn.strip().upper().startswith('Y'):
    print('OK, going')
else:
    input('Did not listify. Hit Enter to quit')
    sys.exit()

if not os.path.exists(SAFE):
    os.mkdir(SAFE)

for _, _, files in os.walk('.'):
    for fname in files:
        if fname == THIS:
            continue
        
        os.rename(fname, f'{SAFE}/{fname}')
        with open(f'{fname}.txt', 'w') as f:
            f.write(fname)

    # Just top level ...
    break

print(f'Listified {cwd}')
input('Hit Enter to quit')
def m_to_d_1(m: int) -> int:
    \"\"\"Hardcoding each relation\"\"\"

    if m == 1:
        return 31
    elif m == 2:
        return 28
    elif m == 3:
        return 31
    elif m == 4:
        return 30
    elif m == 5:
        return 31
    elif m == 6:
        return 30
    elif m == 7:
        return 31
    elif m == 8:
        return 31
    elif m == 9:
        return 30
    elif m == 10:
        return 31
    elif m == 11:
        return 30
    elif m == 12:
        return 31


def m_to_d_2(m: int) -> int:
    \"\"\"Hardcoding each relation, but code golfed\"\"\"
    
    return int('312831303130313130313031'[(m - 1) * 2:][:2])

def m_to_d_3(m: int) -> int:
    \"\"\"First attempt to find a pattern\"\"\"
    
    if m == 2:
        return 28
    elif m < 8:
        return 30 + m % 2
    else:
        return 31 - m % 2

def m_to_d_4(m: int) -> int:
    \"\"\"Same as 3 but as an expression instead of with control keywords\"\"\"

    return 28 + (2 * (m != 2)) + ((m < 8 and m % 2) or (m > 7 and not (m % 2)))



months = list(range(1, 13))
check = [m_to_d_1(m) for m in months]
test = [m_to_d_4(m) for m in months]
print(check == test)
def get_baskets_left(thousands, loaves):
    
    # http://www.biblegateway.com/passage/?search=mark%208:19-21&version=NIV
    
    if thousands == loaves:
        return 12
    else:
        return loaves

temp_loaves = int(input('How many loaves?: '))    
temp_thousands = int(input('How many thousands of people?: '))
print('{} baskets left over.'.format(get_baskets_left(temp_thousands, temp_loaves)))
print(" ")
print("Guess the number. You may only enter numerals.")
print("...It is winnable. >:)")
print(" ")

a = 0

while a == 0:
    x = float(input("How many? "))
    if x > 17.5 and x != 71:
        print("Not enough.")
        print(" ")
    elif x < 17.5:
        print("Too many.")
        print(" ")
    else:
        print("Yeah!")
        print("A chocolate bar is totally coming your way.")
        print("Any time now.")
        a = 1
        
input()
import os, time
os.chdir('C:\\')

ROWS = 15000
VARS = 34
MULT = 7

T_1 = time.time()
print(f'Started at {T_1}')

f = open('test.csv', 'w')

for i in range(ROWS):
    row = ''
    for v in range(VARS):
        row += f'{v};'
    f.write(row + '\\n')

f.close()

T_2 = time.time()
print(f'Time to finish original seed: {T_2 - T_1}')

f = open('test.csv', 'r')
f2 = open('testx7.csv', 'w')

for line in f.readlines():
    rows = [''] * MULT
    
    for item in line.split(';'):
        if item != '\\n':
            div = int(item) / MULT
            for i in range(MULT):
                rows[i] += f'{div};'

    for row in rows:
        f2.write(row + '\\n')

f.close()
f2.close()

T_3 = time.time()
print(f'Time to finish multiplication: {T_3 - T_2}')

print('Finished at {T_3}')

number = '8738942'
letters = {
    '2': set('ABC'),
    '3': set('DEF'),
    '3': set('GHI'),
    '4': set('JKL'),
    '6': set('MNO'),
    '7': set('PQRS'),
    '8': set('TUV'),
    '9': set('WXYZ')
}
allowed = set('MNODEFWXYZ')

words2 = set()
words2end = set()
words2mid = set()
words3 = set()
words3end = set()
words4 = set()
words4end = set()
words5 = set()
words5end = set()
words7 = set()
lengths = {2, 3, 4, 5, 7}

words = {
    7: words7,
    5: words5,
    4: words4,
    3: words3,
    2: words2,
    1005: words5end,
    1004: words4end,
    1003: words3end,
    1002: words2end,
    2002: words2mid
}

def can_make(word: str, offset: int=0) -> bool:
    for i, c in enumerate(word):
        if c not in letters[number[i + offset]]:
            return False
    else:
        return True

def can_start(word: str) -> bool:
    return can_make(word)

def can_end(word: str) -> bool:
    return can_make(word, len(number) - len(word))    
    

with open('cmudict.txt', 'r') as f:
    for line in f.readlines():
        word = line.split(' ')[0]
        n = len(word)
        if n in lengths:
            if can_start(word):
                words[n].add(word)
            if can_end(word):
                words[n + 1000].add(word)
            if n == 2 and can_make(word, 3):
                words[2002].add(word)


possible = set()

for word5 in words5:
    for word2 in words2:
        possible.add(f'{word5} {word2}')

for word4 in words4:
    for word3 in words3end:
        possible.add(f'{word4} {word3}')

for word3 in words3:
    for word4 in words4end:
        possible.add(f'{word3} {word4}')
    for word2mid in words2mid:
        for word2end in words2end: # happens to be 63 at start and end
            possible.add(f'{word3} {word2mid} {word2end}')

for word2 in words2:
    for word5 in words5end:
        possible.add(f'{word2} {word5}')

for word in sorted(possible, key=len, reverse=True):
    print(word)

LETTERS = {
    # 0 is a space and 1 maps to no letters
    '2': set('ABC'),
    '3': set('DEF'),
    '4': set('GHI'),
    '5': set('JKL'),
    '6': set('MNO'),
    '7': set('PQRS'),
    '8': set('TUV'),
    '9': set('WXYZ'),
}

prompt = \"\"\"Enter here:\"\"\"

no_words = set()

with open('cmudict_no.txt', 'r') as f:
    for word in f.readlines():
        word = word.strip()

        # Skip comments
        if word.startswith('#'):
            continue

        # Stop when we get to the yes words
        if not word:
            break
        
        no_words.add(word)

with open('cmudict.txt', 'r') as f:
    lines = f.readlines()
    

def extract_pieces(number: str) -> dict:
    pieces = {}
    for line in lines:
        word = line.split(' ')[0]
        n = len(word)
        
        # exception for ridiculous words...
        if word in no_words:
            if word == 'ME':
                print(word)
            continue
        
        for i in range(len(number)):
            if can_make(number, word, i):
                if n not in pieces:
                    pieces[n] = {}
                if i not in pieces[n]:
                    pieces[n][i] = set()
                
                pieces[n][i].add(word)
    return pieces

def can_make(number: str, word: str, offset: int=0) -> bool:
    if len(word) + offset > len(number):
        return False
    
    for i, c in enumerate(word):
        if c not in LETTERS[number[i + offset]]:
            return False
    else:
        return True

def can_start(number: str, word: str) -> bool:
    return can_make(number, word)

def can_end(number: str, word: str) -> bool:
    return can_make(number, word, len(number) - len(word))

def construct_phrases(number: str, pieces: dict) -> set:

    def _recurse(sub_number: str, phrase: str) -> set:

        # at each level, we get the remaining number,
        # and the word we're building up to that point.

        # for all words of the remaining length or less
        # at that offset, recurse using said word and
        # the number less than that word.

        # said recursion returns a set of phrases.
        # return a set consisting of the current word
        # concatenated with each of those phrases.

        # Base case: end of the word
        
        if not sub_number:
            return {phrase}
        
        else:
            phrases = set()
            i = len(number) - len(sub_number)
            
            for n in (n for n in pieces if n <= len(sub_number)):
                for word in pieces[n].get(i, ()):
                    subphrases = _recurse(sub_number[len(word):], word)
                    for subphrase in subphrases:
                        phrases.add(f'{phrase} {subphrase}')
            return phrases

    return _recurse(number, '')

def find_phrases(number: str) -> set:
    pieces = extract_pieces(number)
    return construct_phrases(number, pieces)

def chain(sets: list) -> list:
    if len(sets) == 1:
        return sets[0]
    else:
        words = []
        for outer in sets[0]:
            for inner in chain(sets[1:]):
                words.append(f'{outer}{inner}')
        return words

def multi_split(s: str, seps: str) -> list:
    parts = []
    part = ''
    for c in s:
        if (c in seps) and part:
            parts.append(part)
            part = ''
        else:
            part += c
    if part:
        parts.append(part)
    return parts

def sub_combos(number: str) -> list:
    sets = []
    parts = multi_split(number, '01')
    for part in parts:
        sets.append(find_phrases(part))
    sets = list(filter(lambda s: s, sets))
    return chain(sets) if sets else []

def sanitize_number(number: str) -> str:
    return ''.join(list(filter(lambda c: c.isdigit(), number)))

def run() -> None:
    number = sanitize_number(input(prompt))
    words = sub_combos(number)
    if not words:
        print('No words found')
    else:
        for word in sorted(words):
            print(word)

if __name__ == '__main__':
    run()
# TODO FOR v3
# hyphens to differentiate from spaces?
# option to filter stupid words?
# display original number for unused sections

LETTERS = {
    # 0 is a space and 1 maps to no letters
    '2': set('ABC'),
    '3': set('DEF'),
    '4': set('GHI'),
    '5': set('JKL'),
    '6': set('MNO'),
    '7': set('PQRS'),
    '8': set('TUV'),
    '9': set('WXYZ'),
}

prompt = \"\"\"Enter here: \"\"\"

no_words = set()

with open('cmudict_no.txt', 'r') as f:
    for word in f.readlines():
        word = word.strip()

        # Skip comments
        if word.startswith('#'):
            continue

        # Stop when we get to the yes words
        if not word:
            break
        
        no_words.add(word)

with open('cmudict.txt', 'r') as f:
    lines = f.readlines()
    

def extract_pieces(number: str) -> dict:
    pieces = {}
    for line in lines:
        word = line.split(' ')[0]
        n = len(word)
        
        # exception for ridiculous words...
        if word in no_words:
            if word == 'ME':
                print(word)
            continue
        
        for i in range(len(number)):
            if can_make(number, word, i):
                if n not in pieces:
                    pieces[n] = {}
                if i not in pieces[n]:
                    pieces[n][i] = set()
                
                pieces[n][i].add(word)
    return pieces

def can_make(number: str, word: str, offset: int=0) -> bool:
    if len(word) + offset > len(number):
        return False
    
    for i, c in enumerate(word):
        if c not in LETTERS[number[i + offset]]:
            return False
    else:
        return True

def can_start(number: str, word: str) -> bool:
    return can_make(number, word)

def can_end(number: str, word: str) -> bool:
    return can_make(number, word, len(number) - len(word))

def construct_phrases(number: str, pieces: dict) -> set:

    def _recurse(sub_number: str, phrase: str) -> set:

        # at each level, we get the remaining number,
        # and the word we're building up to that point.

        # for all words of the remaining length or less
        # at that offset, recurse using said word and
        # the number less than that word.

        # said recursion returns a set of phrases.
        # return a set consisting of the current word
        # concatenated with each of those phrases.

        # Base case: end of the word
        
        if not sub_number:
            return {phrase}
        
        else:
            phrases = set()
            i = len(number) - len(sub_number)
            
            for n in (n for n in pieces if n <= len(sub_number)):
                for word in pieces[n].get(i, ()):
                    subphrases = _recurse(sub_number[len(word):], word)
                    for subphrase in subphrases:
                        phrases.add(f'{phrase} {subphrase}')
            return phrases

    return _recurse(number, '')

def find_phrases(number: str) -> set:
    pieces = extract_pieces(number)
    return construct_phrases(number, pieces)

def chain(sets: list) -> list:
    if len(sets) == 1:
        return sets[0]
    else:
        words = []
        for outer in sets[0]:
            for inner in chain(sets[1:]):
                words.append(f'{outer}{inner}')
        return words

def multi_split(s: str, seps: str) -> list:
    parts = []
    part = ''
    for c in s:
        if (c in seps) and part:
            parts.append(part)
            part = ''
        else:
            part += c
    if part:
        parts.append(part)
    return parts

def sub_combos(number: str) -> list:
    sections = []
    parts = multi_split(number, '01')
    print(parts)
    for part in parts:
        sections.append(find_phrases(part))
    for (i, section) in enumerate(sections):
        if not section:
            sections[i] = parts[i]
        
    return chain(sections) if sections else []

def sanitize_number(number: str) -> str:
    return ''.join(list(filter(lambda c: c.isdigit(), number)))

def run() -> None:
    number = sanitize_number(input(prompt))
    words = sub_combos(number)
    if not words:
        print('No words found')
    else:
        for word in sorted(words):
            print(word)

if __name__ == '__main__':
    run()
##def count(rem):
##    
##    if rem < 2:
##        return rem
##    else:
##        return 2 + count(rem - 1) + count(rem - 2)


def count(rem: int) -> int:
    '''
    A short staircase consists of n steps. Sometimes you take 1 step
    at a time, sometimes 2. How many possible ways to go down the stairs
    are there?
    '''

    if rem < 2:
        return 1
    else:
        return count(rem - 1) + count(rem - 2) 
# in mac filenames, 'a_' sorts before 'a'
# in pc filenames, 'a' sorts before 'a_'
# this script takes the mac system and just renumbers files without underscores

import os
import functools

fnames = {}

for fname in list(os.walk('.'))[0][2]:
    if '.py' in fname:
        continue
    
    fnames[fname] = []

def _strcmp(a, b):
    if a < b:
        return -1
    elif b < a:
        return 1
    else:
        return 0

def _undercmp(a, b):
    a = a.split('.')[0]
    b = b.split('.')[0]
    if a.rstrip('_') == b.rstrip('_'):
        if len(a) > len(b):
            return -1
        elif len(b) > len(a):
            return 1
        else:
            return 0
    else:
        return _strcmp(a, b)

def new_fname_1(i, ext):
    return str(i) + '.' + ext

def new_fname_2(i, ext):
    return chr(i + 97) + '.' + ext

fnames_sorted = sorted(fnames, key=functools.cmp_to_key(_undercmp))
fnames_2 = {}

for (i, fname) in enumerate(fnames_sorted):
    ext = fname.split('.')[1]
    fnames[fname] = new_fname_1(i, ext)
    fnames_2[new_fname_1(i, ext)] = new_fname_2(i, ext)

for (old, new) in fnames.items():
    os.rename(old, new)

for (old, new) in fnames_2.items():
    os.rename(old, new)
import random

R = 'ROCK'
P = 'PAPER'
S = 'SCISSORS'

class Player:
    def __init__(self, name: str):
        self.name = name
        self.roll = None

    def fight(self, other):
        if self.roll == other.roll:
            return None

        if self.roll == R:
            return self if other.roll == S else other
        elif self.roll == P:
            return self if other.roll == R else other
        elif self.roll == S:
            return self if other.roll == P else other

def run():
    name = input('Your name: ').strip()
    user = Player(name)
    comp = Player('ATM')

    wins = 0
    go = ''

    while go != 'Q':
        roll = input('R/P/S: ').strip().upper()
        user.roll = eval(roll)
        comp.roll = random.choice((R, P, S))
        print('{} rolled {}'.format(comp.name, comp.roll))

        winner = user.fight(comp)
        wins += winner == user
        winner = 'Tie!' if not winner else winner.name
        print('Winner: {}'.format(winner))
        print('Your wins: {}'.format(wins))

        go = input('\\nEnter to play again, Q to quit: ').strip().upper()

if __name__ == '__main__':
    run()
    
def off_square(lower: int, distance: int) -> int:
    upper = lower + distance
    mean = lower + (distance / 2)
    return mean**2 - (lower * upper)

def test(upper: int) -> None:
    for n in range(1, upper + 1):
        for distance in range(0, 9):
            off = off_square(n, distance)
            if off != (distance / 2)**2:
                print(f'{n} * {n+(distance * 2)} is {off} less than {n+distance}^2')

test(1000)

# 16 x 16 = 0 less than 16 x 16
# 15 x 17 = 1 less than 16 x 16
# 14 x 18 = 4 less than 16 x 16
# 13 x 19 = 9 less than 16 x 16

# Moreover, even with non-integer means
# 15 x 16 = 0.25 less than 15.5 x 15.5
# 15 x 18 = 2.25 less than 16.5 x 16.5

# Square the distance from the middle #

# For any two numbers a and b, let c be their average.
# The product of any two numbers is
# equal to the square of their mean minus the square of half their range.
def any_base_to_int(n: str, base: int) -> int:
    result = 0
    mult = 1

    for i in range(len(n)):
        digit = int(n[-(i + 1)])
        result += digit * mult
        mult *= base

    return result

def vindicate_douglas_adams():
    assert 6 * 9 == any_base_to_int('42', 13)
"""

# Remove blank first and last used for formatting
REAL_WORLD_LINES = REAL_WORLD_TEXT.split('\n')[1:-1]
REAL_WORLD_LINES = list(filter(lambda L: bool(L.strip()), REAL_WORLD_LINES))
