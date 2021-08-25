from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:1234@localhost:5432/flask_course'
app.config['SECRET_KEY'] = 'super-secret'
app.config['SECURITY_REGISETRABLE'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.debug=True

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(75), unique=True)
    password = db.Column(db.String(75), unique=True)

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def _repr_(self):
        return '<User %r>'%self.username


if __name__ == '__main__':
    app.run()
