from flask import render_template
from app import app

#views
@app.route('/')
def index():
    '''
    view root page function that returns the index page
    '''
    title = 'GET YOUR NEWS'
    return render_template('index.html',title = title) 