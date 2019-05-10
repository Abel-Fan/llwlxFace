from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/face1")
def face1():
    return render_template("face1.html")

@app.route("/zhuce")
def zhuce():
    return render_template("zhuce.html")

@app.route("/success")
def success():
    return render_template("success.html")

@app.route("/error")
def error():
    return render_template("error.html")

if __name__ =="__main__":
    app.run(debug=True)

