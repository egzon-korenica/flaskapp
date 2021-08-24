from flask import Flask, render_template, request, redirect, url_for, make_response, session, abort, flash
from werkzeug.utils import secure_filename

app = Flask(__name__, template_folder='templates')

app.secret_key="john"

@app.route('/upload')
def upload_file():
    return render_template('upload.html')

@app.route('/uploader', methods=['GET', 'POST'])
def uploaded_file():
    if request.method == 'POST':
        f = request.files['file']
        f.save(secure_filename(f.filename));
        return 'file uploaded successfully'

if __name__ == '__main__':
    app.run(debug=True)
