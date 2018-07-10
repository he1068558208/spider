# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SinaItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    collections = 'sina'
    newsTitle = scrapy.Field()  # 新闻标题
    newsUrl = scrapy.Field()  # 链接
    newsTime = scrapy.Field()  # 时间
    newsContent = scrapy.Field()  # 新闻内容
    pass
