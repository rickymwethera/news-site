from flask import render_template,request,redirect,url_for
from . import main
from ..request import get_news,get_articles


# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    #getting floods news
  
    title='HOMEPAGE'
    
    news=get_news('general')
    
    
    
    search_news = request.args.get('news_query')

    if search_news:
        return redirect(url_for('main.search',query=search_news))
    else:
        return render_template('index.html',title = title,news=news)

@main.route('/sources/<id>')
def articles(id):
	'''view function that returns the articles page'''
	articles =get_articles(id)
	return render_template('articles.html',articles = articles)

