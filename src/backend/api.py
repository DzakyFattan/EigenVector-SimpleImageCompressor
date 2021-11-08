from flask import Flask, render_template
from flask_cors import CORS

app = Flask(__name__, 
            static_folder="../frontend/dist/static",
            template_folder="../frontend/dist")

CORS(app, resources={r'/*': {'origins': '*'}})

@app.route("/main", methods=["POST","GET"])
def index():
    return render_template("index.html")
