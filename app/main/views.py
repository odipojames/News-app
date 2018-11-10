from flask import render_template,request,redirect,url_for
# from app import app
from .import main
from ..request import get_source,get_article,get_category


@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    source=get_source()
    print(source)
    title = 'Home - Welcome to The best news highlighter Website Online'
    return render_template('index.html', title = title,source = source)


   #route to the articles.html page
@main.route('/article/<article_id>')
def article(article_id):
    '''
    function that returns the article.html page and its contect
    '''
    article = get_article(article_id)
    print(article)
    title = f'{article_id}'
    return render_template('article.html',id = article_id,title = title,article = article)

@main.route('/category/<cat_name>')
def category(cat_name):
    '''
    function to return the category.html page and its content
    '''
    category = get_category(cat_name)
    print (category)
    title = f'{cat_name}'
    return render_template('category.html',title = title, category = category)
