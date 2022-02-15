from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class StepForm(FlaskForm):
    step = StringField(label='Step:', validators=[DataRequired()])
    submit = SubmitField(label='Enter')

