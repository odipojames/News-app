from flask import render_template
from .request import get_source
from app import app

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    source=get_source()
    print(source)
    title = 'Home - Welcome to The best news highlighter Website Online'
    return render_template('index.html', title = title,source = source)
