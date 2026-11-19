"""Build ../index.html: a single self-contained page with every image embedded once.

Edit src/index.html (it loads images from src/assets/), then run:  python3 src/build.py
"""
import base64, json, re, pathlib
here = pathlib.Path(__file__).parent
src = (here / 'index.html').read_text()
keys = sorted(set(re.findall(r'assets/([\w-]+)\.jpg', src)))
data = {k: 'data:image/jpeg;base64,' + base64.b64encode((here / 'assets' / f'{k}.jpg').read_bytes()).decode() for k in keys}
out = re.sub(r'src="assets/([\w-]+)\.jpg"', r'data-asset="\1"', src)
out = re.sub(r'data-img="assets/([\w-]+)\.jpg"', r'data-img-asset="\1"', out)
boot = ('<script>(function(){var A=' + json.dumps(data) + ';'
        'document.querySelectorAll("[data-asset]").forEach(function(el){el.src=A[el.dataset.asset];});'
        'document.querySelectorAll("[data-img-asset]").forEach(function(el){el.dataset.img=A[el.dataset.imgAsset];});'
        '})();</script>\n')
out = out.replace('<script>\n(() => {', boot + '<script>\n(() => {', 1)
assert 'assets/' not in out, 'unresolved asset path'
(here.parent / 'index.html').write_text(out)
print(f'{len(keys)} images, {len(out)/1e6:.2f} MB -> index.html')
