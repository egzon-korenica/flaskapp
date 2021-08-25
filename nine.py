from flask import Flask, render_template, request, redirect, url_for, make_response, session, abort, flash
from werkzeug.utils import secure_filename
from flask_mail import Mail, Message

app = Flask(__name__)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = '2015n0346@gmail.com'
app.config['MAIL_PASSWORD'] = 'umairkhan123'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail = Mail(app)

@app.route('/')
def index():
    msg = Message('Hello', sender='2014n0346@gmail.com', recipients=['korenicaegzon@gmail.com'])
    msg.body = 'Hello flask sent you an email through localserver'
    mail.send(msg)
    return 'Sent Success'

if __name__ == '__main__':
    app.run(debug=True)
