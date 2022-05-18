from crypt import methods
from flask import render_template, request, redirect,url_for,abort
from . import main
from ..requests import get_quotes,get_quote
from ..models import Post,User
from .forms import PostForm,UpdateProfile
from flask_login import login_required
from .. import db

# Post = post.Post


# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    popular_quotes = get_quotes('popular')
    print(popular_quotes)
    title='Home-Welcome to my blog'
    return render_template('index.html', title=title, popular=popular_quotes)


@main.route('/quote')
def quote(quote):

    '''
    View quote page function that returns the quote details page and its data
    '''
    quotes = get_quote(quote)
    author = f'{quotes.author}'
    post = Post.get_post(quotes.id)
    return render_template('quote.html', quote=quotes, post=post, author=author)

@main.route('/quotes/new', methods = ['GET','POST'])
@login_required
def new_post(id):
    form = PostForm()
    quotes = get_quote(id)

    if form.validate_on_submit():
        author = form.author.data
        quote = form.quote.data
        new_post = Post(author, quote)
        new_post.save_post()
        return redirect(url_for('quotes',id=quotes.id))

    # title = f'{movie.title} review'
    return render_template('new_post.html', post_form=form, quotes=quotes)

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile.html", user = user)

@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('update.html',form =form)