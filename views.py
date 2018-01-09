from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/signin')
def signin():
    return render_template("signin.html")

@app.route('/authorize.php')
def authorize():
    return render_template("authorize.php")




if __name__ == '__main__':
    app.run(debug=True)
