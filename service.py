from flask import Flask,request
from fileinput import filename
from flask_cors import CORS , cross_origin
app = Flask(__name__)

CORS(app)

@app.route("/uploadFile", methods=["GET","POST"])
@cross_origin()
def sendValuesfromFrontend():
    if request.method == "POST":
        f = request.files['files']
        f.save(f.filename)
        return "files Uploaded"

if __name__ == '__main__':
    app.run(debug=True)
