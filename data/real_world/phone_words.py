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

