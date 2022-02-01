import scrapy
from scrapy_redis.spiders import RedisSpider


class DemoSpider(RedisSpider):
    name = "demo"
    redis_key = "demo:start_urls"
    allowed_domains = ['quotes.toscrape.com']
    start_urls = [
        'http://quotes.toscrape.com/',
    ]

    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {
                'text': quote.css('span.text::text').get(),
                'author': quote.css('span small::text').get(),
                'tags': quote.css('div.tags a.tag::text').getall(),
            }