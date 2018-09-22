from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField
from wtforms.validators import DataRequired


class AddAuto(FlaskForm):
    autoName = StringField('Auto Name', validators=[DataRequired()])
    autoModel = StringField('Auto Model', validators=[DataRequired()])
    engine = StringField('Engine', validators=[DataRequired()])
    passengers = StringField('Passengers Max', validators=[DataRequired()])
    #sure = BooleanField('Are you sure?', validators=[DataRequired()])
    submit = SubmitField('Add')
