from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
from settings import MONGO_URI
import subprocess

app = Flask(__name__)
app.config['MONGO_URI'] = MONGO_URI
mongo = PyMongo(app)


@app.route("/")
def index():
    users = mongo.db.user.find().sort('rating', -1)
    return render_template('index.html', users=users)


@app.route("/<user_name>")
def user_profile(user_name):
    user = mongo.db.user.find_one_or_404({'user_name': user_name})
    return render_template('user.html', user=user)


@app.route("/refresh", methods=['POST'])
def refresh():
    subprocess.call(['scrapy', 'runspider', 'spider/forum.py'])
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)
