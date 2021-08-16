from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__, template_folder='templates')

@app.route('/success/<name>')
def success(name):
    return 'Welcome %s ' %name


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['nam']
        return redirect(url_for('success', name=user))
        #return redirect(url_for('success', name=user))
    else:
        user=request.args.get('nam')
        #return redirect(url_for('success', name=user))

if __name__ == '__main__':
    app.run(debug=True)
