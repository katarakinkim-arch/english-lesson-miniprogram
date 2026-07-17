import urllib.request, urllib.parse, json, os, time
from PIL import Image

OUT = 'classroom_images_v2'
LOG = os.path.join(OUT, '_retry_log.txt')

def log(m):
    with open(LOG, 'a', encoding='utf-8') as f:
        f.write(m + '\n')
    print(m, flush=True)

def search(query, n=8):
    params = {'action':'query','generator':'search','gsrsearch':f'filetype:bitmap {query}',
        'gsrnamespace':'6','gsrlimit':str(n),'prop':'imageinfo',
        'iiprop':'url|size|mime','iiurlwidth':'1600','format':'json'}
    url = 'https://commons.wikimedia.org/w/api.php?' + urllib.parse.urlencode(params)
    req = urllib.request.Request(url, headers={'User-Agent':'EduPPTBot/1.0 (edu@example.com)'})
    with urllib.request.urlopen(req, timeout=20) as r:
        data = json.load(r)
    pages = data.get('query', {}).get('pages', {})
    out = []
    for p in pages.values():
        ii = p.get('imageinfo', [{}])[0]
        if ii.get('mime') in ('image/jpeg','image/png') and ii.get('width', 0) >= 700:
            out.append({'title':p.get('title'),'thumb':ii.get('thumburl')})
    return out

def download(url, path, tries=5):
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
            last = e; time.sleep(3)
    raise last

targets = {
 'orange_isle':['Orange Isle Changsha','Juzizhou Changsha','Changsha Xiang River island'],
 'autumn_forest':['autumn forest colorful trees','fall foliage forest','autumn woodland path'],
 'mao':['Mao Zedong 1927','Mao Zedong 1930s','Mao Zedong portrait'],
}
for key, qs in targets.items():
    done = False
    for q in qs:
        try:
            res = search(q)
        except Exception as e:
            log(f'{key}: search err {e}'); continue
        if res:
            top = res[0]
            try:
                path = os.path.join(OUT, f'{key}.jpg')
                sz = download(top['thumb'], path)
                Image.open(path).verify()
                log(f'OK {key}: {top["title"]} -> {sz}B')
                done = True; break
            except Exception as e:
                log(f'{key}: dl err {e}')
    if not done:
        log(f'FAIL {key}')
log('===RETRY DONE===')
