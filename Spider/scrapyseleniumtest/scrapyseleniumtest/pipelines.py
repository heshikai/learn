## -*- coding: utf-8 -*-
#
## Define your item pipelines here
##
## Don't forget to add your pipeline to the ITEM_PIPELINES setting
## See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
#
#import pymongo
#
#class MongoPipeline(object):
#    
#    def __init__(self,mongo_uri,mongo_db):
#        self.mongo_uri = mongo_uri
#        self.mongo_db = mongo_db
#    
#    @classmethod
#    def from_crawler(cls,crawler):
#        return cls(
#            mongo_uri = crawler.settings.get('MONGO_URI'),
#            mongo_db = crawler.settings.get('MONGO_DB')
#        )
#
#    def open_spider(self,spider):
#        print(2222222222222222222)
#        self.client = pymongo.MongoClient(self.mongo_uri)
#        self.db = self.client[self.mongo_db]
#    def process_item(self,item,spider):
#        print(1111111111111111111)
#        print(dict(item))
#        self.db[item.collection].insert(dict(item))
#    def close_spider(self,spider):
#        print(333333333333333333333)
#        self.client.close()
#
#class ScrapyseeleniumtestPipeline(object):
#    def process_item(self, item, spider):
#        return item



# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


import pymongo

class MongoPipeline(object):
    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db
    
    @classmethod
    def from_crawler(cls, crawler):
        return cls(mongo_uri=crawler.settings.get('MONGO_URI'), mongo_db=crawler.settings.get('MONGO_DB'))
    
    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]
    
    def process_item(self, item, spider):
        self.db[item.collection].insert(dict(item))
        return item
    
    def close_spider(self, spider):
        self.client.close()
