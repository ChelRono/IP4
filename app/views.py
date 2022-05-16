from crypt import methods
from flask import render_template, request
from app import app
from .request import get_quotes,get_quote
from .models import 
from .forms import QuoteForm
Review = review.Review


# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    random_quotes = get_quotes('random')
    print(random_quotes)
    title='Home-Welcome to my blog'
    return render_template('index.html', title=title, random=random_quotes)


@app.route('/quote')
def quote(quote):

    '''
    View quote page function that returns the quote details page and its data
    '''
    quotes = get_quote(quote)
    return render_template('quote.html', quote=quotes)