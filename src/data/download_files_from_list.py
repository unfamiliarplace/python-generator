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
