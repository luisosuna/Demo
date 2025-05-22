from scrapy.cmdline import execute

# IMPORTANT: Set this to match your spider name
execute(["scrapy", "crawl", "stackoverflow"])
