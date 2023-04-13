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
