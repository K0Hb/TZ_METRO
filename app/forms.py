from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import DataRequired

class Regform(FlaskForm):
    first_name = StringField("Имя",validators=[DataRequired()])
    last_name = StringField("Фамилия",validators=[DataRequired()])
    fathers_name = StringField("Отчество",validators=[DataRequired()])
    date_of_brith = StringField("Дата рождения",validators=[DataRequired()])
    location = SelectField("Место рождения",validators=[DataRequired()])
    submit = SubmitField('Отправить')


