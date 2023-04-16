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

prompt = """Enter here:"""

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
