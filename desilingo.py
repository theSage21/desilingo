import bottle
from utils import render

app = bottle.Bottle()

# ----------routes
@app.get('/')
def home():
    return render('home.html')

@app.get('/<target>/<medium>')
def learn_language(target, medium):
    return render('learn.html')

if __name__ == '__main__':
    bottle.run(app, host='localhost', port=8080, debug=True)
