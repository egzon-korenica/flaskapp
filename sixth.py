from flask import Flask, render_template, request, redirect, url_for, make_response, session, abort

app = Flask(__name__, template_folder='templates')

app.secret_key="john"

@app.route('/')
def index():
    if 'username' in session:
        username = session['username']
        return '<br> Logged in as ' + username + '<br>' +\
            "<b><a href = '/logout'> Click here to log out</a><b>"
    return "you are not logged in <br><a href='/login'></br>" +\
        "Click here to Log In </b></a>"

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST' and request.form['username'] !== 'admin':
        abort(401)
    return '''

    <form action = "" method = "post">
        <p><input type="text" name="username"</p>
        <p><input type="submit" value="Login"</p>
    </form>

    '''

@app.route('/success')
def success():
    return "Login success"

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
