import scrapy

class SoItem(scrapy.Item):
    question = scrapy.Field()
    answer = scrapy.Field()
    tags = scrapy.Field()
    link = scrapy.Field()
    answers = scrapy.Field()  # Add the field for answers
