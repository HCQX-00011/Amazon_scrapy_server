# 亚马逊德国爬虫项目的Scrapy设置
#
# 为简单起见，此文件仅包含最重要的或常用的设置。
# 更多设置请查阅文档：
#
#   https://docs.scrapy.org/en/latest/topics/settings.html
#   https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#   https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = "amazon_de_spider"  # 爬虫名称

SPIDER_MODULES = ["amazon_de_spider.spiders"]  # 爬虫模块路径
NEWSPIDER_MODULE = "amazon_de_spider.spiders"  # 新建爬虫的默认模块

ADDONS = {}  # 插件字典

# 通过在User-Agent中声明身份来负责任地爬取
#USER_AGENT = "amazon_de_spider (+http://www.yourdomain.com)"

# 不遵守robots.txt规则
ROBOTSTXT_OBEY = False

# 使用 Redis 作为调度器
SCHEDULER = "scrapy_redis.scheduler.Scheduler"
# 保持暂停状态允许恢复
SCHEDULER_PERSIST = True
# 使用 Redis 去重
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"
# Redis 连接设置
REDIS_HOST = 'localhost'
REDIS_PORT = 6379
REDIS_PASSWORD = None

# 启用 Redis 管道存储结果
ITEM_PIPELINES = {
    'scrapy_redis.pipelines.RedisPipeline': 300
}

# 配置Scrapy的最大并发请求数（默认：16）
#CONCURRENT_REQUESTS = 32

# 配置对同一网站的请求延迟（默认：0）
# 详见：https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# 另见自动限速设置和文档
#DOWNLOAD_DELAY = 3
# 下载延迟设置将仅生效以下一项：
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# 禁用Cookies（默认启用）
#COOKIES_ENABLED = False

# 禁用Telnet控制台（默认启用）
#TELNETCONSOLE_ENABLED = False

# 覆盖默认请求头：
DEFAULT_REQUEST_HEADERS = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'cache-control': 'no-cache',
    'device-memory': '8',
    'downlink': '3.8',
    'dpr': '0.8',
    'ect': '4g',
    'pragma': 'no-cache',
    'priority': 'u=0, i',
    'rtt': '150',
    'sec-ch-device-memory': '8',
    'sec-ch-dpr': '0.8',
    'sec-ch-ua': '"Microsoft Edge";v="137", "Chromium";v="137", "Not/A)Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-ch-ua-platform-version': '"19.0.0"',
    'sec-ch-viewport-width': '804',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36 Edg/137.0.0.0',
    'viewport-width': '804',
}

# 启用或禁用爬虫中间件
# 详见：https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    "amazon_de_spider.middlewares.AmazonDeSpiderSpiderMiddleware": 543,
#}

# 启用或禁用下载器中间件
# 详见：https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    "amazon_de_spider.middlewares.AmazonDeSpiderDownloaderMiddleware": 543,
#}

# 启用或禁用扩展组件
# 详见：https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    "scrapy.extensions.telnet.TelnetConsole": None,
#}

# 配置项目管道
# 详见：https://docs.scrapy.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    "amazon_de_spider.pipelines.AmazonDeSpiderPipeline": 300,
#}

# 启用并配置自动限速扩展（默认禁用）
# 详见：https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# 初始下载延迟
#AUTOTHROTTLE_START_DELAY = 5
# 高延迟情况下的最大下载延迟
#AUTOTHROTTLE_MAX_DELAY = 60
# Scrapy应向每个远程服务器发送的平均并发请求数
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# 启用显示每个响应的限速统计信息：
#AUTOTHROTTLE_DEBUG = False

# 启用并配置HTTP缓存（默认禁用）
# 详见：https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = "httpcache"
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = "scrapy.extensions.httpcache.FilesystemCacheStorage"

# 将已弃用的默认设置改为未来兼容的值
FEED_EXPORT_ENCODING = "utf-8"  # 导出文件编码格式