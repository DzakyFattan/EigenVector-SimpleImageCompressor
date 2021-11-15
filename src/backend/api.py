from flask import Flask, request, redirect, render_template, send_file
from flask_cors import CORS
from PIL import Image
from io import BytesIO

import time
import json
import base64
import os
import img_compress as imgcomp

app = Flask(__name__,
            static_folder = "../dist/static", 
            template_folder="../dist")

IMG_FOLDER = './img/'
app.config['IMG_FOLDER'] = IMG_FOLDER

CORS(app)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
   return render_template('index.html')

@app.route("/compress", methods=['GET','POST'])
def upload_img():
    time.sleep(2)
    f = open('../frontend/img/image.json')
    imgData = json.load(f)
    base64_jpg = imgData['image'][0]['base64']
    value = int(imgData['image'][0]['percentage'])
    fileName = imgData['image'][0]['fileName']
    code = base64.b64decode(base64_jpg.split(',')[1]) 
    image_decoded = Image.open(BytesIO(code))
    image_comp = imgcomp.compress(image_decoded, value)
    image_comp.filename = "image.jpg"
    imgPath = os.path.join(app.config['IMG_FOLDER'], image_comp.filename).replace("\\","/")
    image_comp.save(imgPath)
    return send_file('.\\img\\image.jpg')
        
       

if __name__ == "__main__":
    app.run(debug=True)
