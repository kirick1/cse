from dotenv import get_key
from os.path import dirname, join
from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
from Lab2.parser import Forum

dotenv_path = join(dirname(__file__), '.env')

app = Flask(__name__)
app.config['MONGO_URI'] = mongodb_uri = get_key(dotenv_path, 'MONGODB_URI')
mongo = PyMongo(app)


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/refresh", methods=['POST'])
def refresh():
    return redirect('/')


if __name__ == "__main__":
    forum = Forum()
    messages = forum.get_messages()
    print('Messages:')
    print(messages)
    users = forum.get_users()
    print('Users:')
    print(users)
    # app.run(debug=True)
