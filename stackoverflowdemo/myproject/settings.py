# Scrapy settings for myproject project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = "myproject"

SPIDER_MODULES = ["myproject.spiders"]
NEWSPIDER_MODULE = "myproject.spiders"
ITEM_PIPELINES = {
    'myproject.pipelines.JsonlPipeline': 1
}
# settings.py

USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
ADDONS = {}
HTTPERROR_ALLOWED_CODES = [403]
ROBOTSTXT_OBEY = False
FEED_EXPORT_ENCODING = "utf-8"
DOWNLOAD_DELAY = 2  # Delay of 2 seconds between requests
CONCURRENT_REQUESTS_PER_DOMAIN = 1