import redis
import json  # 新增导入json模块

# Redis 配置
REDIS_HOST = 'localhost'
REDIS_PORT = 6379
REDIS_PASSWORD = None  # 如果没有密码则为 None
START_URLS = [
    'https://ssr1.scrape.center/',
    'https://www.baidu.com/',
    'https://curlconverter.com/python/',
    'http://books.toscrape.com/',
    'http://quotes.toscrape.com/',
    'http://api.openweathermap.org/data/2.5/weather?q=London',
    'https://api.nasa.gov/',
]

def start_master():
    r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, password=REDIS_PASSWORD, decode_responses=True)
    r.delete("myspider:start_urls")  # 清空旧数据

    for url in START_URLS:
        request_data = {
            "url": url,
        }
        r.lpush("myspider:start_urls", json.dumps(request_data))

if __name__ == "__main__":
    start_master()