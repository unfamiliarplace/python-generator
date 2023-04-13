import requests
import os
import shutil

dir_out = './output'
if not os.path.exists(dir_out):
    os.mkdir(dir_out)

placeholder = '****'
stem = "https://ia803205.us.archive.org/BookReader/BookReaderPreview.php?id=seizeday0000bell_x5c5&subPrefix=seizeday0000bell_x5c5&itemPath=/13/items/seizeday0000bell_x5c5&server=ia803205.us.archive.org&page=leaf{placeholder}&fail=preview&&scale=1&rotate=0"

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

stem2 = "https://ia903205.us.archive.org/BookReader/BookReaderImages.php?zip=/13/items/seizeday0000bell_x5c5/seizeday0000bell_x5c5_jp2.zip&file=seizeday0000bell_x5c5_jp2/seizeday0000bell_x5c5_0008.jp2&id=seizeday0000bell_x5c5&scale=2&rotate=0"
stem2 = "id=seizeday0000bell_x5c5&scale=2&rotate=0"

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

    
