from flask import Flask, render_template, request, redirect, url_for, make_response, session, abort, flash
from werkzeug.utils import secure_filename
from flask_mail import Mail, Message
from flask_wtf import Form
from forms import ContactForm

app = Flask(__name__)

app.secret_key = "Flask"

@app.route('/contact', methods=['get', 'post'])
def contact():
    form = ContactForm()
    if request.method == "POST":
        if form.validate() == False:
            flash("All the required fields must be filled")
            return render_template('contact.html', form=form)
        else:
            return "Success"
    elif request.method=='GET':
        return render_template('contact.html', form=form)
    return render_template('contact.html', form=form)



if __name__ == '__main__':
    app.run(debug=True)
