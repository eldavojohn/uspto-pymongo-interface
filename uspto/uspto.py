import pymongo
from pymongo import MongoClient

def crawl_patents():
    client = MongoClient('localhost', 27017)
    db = client.uspto
    patent_collection = db.patents
    first_patent = patent_collection.find_one()
    print first_patent
    
