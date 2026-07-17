import urllib.request, urllib.parse, json, os, sys, time
from PIL import Image

OUT = 'classroom_images_v2'
os.makedirs(OUT, exist_ok=True)
LOG = 'classroom_images_v2/_download_log.txt'

def log(msg):
    with open(LOG, 'a', encoding='utf-8') as f:
        f.write(msg + '\n')
    print(msg, flush=True)

def search_commons(query, n=8):
    params = {'action':'query','generator':'search','gsrsearch':f'filetype:bitmap {query}',
        'gsrnamespace':'6','gsrlimit':str(n),'prop':'imageinfo',
        'iiprop':'url|size|mime','iiurlwidth':'1600','format':'json'}
    url = 'https://commons.wikimedia.org/w/api.php?' + urllib.parse.urlencode(params)
    req = urllib.request.Request(url, headers={'User-Agent':'EduPPTBot/1.0 (edu@example.com)'})
    with urllib.request.urlopen(req, timeout=12) as r:
        data = json.load(r)
    pages = data.get('query', {}).get('pages', {})
    out = []
    for p in pages.values():
        ii = p.get('imageinfo', [{}])[0]
        if ii.get('mime') in ('image/jpeg','image/png') and ii.get('width', 0) >= 700:
            out.append({'title':p.get('title'),'thumb':ii.get('thumburl')})
    return out

def download(url, path, tries=4):
    last = None
    for i in range(tries):
        try:
            req = urllib.request.Request(url, headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
            with urllib.request.urlopen(req, timeout=60) as r:
                data = r.read()
            with open(path, 'wb') as f:
                f.write(data)
            return len(data)
        except Exception as e:
            last = e
            time.sleep(2)
    raise last

targets = {
 'orange_isle':['Orange Isle Changsha Juzizhou'],
 'red_mountains':['autumn mountains red maple foliage','red leaves mountain autumn','maple forest autumn'],
 'green_river':['Li River Guilin landscape','turquoise river canyon','green river aerial'],
 'eagle':['bald eagle flying sky','golden eagle flying'],
 'fish':['fish underwater clear','rainbow trout stream','koi fish pond'],
 'boats':['sailboats regatta river','junks river China','fishing boats river'],
 'mao':['Mao Zedong 1927','Mao Zedong portrait','Mao Zedong'],
 'rapids':['white water rapids river','river rapids','Niagara rapids'],
 'autumn_forest':['autumn forest colorful trees','autumn woodland'],
}

log('START ' + time.strftime('%H:%M:%S'))
for key, qs in targets.items():
    done = False
    for q in qs:
        try:
            res = search_commons(q)
        except Exception as e:
            log(f'{key}: search err {e}')
            continue
        if res:
            top = res[0]
            try:
                path = os.path.join(OUT, f'{key}.jpg')
                sz = download(top['thumb'], path)
                im = Image.open(path); im.verify()
                log(f'OK {key}: {top["title"]} -> {im.size[0]}x{im.size[1]} {sz}B')
                done = True
                break
            except Exception as e:
                log(f'{key}: dl err {e}')
    if not done:
        log(f'FAIL {key}: all queries exhausted')
log('===DONE===')
