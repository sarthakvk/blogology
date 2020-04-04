from wtforms import StringField, SubmitField, TextAreaField, RadioField
from flask_wtf import FlaskForm
from wtforms.validators import Length

class Add(FlaskForm):

    title = StringField("Title",validators=[Length(min=1,max=25)])
    short = TextAreaField("Short description",validators=[Length(min=1,max=50)])
    breif  = TextAreaField("Content",validators=[Length(min=1)])

    submit = SubmitField("Add Blog")

class Remove(FlaskForm):


    choice = RadioField('Do you want to remove the blog?', choices=[(1,'Yes'),(0,'No')],coerce=int)
    submit = SubmitField("Submit")

class Edit(FlaskForm):

    title = StringField("Title")
    short = TextAreaField("Short description")
    breif = TextAreaField("Content")

    submit = SubmitField("Save Changes")