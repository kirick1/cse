import pymongo


class MongoPipeline(object):
    def __init__(self, mongo_uri, mongo_db):
        self.client = pymongo.MongoClient(mongo_uri)
        self.db = self.client[mongo_db]
        self.db.user.remove()

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get('MONGO_URI'),
            mongo_db=crawler.settings.get('MONGO_DATABASE', 'items')
        )

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        user = self.db.user.find_one({'user_name': item['user_name']})
        if user is None:
            item['messages'] = [item.pop('message')]
            self.db.user.insert(item)
        else:
            user['messages'].append(item['message'])
            self.db.user.update({"user_name": user['user_name']}, user)
