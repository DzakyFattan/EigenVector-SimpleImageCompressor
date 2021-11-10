from flask import Flask, request, render_template, make_response, jsonify
from flask_cors import CORS
from PIL import Image
from pathlib import Path
from io import BytesIO

import base64
import os
import img_compress as imgcomp

IMG_FOLDER = './img'
if not os.path.exists(IMG_FOLDER): os.makedirs(IMG_FOLDER)

app = Flask(__name__,
            static_folder = "../frontend/dist/static", 
            template_folder="../frontend/dist")

CORS(app, resources={r'/*': {'origins': '*'}})
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
   return render_template('index.html')

@app.route("/", methods=['POST'])
def upload_img():
    if request.method == 'POST':
        base64_jpg =  request.form['image']
        code = base64.b64decode(base64_jpg.split(',')[1]) 
        image_decoded = Image.open(BytesIO(code))
        image_decoded.save(Path(app.config['IMG_FOLDER']) / 'image.jpg')
        return make_response(jsonify({'result': 'success'}))
    else: 
        return make_response(jsonify({'result': 'invalid method'}), 400)

if __name__ == "__main__":
    app.run(debug=True)
