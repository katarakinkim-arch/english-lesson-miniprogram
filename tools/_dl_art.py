import urllib.request, urllib.parse, json, os, time
from PIL import Image

OUT = 'classroom_images_v2'

def get_thumb(title, width=1400):
    params = {'action':'query','titles':title,'prop':'imageinfo',
              'iiprop':'url|size|mime','iiurlwidth':str(width),'format':'json'}
    url = 'https://commons.wikimedia.org/w/api.php?' + urllib.parse.urlencode(params)
    req = urllib.request.Request(url, headers={'User-Agent':'EduPPTBot/1.0 (edu@example.com)'})
    with urllib.request.urlopen(req, timeout=30) as r:
        d = json.load(r)
    p = list(d['query']['pages'].values())[0]
    return p['imageinfo'][0].get('thumburl','')

def download(url, path, retries=5):
    for i in range(retries):
        try:
            req = urllib.request.Request(url, headers={'User-Agent':'Mozilla/5.0'})
            with urllib.request.urlopen(req, timeout=60) as r:
                data = r.read()
            with open(path, 'wb') as f:
                f.write(data)
            im = Image.open(path); im.verify()
            im2 = Image.open(path)
            print(f'OK {os.path.basename(path)}: {im2.size[0]}x{im2.size[1]}, {len(data)//1024}KB')
            return True
        except Exception as e:
            print(f'retry {i} for {path}: {e}')
            time.sleep(3)
    return False

# Primary: Xiao-Xiang rivers Chinese painting (artwork, not photo)
u1 = get_thumb('File:Xiao and Xiang rivers.jpg')
print('URL1:', u1)
download(u1, os.path.join(OUT, 'mao_art.jpg'))

# Backup: Mao poem mural (artwork, text of his poem)
try:
    u2 = get_thumb('File:Peking Wandbild Mao Gedicht-20131230-RM-112409.jpg')
    print('URL2:', u2)
    download(u2, os.path.join(OUT, 'mao_mural.jpg'))
except Exception as e:
    print('mural search failed:', e)

print('===DONE===')
