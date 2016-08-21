from pymongo import MongoClient
from bson.son import SON

def get_collection():
    client = MongoClient('localhost', 27017)
    db = client.uspto
    return db.patents

def print_first_patent():
    patent_collection = get_collection()
    first_patent = patent_collection.find_one()
    print first_patent

def crawl_patents_with_aggregate():
    patent_collection = get_collection()
    pipeline = [
        {"$match": {"lang": "EN"}}, # we match only records that are english language
        {"$group": {"_id": "$status", "count": {"$sum": 1}}}, # of those records we group them by status value and count them by 1 each
        {"$sort": SON([("count", -1), ("_id", -1)])} # finally we put the highest values first in our output array
    ]
    list(patent_collection.aggregate(pipeline))
