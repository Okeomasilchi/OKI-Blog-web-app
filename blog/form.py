from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from blog.models import User


class Regfrom(FlaskForm):
    uname = StringField('Username',
                        validators=[DataRequired(), Length(min=2, max=21)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(),])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_uname(self, field):
        user = User.query.filter_by(uname=field.data).first()
        if user:
            raise ValidationError(f"The user name {field.data} already Exist")

    def validate_email(self, field):
        email = User.query.filter_by(email=field.data).first()
        if email:
            raise ValidationError(f"{field.data} already in use by another user")


class Loginfrom(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(),])
    remember = BooleanField('Remeber Me')
    submit = SubmitField('Login')