from flask import Flask, request, render_template
from utils import compare_signatures
import os

app = Flask(__name__)
#UPLOAD_FOLDER = "uploads"
UPLOAD_FOLDER = "static"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/", methods=["GET", "POST"])
def index():
    result = ""
    if request.method == "POST":
        file1 = request.files["image1"]
        file2 = request.files["image2"]
        path1 = os.path.join("static", "img1.png")
        path2 = os.path.join("static", "img2.png")
        file1.save(path1)
        file2.save(path2)
        result = compare_signatures(path1, path2)
    return render_template("index.html", result=result)

if __name__ == "__main__":
    #app.run(debug=True)
    app.run(debug=True, host="0.0.0.0")