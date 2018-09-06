"""
Core Hyperpython API
"""
__version__ = '0.3.0'
__author__ = 'Fábio Macêdo Mendes'

# Ugly hack to make it possible to store __version__ directly on __init__.py
try:
    from .core import Element, Text, Block
    from .html import html, render
    from .tags import (
        HTML5, h,
        body, head, meta, link, title, div, span, article, aside, details, footer,
        figcaption, figure, header, main, p, pre, section, embed, iframe, noscript,
        object_, script, style, button, fieldset, form, input_, keygen, label,
        legend, optgroup, option, select, textarea, h1, h2, h3, h4, h5, h6, dd, dl,
        dt, ul, li, ol, area, audio, canvas, img, picture, track, video, source, a,
        menu, menuitem, nav, abbr, blockquote, code, caption, col, colgroup, table,
        tbody, td, tfoot, th, thead, tr, b, em, del_, i, ins, mark, q, s, small,
        strong, sub, sup, u, br, hr, wbr, bdi, bdo, rp, rt, ruby, address, dialog,
        base, cite, datalist, dfn, kbd, map_, meter, param, progress, samp, summary,
        time, var, output, acronym, applet, big, basefont, center, dir_, font,
        frame, frameset, noframes, strike, tt
    )
    from .utils import escape, unescape, safe, sanitize
    from .fragment import fragment
    from .helpers import classes
except ImportError as exc:
    print('Caught exception:', exc)
    print('This is expected during installation.')
