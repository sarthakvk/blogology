from wtforms import StringField, SubmitField, TextAreaField, RadioField
from wtforms.fields.html5 import DateField
from flask_wtf import FlaskForm
from wtforms.validators import Length,InputRequired

class Add(FlaskForm):

    title = StringField("Title",validators=[Length(min=1,max=25),InputRequired()])
    short = TextAreaField("Short description",validators=[Length(min=1,max=50),InputRequired()])
    breif  = TextAreaField("Content",validators=[Length(min=1),InputRequired()])
    dat = DateField("Date", format='%Y-%m-%d',validators=[InputRequired()])

    submit = SubmitField("Add Blog")

class Remove(FlaskForm):


    choice = RadioField('Do you want to remove the blog?', choices=[(1,'Yes'),(0,'No')],coerce=int)
    submit = SubmitField("Submit")

class Edit(FlaskForm):

    title = StringField("Title",validators=[Length(min=1,max=25),InputRequired()])
    short = TextAreaField("Short description",validators=[Length(min=1,max=50)])
    breif = TextAreaField("Content",validators=[Length(min=1),InputRequired()])
    dat = DateField("Date", format="%Y-%m-%d",validators=[InputRequired()])


    submit = SubmitField("Save Changes")