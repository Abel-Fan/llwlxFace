from flask import Flask,render_template,request
import urllib,ssl

ssl._create_default_https_context = ssl._create_unverified_context

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

@app.route("/face2")
def face2():
    return render_template("face2.html")

@app.route("/photo",methods=['POST'])   # 检测人脸并且存储人脸
def photo():
    data = urllib.parse.urlencode(request.form).encode("utf8") # 编码
    con = urllib.request.urlopen("https://118.190.150.35:5000/api/photo",data=data).read()
    print(con)
    return con

@app.route("/check",methods=['POST'])
def check():
    data = urllib.parse.urlencode(request.form).encode("utf8")  # 编码
    con = urllib.request.urlopen("https://118.190.150.35:5000/api/check", data=data).read()
    print(con)
    return con

if __name__ =="__main__":
    app.run(debug=True)

