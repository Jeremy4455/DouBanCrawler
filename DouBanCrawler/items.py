# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubancrawlerItem(scrapy.Item):
    score = scrapy.Field()
    name = scrapy.Field()
    desc = scrapy.Field()
    img = scrapy.Field()

