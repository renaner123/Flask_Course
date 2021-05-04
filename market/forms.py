from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from market.models import User
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError

class RegisterForm(FlaskForm):
    # Necessário validar o campos uniques, pra não mostrar tela de debug para o usuário
    # o nome após o validate_ deve ser o nome do campo a ser validado. Flask vai entender que precisa validar algo
    def validate_username(self, username_to_check):
        #retorna um objeto. o first() retorna o primeiro item que é igual desse objeto
        user = User.query.filter_by(username=username_to_check.data).first()
        if user:
            raise ValidationError('Username already exists! Please try a differente username')

    def validate_email_address(self, email_address_to_check):
        email_address = User.query.filter_by(email_address=email_address_to_check.data).first()
        if email_address:
            raise ValidationError('Email Addres already exists! Please try a different email address')

    username = StringField(label='User Name:', validators=[Length(min=2,max=30), DataRequired()])
    email_address = StringField(label='Email Address', validators=[Email(), DataRequired()])
    password1 = PasswordField(label='Password', validators=[Length(min=6), DataRequired()])
    password2 = PasswordField(label='Confirm Password', validators=[EqualTo('password1'),DataRequired()])
    submit = SubmitField(label='Create Account')
    
class LoginForm(FlaskForm):
    username = StringField(label='User Name:', validators=[DataRequired()])
    password = StringField(label='Password:', validators=[DataRequired()])
    submit = SubmitField(label='Sign in')

class PurchaseItemForm(FlaskForm):
    submit = SubmitField(label='Purchase Item!')

class SellItemForm(FlaskForm):
    submit = SubmitField(label='Sell Item!')