import sys
from playwright.sync_api import sync_playwright
ART = '''<g opacity=".55" fill="#5AB0FF"><path d="M256 250 L60 150 L60 210 Z"/><path d="M256 250 L452 150 L452 210 Z"/><path d="M256 250 L90 70 L130 60 Z" opacity=".6"/><path d="M256 250 L422 70 L382 60 Z" opacity=".6"/></g>
<path d="M156 340 V250 a100 100 0 0 1 200 0 V340 Z" fill="url(#aD)"/><path d="M176 250 a80 80 0 0 1 60 -77" stroke="#fff" stroke-width="14" fill="none" stroke-linecap="round" opacity=".55"/>
<text x="256" y="320" text-anchor="middle" font-family="Inter,system-ui,sans-serif" font-weight="900" font-size="150" fill="#fff">?</text>
<rect x="124" y="340" width="264" height="54" rx="14" fill="#E9EEF5"/><rect x="124" y="372" width="264" height="22" rx="8" fill="#B9C4D3"/>'''
DEFS = '''<defs><radialGradient id="aG" cx="50%" cy="42%" r="60%"><stop offset="0" stop-color="#1B3E78"/><stop offset="1" stop-color="#0A1830"/></radialGradient><linearGradient id="aD" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#7CC4FF"/><stop offset="1" stop-color="#1F6FE0"/></linearGradient></defs>'''
def svg(rx, scale=1.0):
    t = 256*(1-scale)
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512">{DEFS}<rect width="512" height="512" rx="{rx}" fill="url(#aG)"/><g transform="translate({t} {t}) scale({scale})">{ART}</g></svg>'
out = sys.argv[1]
open(out+'/favicon.svg','w').write(svg(112))
jobs = [('icon-192.png',192,svg(112)),('icon-512.png',512,svg(112)),('icon-512-maskable.png',512,svg(0,.78)),('apple-touch-icon.png',180,svg(0,.92))]
with sync_playwright() as p:
    b = p.chromium.launch()
    for name,size,s in jobs:
        pg = b.new_page(viewport={'width':size,'height':size})
        pg.set_content(f'<html><body style="margin:0;background:transparent">{s.replace("<svg ", f"<svg width={size} height={size} ")}</body></html>')
        pg.screenshot(path=f'{out}/{name}', omit_background=True)
        pg.close()
    b.close()
print('icons ok')
