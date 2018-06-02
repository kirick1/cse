from utils import get_file, parse_user, parse_users
from werkzeug.contrib.cache import SimpleCache
from flask import Flask, Response, redirect
from flask_pymongo import PyMongo
from settings import MONGO_URI
import subprocess
import json

from messages_processor.tag_cloud import get_cloud

app = Flask(__name__)
app.config['MONGO_URI'] = MONGO_URI
mongo = PyMongo(app)
cache = SimpleCache()


def get_all_users():
    print('Getting all users ...')
    users_from_cache = cache.get('users')
    if users_from_cache is None:
        print('Getting all users from database ...')
        users_from_db = mongo.db.user.find().sort('rating', -1)
        users_without_objectid_field = parse_users(users_from_db)
        cache.set('users', users_without_objectid_field)
        users_from_cache = cache.get('users')
    return list(users_from_cache)


def get_users(skip=0):
    users = get_all_users()
    if skip > len(users):
        skip = round(len(users) / 100)
    i = skip
    users_number = skip + 100
    users_in_range = []
    while i < users_number:
        users_in_range.append(users[i])
        i += 1
        if i == len(users) - 1:
            return users_in_range
    return users_in_range


@app.route("/")
def index():
    print('Redirecting to "/users/page/1"')
    return redirect('/users/page/1')


@app.route("/users")
def users_page():
    print('Redirecting to "/users/page/1"')
    return redirect('/users/page/1')


@app.route("/users/page/<page_number>")
def get_page(page_number):
    print('Page number: ' + page_number)
    content = get_file('index.html')
    return Response(content, mimetype='text/html')


@app.route("/users/<user_name>")
def user_profile(user_name):
    print('User: ' + user_name)
    content = get_file('user.html')
    return Response(content, mimetype='text/html')


@app.route("/api/users")
def get_users_list():
    users = get_all_users()
    response = app.response_class(
        response=json.dumps(users, ensure_ascii=False),
        status=200,
        mimetype='application/json'
    )
    return response


@app.route("/api/users/page/<page_number>")
def get_users_by_page(page_number):
    skip = 100 * (int(page_number) - 1)
    users = get_users(skip=skip)
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


@app.route("/api/tagcloud")
def get_tag_cloud():
    users = get_all_users()
    tag_cloud = get_cloud(users)
    response = app.response_class(
        response=json.dumps(tag_cloud, ensure_ascii=False),
        status=200,
        mimetype='application/json'
    )
    return response


@app.route("/api/tagcloud/pages/<page_number>")
def get_tag_cloud_by_page(page_number):
    skip = 100 * (int(page_number) - 1)
    users = get_users(skip=skip)
    tag_cloud = get_cloud(users)
    response = app.response_class(
        response=json.dumps(tag_cloud, ensure_ascii=False),
        status=200,
        mimetype='application/json'
    )
    return response


@app.route("/api/tagcloud/users/<user_name>")
def get_tag_cloud_by_user(user_name):
    user = mongo.db.user.find_one_or_404({'user_name': user_name})
    parsed = parse_user(user)
    users = [parsed]
    tag_cloud = get_cloud(users)
    response = app.response_class(
        response=json.dumps(tag_cloud, ensure_ascii=False),
        status=200,
        mimetype='application/json'
    )
    return response


@app.route("/refresh", methods=['POST'])
def refresh():
    subprocess.call(['scrapy', 'runspider', 'spider/forum.py'])
    return redirect('/')


if __name__ == 'main':
    app.run(debug=True)
