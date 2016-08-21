import pymongo
from pymongo import MongoClient


def start_client():
    client = MongoClient('localhost', 27017)
    return 'started...'

def crawl_patents():
    print start_client()
