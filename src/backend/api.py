from flask import Flask, request, redirect, render_template, make_response, jsonify
from flask.helpers import url_for
from flask_cors import CORS
from PIL import Image
from io import BytesIO

import base64
import os
import img_compress as imgcomp

app = Flask(__name__,
            static_folder = "../dist/static", 
            template_folder="../dist")

IMG_FOLDER = './img'
app.config['IMG_FOLDER'] = IMG_FOLDER

CORS(app, resources={r'/*': {'origins': '*'}})
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
   return render_template('index.html')

@app.route("/", methods=['POST'])
def upload_img():
    base64_jpg =  request.form['image']
    value =  request.form['value']
    code = base64.b64decode(base64_jpg.split(',')[1]) 
    image_decoded = Image.open(BytesIO(code))
    image_decoded = imgcomp.compress(image_decoded, value)
    image_decoded.filename = "image.jpg"
    full_filename = os.path.join(app.config['IMG_FOLDER'], image_decoded.filename)
    image_decoded.save(full_filename)
    return render_template("pic.html", user_image = full_filename)

if __name__ == "__main__":
    app.run(debug=True)
