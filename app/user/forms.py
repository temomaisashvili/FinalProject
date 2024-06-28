from flask_wtf import FlaskForm
from wtforms.fields.numeric import IntegerField
from wtforms.fields.simple import EmailField, PasswordField, SubmitField, StringField
from wtforms.validators import data_required, email




class LoginForm(FlaskForm):

    email = EmailField('Email', validators=[data_required(), email()],
                       render_kw={'placeholder': 'შეიყვანეთ ემეილი', 'class': 'form-control'})
    password = PasswordField('Password', validators=[data_required()],
                             render_kw={'class': 'form-control', 'placeholder': 'შეიყვანეთ პაროლი'})
    submit = SubmitField('Login', render_kw={'class': 'btn btn-primary', 'style': 'text-align: center;'})


class RegistrationForm(LoginForm):
    first_name = StringField('First Name', validators=[data_required()],
                             render_kw={'placeholder': 'შეიყვანეთ სახელი', 'class': 'form-control'})
    last_name = StringField('Last Name', validators=[data_required()],
                            render_kw={'placeholder': 'შეიყვანეთ გვარი', 'class': 'form-control'})
    age = IntegerField('Age', validators=[data_required()], render_kw={'class': 'form-control',
                                                                       'placeholder': 'შეიყვანეთ ასაკი'})
    address = StringField('Address', validators=[data_required()],
                          render_kw={'placeholder': 'შეიყვანეთ მისამართ', 'class': 'form-control'})
    submit = SubmitField('Registration', render_kw={'class': 'btn btn-primary', 'style': 'text-align: center;'})

