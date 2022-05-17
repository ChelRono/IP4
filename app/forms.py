from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import DataRequired

class PostForm(FlaskForm):

    author = StringField('Author',validators=[DataRequired()])
    quote = TextAreaField('Quote', validators=[DataRequired()])
    submit = SubmitField('Submit')