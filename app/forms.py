from wtforms import Form, TextField, SubmitField, PasswordField

class LoginForm(Form):
    username = TextField("Username")
    password = PasswordField("Password")
    submit = SubmitField("Login")