from utils import render
from bottle import route, run, request, redirect, get, post, Bottle, template

app = Bottle()

# ----------routes
@app.get('/')
def home():
    return render('home.html')

if __name__ == '__main__':
    run(app, host='localhost', port=8080, debug=True)
