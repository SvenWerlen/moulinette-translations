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
    translations=json.loads(f.read())

  # write translations
  with open("%s/%s.json" % (os.path.dirname(__file__), transISO), 'w') as f:
    json.dump(translations, f, indent = 2, sort_keys=True, ensure_ascii=False)
