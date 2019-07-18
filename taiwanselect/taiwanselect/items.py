# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/itemgr
from scrapy import Field,Item


class TaiwanselectItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title=Field()
    time=Field()
    content=Field()

