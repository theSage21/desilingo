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

@app.get('/about')
def about():
    return render('about.html')

@app.get('/start')
def start():
    return render('start.html')

@app.get('/<user>/')
def get_profile(user):
    user = utils.get_user(user)
    return render('profile.html', {'user': user})

@app.get('/<user>/learn')
def user_revision(user):
    user = utils.get_user(user)
    return render('revision.html', {'user': user})

@app.get('/<level>/add')
def add_question(level):
    question = bottle.request.json.get('question')
    answer = bottle.request.json.get('answer')
    support = bottle.request.json.get('support')

@app.get('/static/<path:path>')
def static_server(path):
    return bottle.static_file(path, root='static')

# --------------MAIN
if __name__ == '__main__':
    bottle.run(app, host='localhost', port=8080, debug=True)
