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

def user_exists(user):
    with dataset.connect(DB_STRING) as db:
        users = db['Users']
        existing_user = users.find_none(nick=user)
    return existing_user is not None

def create_user(user):
    with dataset.connect(DB_STRING) as db:
        users = db['Users']
        users.insert({'nick': user})

def get_question(level):
    with dataset.connect(DB_STRING) as db:
        questions = db['question']
        q = questions.find_one(level=level)
    return q

def translate(text, target):
    # TODO
    return text
