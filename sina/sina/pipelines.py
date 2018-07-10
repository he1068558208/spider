# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
from scrapy.conf import settings

from sina.items import SinaItem


class SinaPipeline(object):
    def process_item(self, item, spider):
        return item

class PymongosinaPipeline(object):

    def __init__(self):
        conn = pymongo.MongoClient(host=settings['MONGODB_HOST'],
                                    port=settings['MONGODB_PORT'])
        db = conn[settings['MONGODB_DB']]
        self.collection = db[SinaItem.collections]

    def process_item(self, item, spider):
        if isinstance(item,SinaItem):
            # self.collection.update({'house_code':item['house_code']},{'$set':item}, True)
            self.collection.insert(dict(item))
        return item