from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import DataRequired

class Regform(FlaskForm):
    first_name = StringField(label="Имя",validators=[DataRequired()])
    last_name = StringField(label="Фамилия",validators=[DataRequired()])
    fathers_name = StringField(label="Отчество",validators=[DataRequired()])
    date_of_brith = StringField(label="Дата рождения",validators=[DataRequired()])
    location = SelectField(label="Место рождения",choices=[(1,"Москва"),(2,"МО"), (3, "Россия")], validators=[DataRequired()])
    submit = SubmitField(label='Отправить')


