from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "这是首页"

@app.route("/face")
def face():
    return "这是face"


if __name__ =="__main__":
    app.run(debug=True)

