from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import DataRequired

class PostForm(FlaskForm):

    Author = StringField('Author',validators=[DataRequired()])
    Quote = TextAreaField('Quote', validators=[DataRequired()])
    submit = SubmitField('Submit')