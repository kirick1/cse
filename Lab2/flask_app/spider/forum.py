from os.path import dirname, join
from dotenv import get_key
import scrapy
import re

from scrapy import Selector

dotenv_path = join(dirname(__file__), '..', '.env')

XPATH_TOPICS = "//ol[@class='nodeList']//div[contains(@class, 'primaryContent')]//h3[@class='nodeTitle']/a/@href"
XPATH_THREADS = "//*[contains(@class, 'discussionListItems')]//h3/a[@class='PreviewTooltip']/@href"
XPATH_USER_NAME = '//@data-author'
XPATH_POSTS = "//ol[@class='messageList']/li[div[not(contains(@id, 'second-post'))]]"
XPATH_MESSAGE = '//div[@class="messageContent"]//blockquote/text()'
XPATH_AVATAR = '//div[contains(@class, "avatar")]/img/@src'
XPATH_RANG = '//h3[@class="userText"]/em[2]/text()'
XPATH_RATING = '//div[@class="extraUserInfo"]/dl[3]/dd/span/text()'
XPATH_USER_MESSAGES_COUNT = "//div[@class='extraUserInfo']/dl[2]/dd[1]/span/text()"
XPATH_NEXT = '//div[@class="PageNav"]/nav/a[last()]/@href'
USER_ID_REGEX = '.([0-9]+)/$'
HEADERS = {
    'User-Agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.78 Safari/537.36"}

name = "posts"
base_url = 'http://avtoved.guru/forums/'


class ForumSpider(scrapy.Spider):
    name = 'forum_spider'
    start_urls = [base_url]

    custom_settings = {
        'ITEM_PIPELINES': {
            'spider.pipelines.MongoPipeline': 300,
        },
        'MONGO_URI': get_key(dotenv_path, 'MONGO_URI'),
        'MONGO_DATABASE': 'python-lab-2'
    }

    def parse(self, response):
        for topic in response.xpath(XPATH_TOPICS).extract():
            yield response.follow(topic, callback=self.parse_topic)

    def parse_topic(self, response):
        for thread in response.xpath(XPATH_THREADS).extract():
            yield response.follow(thread, callback=self.parse_thread)
        next_page_url = response.xpath(XPATH_NEXT).extract_first()
        if next_page_url:
            yield response.follow(next_page_url, callback=self.parse_topic)

    def parse_thread(self, response):
        posts = response.xpath(XPATH_POSTS)
        for post in posts:
            selected_post = Selector(text=post.extract())

            raw_message = "".join(selected_post.xpath(XPATH_MESSAGE).extract())

            user_name = selected_post.xpath(XPATH_USER_NAME).extract_first()
            avatar = selected_post.xpath(XPATH_AVATAR).extract_first()
            rating = float(selected_post.xpath(XPATH_RATING).extract_first())
            rang = selected_post.xpath(XPATH_RANG).extract_first()
            message = re.sub('', '', re.sub(' +', ' ', raw_message)).replace('\n', '').replace('\t', '').strip(' ')

            yield {
                "user_name": user_name,
                "message": message,
                "rating": rating,
                "avatar": avatar,
                "rang": rang
            }

        next_page_url = response.xpath(XPATH_NEXT).extract_first()
        if next_page_url:
            yield response.follow(next_page_url, callback=self.parse_thread)
