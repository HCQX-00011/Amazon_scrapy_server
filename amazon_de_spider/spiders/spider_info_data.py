import scrapy
from scrapy_redis.spiders import RedisSpider

class MySpider(RedisSpider):
    name = 'spider_info_de'
    redis_key = "myspider:start_urls"

    def parse(self, response):
        # 简易解析示例：提取标题
        title = response.css('title::text').get()
        status = response.status
        yield {
            'url': response.url,
            'title': title,
            "status":status,
        }