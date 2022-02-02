import pymongo

from scrapy.utils.project import get_project_settings

from dataclasses import asdict
from .items import StackItem


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
        if isinstance(item, StackItem):
            self.collection.replace_one(
                {'_id': item._id},
                asdict(item),
                upsert=True
            )
        return item
