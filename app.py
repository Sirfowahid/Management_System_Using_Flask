from flask import Flask,render_template,request,redirect,url_for
app = Flask(__name__)


@app.route('/')
@app.route('/index')
@app.route('/home')
def index():
    return render_template("index.html")

@app.route('/login',methods=["GET","POST"])
def login():
    if request.method == "POST":
        user = request.form["username"]
        return redirect(url_for("user"))
    else:
        return render_template("login.html")
    

@app.route('/user')
def user():
    return f"<h1>Hello</h1>"

if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True)