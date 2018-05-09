from lxml import html
import requests


def request_page(page_link):
    return requests.get(page_link)


def parse_forum_message(message):
    tread = message[0][3]
    if len(tread) == 4:
        return tread[2].text
    else:
        return tread[3].text


def parse_forum_messages(page_content):
    document = html.document_fromstring(page_content)
    events_list = document.get_element_by_id('event_list').getchildren()
    events = []
    for event in events_list:
        if event.getchildren():
            parsed_event = parse_forum_message(event.getchildren())
            events.append(parsed_event)
        else:
            continue
    return events


def parse_forum_users(page_content):
    document = html.document_fromstring(page_content)
    users_list = document.find_class('in b1sE p10')
    users = []
    for user in users_list:
        users.append(user.getchildren()[1][0].text)
    return users


class Forum:
    def __init__(self):
        self.origin_link = 'http://avtomarket.ru'
        self.forum_link = self.origin_link + '/forum/remont'
        self.users_link = self.origin_link + '/owners'

    def get_messages(self):
        page = request_page(self.forum_link)
        messages = parse_forum_messages(page.content)
        return messages

    def get_users(self):
        page = request_page(self.users_link)
        users = parse_forum_users(page.content)
        return users
