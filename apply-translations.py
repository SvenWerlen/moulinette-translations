#!/usr/bin/python3
import os
import json
import re
import subprocess

TRANSLATIONS = ["en", "fr", "ja"]

COMMAND = "find -type f \( -name \"*.hbs\" -o -name \"*.js\" \) -exec grep \"mtte\.\" {} \;"

for transISO in TRANSLATIONS:

  # read translations
  with open("%s/%s.json" % (os.path.dirname(__file__), transISO), 'r') as f:
    tr=json.loads(f.read())

  translations = {}

  output = subprocess.getoutput(COMMAND)
  matches = re.findall("(mtte\.[\w.-]+)", output, flags=0)

  for key in matches:
    if key in tr:
      translations[key] = tr[key]
    else:
      print("Translation %s not found: %s" % (transISO, key))

  # write translations
  with open('lang/%s.json' % transISO, 'w') as f:
    json.dump(translations, f, indent = 2, sort_keys=True)
