"""Writes manifest, sw.js (versioned cache), README; rebuilds data.js with version."""
import hashlib, json, subprocess, sys, os
app = sys.argv[1]
subprocess.run(['python3', 'build_data.py', os.path.join(app, 'data.js'), 'tmp'], check=True, capture_output=True)
h = hashlib.sha1()
for f in ['app.js', 'app.css', 'index.html', 'data.js']:
    h.update(open(os.path.join(app, f), 'rb').read())
ver = '1.0.' + h.hexdigest()[:7]
subprocess.run(['python3', 'build_data.py', os.path.join(app, 'data.js'), ver], check=True)
json.dump({
  "name": "Status 3 · Notfallmedizin-Trainer", "short_name": "Status 3", "start_url": "./index.html", "scope": "./",
  "display": "standalone", "orientation": "portrait", "background_color": "#0A1830", "theme_color": "#0A1830", "lang": "de",
  "description": "Gamifizierter Fragentrainer Notfallmedizin: 200 Fragen in 7 Typen, Boss-Einsätze, Blitzrunde, Sichtungssprint und Duell NA vs. NotSan.",
  "icons": [{"src": "icon-192.png", "sizes": "192x192", "type": "image/png", "purpose": "any"},
            {"src": "icon-512.png", "sizes": "512x512", "type": "image/png", "purpose": "any"},
            {"src": "icon-512-maskable.png", "sizes": "512x512", "type": "image/png", "purpose": "maskable"}]
}, open(os.path.join(app, 'manifest.webmanifest'), 'w'), ensure_ascii=False, indent=2)
assets = ['./', './index.html', './app.css', './app.js', './data.js', './manifest.webmanifest', './favicon.svg',
          './icon-192.png', './icon-512.png', './icon-512-maskable.png', './apple-touch-icon.png']
open(os.path.join(app, 'sw.js'), 'w').write(f"""const CACHE='status3-{ver}';
const ASSETS={json.dumps(assets)};
self.addEventListener('install',e=>{{e.waitUntil(caches.open(CACHE).then(c=>c.addAll(ASSETS)).then(()=>self.skipWaiting()));}});
self.addEventListener('activate',e=>{{e.waitUntil(caches.keys().then(ks=>Promise.all(ks.filter(k=>k!==CACHE).map(k=>caches.delete(k)))).then(()=>self.clients.claim()));}});
self.addEventListener('fetch',e=>{{if(e.request.method!=='GET')return;e.respondWith(caches.match(e.request,{{ignoreSearch:true}}).then(r=>r||fetch(e.request).then(res=>{{if(res.ok&&new URL(e.request.url).origin===location.origin){{const c=res.clone();caches.open(CACHE).then(x=>x.put(e.request,c));}}return res;}}).catch(()=>caches.match('./index.html'))));}});
""")
open(os.path.join(app, '.nojekyll'), 'w').write('')
print('version', ver)
