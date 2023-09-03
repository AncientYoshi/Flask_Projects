from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError
from market.models import User


class register_form(FlaskForm):
    def validate_username(self, username_to_check):
        user = User.query.filter_by(username=username_to_check.data).first()
        if user:
            raise ValidationError("Username already exist..")

    def validate_email_address(self, email_address_to_check):
        email_address = User.query.filter_by(
            email_address=email_address_to_check.data
        ).first()
        if email_address:
            raise ValidationError("Email is already in use..")

    username = StringField(
        label="User Name:", validators=[Length(min=4, max=30), DataRequired()]
    )
    email_address = StringField(
        label="Email Address:", validators=[Email(), DataRequired()]
    )
    password1 = PasswordField(
        label="Password:", validators=[Length(min=6, max=30), DataRequired()]
    )
    password2 = PasswordField(
        label="Confirm Password:", validators=[EqualTo("password1"), DataRequired()]
    )
    submit = SubmitField(label="Create Account")


class login_Form(FlaskForm):
    username = StringField(label="Username : ", validators=[DataRequired()])
    password = PasswordField(label="Password : ", validators=[DataRequired()])
    submit = SubmitField(label="Sign in")


class PurchaseItemForm(FlaskForm):
    submit = SubmitField(label="Purchase Item")


class SellItemForm(FlaskForm):
    submit = SubmitField(label="Sell Item")