from flask import Flask, render_template, flash, request, redirect, url_for
from flask_cors import CORS
from werkzeug.utils import secure_filename

import img_compress as imgcomp

app = Flask(__name__)

CORS(app, resources={r'/*': {'origins': '*'}})

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/", methods=["POST"])
def upload_image():
    uploaded_img = request.files['file']
    if uploaded_img.filename != '':
        uploaded_img.save(secure_filename(uploaded_img.filename))


if __name__ == "__main__":
    app.run(debug=True)
