#!/usr/bin/env python3
"""
Copyright (C) 2016 alchimista alchimistawp@gmail.com
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.
This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

import requests

editors = {}
meta_conflit = []
BASENAME = "http://wikimedia.pt/"

_url = "{}api.php?action=query&list=allusers&aulimit=50&format=json".format(BASENAME)
f = open('users.txt', 'r+')
r = requests.get(_url)
s = r.json()
for z in s['query']['allusers']:
    i = z['name'].replace(" ", "_")
    _url = "{0}api.php?action=query&list=usercontribs&format=json&ucuser={1}".format(BASENAME, i)
    r = requests.get(_url)
    data = r.json()

    if not data["query"]['usercontribs']:
        editors[i] = {"pt_wm_edits": False, "meta": None}
    else:

        _url = "https://meta.wikimedia.org/w/api.php?action=query&list=usercontribs&format=json&ucuser={}".format(i)
        r = requests.get(_url)
        account_meta = r.json()
        if account_meta['query']['usercontribs']:
            editors[i] = {"pt_em_edits": True, "meta": True}
        else:
            editors[i] = {"pt_wm_edits": True, "meta": False}
            meta_conflit.append(i)
            f.write(i + "\n")

print(editors)
print(meta_conflit)
