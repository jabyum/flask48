from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, EmailField, SubmitField
from wtforms.validators import DataRequired


# Форма для добавления
class QuestionForm(FlaskForm):
    username = StringField('Имя', validators=[DataRequired('Заполните имя')])
    title = StringField('Тема', validators=[DataRequired('Заполните тему')])
    question = TextAreaField('Коммент', validators=[DataRequired('Заполните коммент')])
    button = SubmitField('Отправить')
