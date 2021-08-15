from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/hello')

def hell_world():
    return 'hello'

@app.route('/world')
def world():
    return "world"

@app.route('/hello/<name>')
def hello(name):
    return 'Hello %s' % name

@app.route('/blog/<int:postID>')
def show_blog(postID):
    return 'Blog Number %d' %postID


@app.route('/rev/<float:revNo>')
def revision_number(revNo):
    return 'Revision Number %f' % revNo

@app.route('/Joe')
def hello_Joe():
    return "hello joe"

@app.route('/John/<John>')
def hello_John(John):
    return "Hello %s as John" %John

@app.route('/user/<name>')
def hello_user(name):
    if name == "Joe":
        return redirect(url_for('hello_Joe'))
    else:
        return redirect(url_for('hello_John', John=name))



if __name__ == '__main__':
    #app.debug=True
    #app.run()
    app.run(debug=True)
