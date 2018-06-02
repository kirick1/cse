from flask import Flask, Response, render_template, redirect
from werkzeug.contrib.cache import SimpleCache
from flask_pymongo import PyMongo
from settings import MONGO_URI
from utils import get_file, parse_user, parse_users
import subprocess
import json

# from flask_app.app.messages_processor.tag_cloud import get_cloud

app = Flask(__name__)
app.config['MONGO_URI'] = MONGO_URI
mongo = PyMongo(app)
cache = SimpleCache()


def get_all_users():
    from_cache = cache.get('users')
    if from_cache is None:
        users_from_db = list(mongo.db.user.find().sort('rating', -1))
        users_without_objectid_field = parse_users(users_from_db)
        cache.set('users', users_without_objectid_field)
        from_cache = cache.get('users')
    return from_cache


@app.route("/")
def index():
    # tag_cloud = get_cloud(users)
    content = get_file('index.html')
    return Response(content, mimetype='text/html')


@app.route("/api/users")
def get_users():
    users = get_all_users()
    response = app.response_class(
        response=json.dumps(users, ensure_ascii=False),
        status=200,
        mimetype='application/json'
    )
    return response


@app.route("/api/users/<user_name>")
def get_user(user_name):
    user = mongo.db.user.find_one_or_404({'user_name': user_name})
    parsed = parse_user(user)
    response = app.response_class(
        response=json.dumps(parsed, ensure_ascii=False),
        status=200,
        mimetype='application/json'
    )
    return response


@app.route("/users/<user_name>")
def user_profile(user_name):
    print(user_name)
    content = get_file('user.html')
    return Response(content, mimetype='text/html')


@app.route("/refresh", methods=['POST'])
def refresh():
    subprocess.call(['scrapy', 'runspider', 'spider/forum.py'])
    return redirect('/')


if __name__ == 'main':
    app.run(debug=True)
