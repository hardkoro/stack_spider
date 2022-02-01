import logging
import pymongo

from scrapy.exceptions import DropItem
from scrapy.utils.project import get_project_settings


settings = get_project_settings()


class MongoDBPipeline(object):
    def __init__(self):
        connection = pymongo.MongoClient(
            settings.get('MONGODB_SERVER'),
            settings.get('MONGODB_PORT')
        )
        db = connection[settings.get('MONGODB_DB')]
        self.collection = db[settings.get('MONGODB_COLLECTION')]

    def process_item(self, item, spider):
        valid = True
        for data in item:
            if not data:
                valid = False
                raise DropItem(f'Missing {data}!')
        if valid:
            self.collection.insert_one(dict(item))
            logging.debug('Question added to MongoDB database!')
        return item
