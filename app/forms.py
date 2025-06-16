from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField
from wtforms.validators import DataRequired

class SymptomForm(FlaskForm):
    description = TextAreaField("Describe your symptoms", validators=[DataRequired()])
    submit = SubmitField("Check")
    
