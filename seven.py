from flask import Flask, render_template, request, redirect, url_for, make_response, session, abort, flash

app = Flask(__name__, template_folder='templates')

app.secret_key="john"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    errorMessage=None
    if request.method=='POST':
        if request.form['username'] != 'admin' or \
            request.form['password'] != 'admin':
            errorMessage= 'Invalid Credentials. Please Try Again'
        else:
            flash("You have successfully logged in")
            return redirect(url_for('index'))
    return render_template('login.html', errorMessage = errorMessage)


if __name__ == '__main__':
    app.run(debug=True)
