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
