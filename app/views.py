from flask import render_template,request,redirect,url_for
from app import app
from .request import get_news

#views
@app.route('/')
def index():
    '''
    view root page function that returns the index page
    '''
    title = 'GET YOUR NEWS'
    news = get_news('general')
    return render_template('index.html',title = title, news = news) 

    #getting news
