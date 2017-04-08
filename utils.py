import os
import json
from bottle import template

def reload_config(name='config.json'):
    with open(name, 'r') as file:
        config = json.loads(file.read())
    return config

CONFIG = reload_config()

def render(name, data=None):
    "Render a html template"
    global CONFIG
    template_base = CONFIG['template_base']
    # -----
    data = data if data is not None else dict()
    with open(os.path.join(template_base, name), 'r') as file:
        html = file.read()
    return template(html, **data)
