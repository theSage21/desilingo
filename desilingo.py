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

@app.get('/learn/<user>/<target>/<medium>/<level>')
def get_profile(user, target, medium, level=0):
    user = utils.get_user(user)
    level = int(level)
    return render('learn.html', {'user': user})


# --------------MAIN
@app.get('/static/<path:path>')
def static_server(path):
    return bottle.static_file(path, root='static')

if __name__ == '__main__':
    bottle.run(app, host='localhost', port=8080, debug=True)
