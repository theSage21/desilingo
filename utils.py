import os
import json
from googletrans import Translator
from bottle import template

############ CONFIG LOADING #############
def reload_config(name='config.json'):
    with open(name, 'r') as file:
        config = json.loads(file.read())
    return config

CONFIG = reload_config()

############ OTHER FUNCTIONS #############
def render(name, data=None):
    "Render a html template"
    global CONFIG
    template_base = CONFIG['template_base']
    # -----
    data = data if data is not None else dict()
    with open(os.path.join(template_base, name), 'r') as file:
        html = file.read()
    return template(html, **data)


def get_level_data(level, target, medium):
    t_q = 'target question'
    m_q = 'medium question'
    t_a = 'target answer'
    m_a = 'medium answer'
    links = ['google.com']
    return t_q, m_q, t_q, m_a, links
