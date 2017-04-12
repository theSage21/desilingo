import bottle
import utils
import dataset


render = utils.render
app = bottle.Bottle()
DB_STRING = 'sqlite:///desilingo.sqlite3'

# ----------routes
@app.get('/')
def home():
    return render('home.html')

@app.get('/<user>/<target>/<medium>/<level>/<item>')
def learn_language(user, target, medium, level):
    question = utils.get_question(level, item)
    return render('learn.html')

@app.get('/<user>/add')
def add_user(user):
    report = None
    with dataset.connect(DB_STRING) as db:
        users = db['Users']
        existing_user = users.find_none(nick=user)
        if existing_user is None:
            users.insert({'nick': user})
            report = 'User added'
        else:
            report = 'User already exists'
    return {'report': report}



        

if __name__ == '__main__':
    bottle.run(app, host='localhost', port=8080, debug=True)
