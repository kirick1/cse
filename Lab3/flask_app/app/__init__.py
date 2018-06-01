from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
from settings import MONGO_URI
import subprocess

from flask_app.app.messages_procesor.tag_cloud import get_cloud

app = Flask(__name__)
app.config['MONGO_URI'] = MONGO_URI
mongo = PyMongo(app)


@app.route("/")
def index():
    # prepare
    users = list(mongo.db.user.find().limit(100))

    tag_cloud = get_cloud(users)

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
