# https://github.com/vookimedlo/alfred-slugify

import sys
import json
from slugify import slugify

txt = sys.argv[1]
alfreditems = {"items": []}


def create_alfred_item(alfred_items, uid, title, subtitle, autocomplete, arg):
    alfred_items['items'].append({
        "uid": uid,
        "title": title,
        "subtitle": subtitle,
        "autocomplete": autocomplete,
        "arg": arg,
    })


slug = slugify(txt)

if slug != "":
    create_alfred_item(alfreditems,
                       "1",
                       slug,
                       "Press Enter to copy a result to the clipboard.",
                       True,
                       slug)
else:
    create_alfred_item(alfreditems,
                       "1",
                       "",
                       "No output for the given text.",
                       True,
                       "")

dump = json.dumps({'items': alfreditems['items']}, indent=4)
sys.stdout.write(dump)
