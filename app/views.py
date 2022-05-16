from crypt import methods
from flask import render_template
from app import app
from .request import get_quotes

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    popular_quotes = get_quotes('popular')
    print(popular_quotes)
    title='Home-Welcome to my blog'
    return render_template('index.html', title=title, popular=popular_quotes)

@app.route('/quote/<quote_id>')
def quote(id):

    '''
    View quote page function that returns the quote details page and its data
    '''
    quotes = get_quotes(id)
    return render_template('quote.html',id = quotes)