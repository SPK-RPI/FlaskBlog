from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField,ValidationError
from blogposts.models import User 
from wtforms.validators import DataRequired, Length, Email, equal_to


class RegistrationForm(FlaskForm):
    username = StringField('Username:', validators=[
        DataRequired(), Length(min=2, max=20)])
    email = StringField('Email: ', validators=[DataRequired(), Email()])
    password = PasswordField('Pssword:', validators=[DataRequired()])
    conform_password = PasswordField('Conform Password', validators=[
                                     DataRequired(), equal_to('password')])
    submit = SubmitField('Sign up')
    
    def validate_username(self,username):
            user=User.query.filter_by(username=username.data).first()
            if user:
                    raise ValidationError('That user name has been taken.Use a different one')
    
    def validate_email(self,email):
            user=User.query.filter_by(email=email.data).first()
            if user:
                    raise ValidationError('That Email has been taken.Use a different one')                

class LoginForm(FlaskForm):
    username = StringField('Username:', validators=[
        DataRequired(), Length(min=2, max=20)])
    email = StringField('Email: ', validators=[DataRequired(), Email()])
    password = PasswordField('Password:', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('LogIn')
