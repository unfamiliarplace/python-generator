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
    f.write('# no words\n')
    for length in sorted(no_words.keys()):
        for word in sorted(no_words[length]):
            f.write(word + '\n')
    f.write('\n# yes words\n')
    for length in sorted(yes_words.keys()):
        for word in sorted(yes_words[length]):
            f.write(word + '\n')

