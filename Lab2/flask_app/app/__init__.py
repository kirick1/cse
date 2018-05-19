from flask import Flask, render_template, redirect
from os.path import dirname, join
from flask_pymongo import PyMongo
from dotenv import get_key
import subprocess

dotenv_path = join(dirname(__file__), '..', '.env')

app = Flask(__name__)
app.config['MONGO_URI'] = get_key(dotenv_path, 'MONGO_URI')
mongo = PyMongo(app)


@app.route("/")
def index():
    users = mongo.db.user.find()
    return render_template('index.html', users=users)


@app.route("/<user_name>")
def user_profile(user_name):
    user = mongo.db.user.find_one_or_404({'user_name': user_name})
    print(user)
    return render_template('user.html', user=user)


@app.route("/refresh", methods=['POST'])
def refresh():
    subprocess.call(['scrapy', 'runspider', 'spider/forum.py'])
    return redirect('/')


if __name__ == "main":
    app.run(debug=True)
