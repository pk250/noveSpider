# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class NoveItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class Name(scrapy.Item):
    Name=scrapy.Field()
    Nurl=scrapy.Field()
    nid=scrapy.Field()
    pass
class Sec(scrapy.Item):
    Title=scrapy.Field()
    Surl=scrapy.Field()
    nid=scrapy.Field()
    sid=scrapy.Field()
    pass

