#!/usr/bin/env python3
"""
Builds wedding-invite.html from wedding-builder.html.

The guest page must draw the invitation exactly as the couple saw it in
the builder, so everything visual is copied from the builder rather than
kept by hand in two places: the invitation stylesheet, the designs, the
border ornaments and their loader, the fades, and the colour maths.

Run it again whenever you change any of those in the builder:
    python3 tools/build-invite.py
"""
import re, sys, pathlib
root = pathlib.Path(__file__).resolve().parent.parent
b = (root/'wedding-builder.html').read_text(encoding='utf-8')
js = b.split('<script>')[1].split('</script>')[0]
css = b.split('<style>')[1].split('</style>')[0]

def block(start, end_pat=r'\n\};', src=js):
    i = src.index(start)
    m = re.compile(end_pat).search(src, i)
    if not m: sys.exit(f'could not find the end of: {start}')
    return src[i:m.end()]

MARK = '/* ═══════════════════════════════════════════════════════════\n   INVITATION'
inv_css = css[css.index(MARK):]
img_rule = re.search(r'\.inv \.bord\.corner i img\{[^}]*\}', css).group(0)

shared = '\n\n'.join([
  block('const FADES = {'),
  block('const OVERLAYS = {'),
  block('const ARTWORKS = [', r'\n\];'),
  block('const BORDERS = {'),
  block('const VEC = {'),
  block('function prepareSvg(txt, key){', r'\n\}\n'),
  js[js.index('const hx = h =>'):js.index('\n', js.index('const contrast = '))],
  block('function artUrl(a, w){', r'\n\}\n'),
  js[js.index('const ART_RATIO = {};'):js.index('\n', js.index('const artById = '))],
  js[js.index('const HEART = '):js.index(';\n', js.index('const HEART = '))+1],
])
# in the builder these follow the builder's own state; here they follow the wedding
shared = shared.replace('state.artwork', '(cfg && cfg.artwork)')
# a guest only needs the one design the couple picked, not all ten
OWN_LOOP = 'ARTWORKS.concat(OWN_ART() ? [artById("own")] : []).forEach(a=>{'
if OWN_LOOP not in shared: sys.exit('could not find the design loop in loadArtworkSizes')
shared = shared.replace(OWN_LOOP, 'ARTWORKS.concat(OWN_ART() ? [artById("own")] : []).filter(a => a.id === (cfg && cfg.artwork)).forEach(a=>{', 1)

fonts = re.search(r'<link href="https://fonts\.googleapis\.com/css2\?[^"]+" rel="stylesheet">', b).group(0)
fonts = re.sub(r'family=Manrope[^&]*&', '', fonts)
fonts = re.sub(r'family=IBM\+Plex\+Sans\+Arabic[^&]*&', '', fonts)

tpl = (root/'tools'/'invite-template.html').read_text(encoding='utf-8')
out = (tpl.replace('/*@@FONTS@@*/', fonts)
          .replace('/*@@INV_CSS@@*/', inv_css)
          .replace('/*@@IMG_RULE@@*/', img_rule)
          .replace('/*@@SHARED_JS@@*/', shared))
(root/'wedding-invite.html').write_text(out, encoding='utf-8')
print(f'wrote wedding-invite.html ({len(out)//1024} KB)')
