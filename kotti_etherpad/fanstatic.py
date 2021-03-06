# -*- coding: utf-8 -*-

from __future__ import absolute_import

from fanstatic import Group
from fanstatic import Library
from fanstatic import Resource

from kotti.fanstatic import view_needed


library = Library("kotti_etherpad", "static")
kotti_etherpad_css = Resource(library,
    "kotti_etherpad.css",
    minified='kotti_etherpad.min.css',
    bottom=True)
kotti_etherpad_js = Resource(library,
    "kotti_etherpad.js",
    minified='kotti_etherpad.min.js',
    bottom=True)
view_needed.add(Group([kotti_etherpad_css,
                       kotti_etherpad_js, ]))
