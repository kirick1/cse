from os.path import dirname, join
from dotenv import get_key

dotenv_path = join(dirname(__file__), '.env')

ITEM_PIPELINES = {
    'app.spider.pipelines.MongoPipeline': 300,
}
MONGO_URI = get_key(dotenv_path, 'MONGO_URI')
