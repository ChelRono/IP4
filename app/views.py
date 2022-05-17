from crypt import methods
from flask import render_template, request, redirect,url_for
from app import app
from .request import get_quotes,get_quote
from .models import post
from .forms import PostForm
Post = post.Post


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

@app.route('/quotes/post/new/<int:id>', methods = ['GET','POST'])
def new_post(id):
    form = PostForm()
    quotes = get_quote(id)

    if form.validate_on_submit():
        author = form.author.data
        quote = form.quote.data
        new_post = Post(author, quote)
        new_post.save_post()
        return redirect(url_for('quotes'))

    # title = f'{movie.title} review'
    return render_template('new_post.html', post_form=form, quotes=quotes)