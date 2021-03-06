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

@app.get('/learn/<nickname>/<target>/<medium>/<level>')
def learning(nickname, target, medium, level):
    level = int(level)
    target_question, medium_question, target_answer, medium_answer, links = utils.get_level_data(level, target, medium)
    data = {'nickname': nickname,
            'target': target,
            'medium': medium,
            'nextlevel': level + 1,
            'target_question': target_question,
            'medium_question': medium_question,
            'target_answer': target_answer,
            'medium_answer': medium_answer,
            'links': links
            }
    return render('learn.html', data)

# --------------MAIN
@app.get('/static/<path:path>')
def static_server(path):
    return bottle.static_file(path, root='static')

if __name__ == '__main__':
    bottle.run(app, host='localhost', port=8080, debug=True)
