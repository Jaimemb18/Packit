from flask import Flask, render_template, redirect
app = Flask(__name__, template_folder='./src/templates/')


@app.route('/')
def index():
    return render_template("packit.html")
