from flask_wtf import Form
from wtforms import TextField, IntegerField, TextAreaField, SubmitField, RadioField, SelectField
from wtforms import validators, ValidationError

class ContactForm(Form):
    name = TextField("Name of Student", [validators.Required("Please Enter your name")])
    gender = RadioField('Gender', choices=[('M', 'Male'), ('F', 'Female')])
    Address = TextField("Address")
    email = TextField("Email", [validators.Required("Please enter your email"), validators.Email("Please enter your email again")])
    Age = IntegerField("Age")
    language = SelectField('Languages', choices=[('cpp', 'C++'), ('py', 'Python')])
    submit = SubmitField("Send")
