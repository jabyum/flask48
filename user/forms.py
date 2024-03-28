from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, \
    EmailField, SubmitField

from wtforms.validators import DataRequired


# Форма для регистрации
class RegisterForm(FlaskForm):
    name = StringField('Имя', validators=[DataRequired('Заполните имя!')])
    email = EmailField('Email', validators=[DataRequired('Заполните Email!')])
    password = PasswordField('Пароль', validators=[DataRequired('Заполните Пароль!')])
    confirm_password = PasswordField('Подтвержения Пароль', validators=[DataRequired('Заполните Пароль еще раз!')])
    button = SubmitField('Зарегаться')


# Форма для логина
class LoginForm(FlaskForm):
    email = EmailField('Email', validators=[DataRequired('Заполните Email!')])
    password = PasswordField('Пароль', validators=[DataRequired('Заполните Пароль!')])

    button = SubmitField('Войти')