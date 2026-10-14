#!/usr/bin/env python3
"""Create one self-contained A4 HTML audit from approved report data."""
import argparse,base64,html,json,mimetypes
from pathlib import Path
from urllib.parse import urlsplit,urlunsplit,parse_qsl,urlencode

def uri(path):
    path=Path(path)
    mime=mimetypes.guess_type(path)[0] or 'application/octet-stream'
    return 'data:'+mime+';base64,'+base64.b64encode(path.read_bytes()).decode()

def booking_url(data):
    """Tag booking links while preserving their existing query and fragment."""
    parts=urlsplit(data.get('booking_url','https://hapy.co/get-started/'))
    if parts.scheme not in ('https','http') or not parts.netloc:
        raise ValueError('booking_url must be an absolute HTTP(S) URL')
    domain=data['domain'].strip().lower()
    domain=urlsplit(domain if '://' in domain else '//'+domain).hostname or domain
    if domain.startswith('www.'): domain=domain[4:]
    params=dict(parse_qsl(parts.query,keep_blank_values=True))
    params.update(utm_source='website-audit',utm_medium='report',utm_campaign='website-audit',utm_content=domain)
    return urlunsplit((parts.scheme,parts.netloc,parts.path,urlencode(params),parts.fragment))

def render(data,package):
    css=(package/'assets/audit.css').read_text()
    for key,file in [('FONT_HEADING','heading.woff2'),('FONT_BODY','body.woff2'),('FONT_SCORE','score-bold.woff2')]:
        css=css.replace('{{'+key+'}}',base64.b64encode((package/'assets'/file).read_bytes()).decode())
    tagged_booking_url=html.escape(booking_url(data),quote=True)
    pages=[]
    for i,p in enumerate(data['pages'],1):
        body=p['body'].replace('{{BOOKING_URL}}',tagged_booking_url) # Approved HTML content. Do not pass untrusted page HTML here.
        for key,path in data.get('images',{}).items(): body=body.replace('{{IMG_'+key+'}}',uri(path))
        body=body.replace('{{ASSET_HAMID}}',uri(package/'assets/hamid.webp'))
        logo=(package/'assets/hapy-logo.svg').read_text(); logo=logo[logo.index('<svg'):].replace('width="100%" height="100%"','width="104" height="32"')
        brand = logo if i in (1,len(data['pages'])) else ('<span>'+html.escape('Design review' if i==2 else 'Technical review')+'</span>')
        section = '' if i == 1 else '<p class="section-name">'+html.escape(p['section'])+'</p>'
        heading = '<h1>'+p['title']+'</h1>'
        if i == 1 and data.get('assessment'):
            score=data['assessment']
            score_class='assessment assessment--attention' if float(score['value'])/float(score['maximum']) < 0.8 else 'assessment'
            heading='<div class="opening-row">'+heading+'<aside class="'+score_class+'" aria-label="Hapy assessment '+html.escape(str(score['value']))+' out of '+html.escape(str(score['maximum']))+'"><strong>'+html.escape(str(score['value']))+'<small>/'+html.escape(str(score['maximum']))+'</small></strong></aside></div>'
        pages.append(f'''<article class="page" aria-label="Page {i}"><header class="brand">{brand}<span>Website audit / {i} · {html.escape(data['domain'])}</span></header><div class="page-head">{section}{heading}{('<p class="lede">'+html.escape(p['lede'])+'</p>') if p.get('lede') else ''}</div>{body}<footer class="footer"><span>{html.escape(p['section']+' / '+data['date'])}</span><span>{i} / {len(data['pages'])}</span></footer></article>''')
    out=(package/'templates/audit.html').read_text()
    for key,val in {'TITLE':html.escape(data['client']+' website audit | Hapy Co'),'CLIENT':html.escape(data['client']),'CSS':css,'PAGES':''.join(pages)}.items(): out=out.replace('{{'+key+'}}',val)
    if '{{IMG_' in out: raise ValueError('Unresolved screenshot placeholder')
    return out

if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--data',required=True);parser.add_argument('--output',required=True);args=parser.parse_args()
    package=Path(__file__).resolve().parents[1]
    Path(args.output).write_text(render(json.loads(Path(args.data).read_text()),package))
