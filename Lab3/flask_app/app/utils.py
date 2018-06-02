import os


def get_file(filename):
    try:
        src = os.path.join(os.getcwd(), 'app', 'views', filename)
        return open(src).read()
    except IOError as exc:
        return str(exc)


def parse_user_messages(messages):
    parsed_messages = []
    for message in messages:
        if message != '':
            parsed_messages.append(str(message))
    return parsed_messages


def parse_user(user):
    return {
        'user_name': user['user_name'],
        'rating': user['rating'],
        'rang': user['rang'],
        'avatar': user['avatar'],
        'messages': parse_user_messages(user['messages'])
    }


def parse_users(users):
    parsed_users = []
    for user in users:
        parsed_users.append(parse_user(user))
    return parsed_users
