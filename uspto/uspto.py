from pymongo import MongoClient
from bson.son import SON
from bson.code import Code

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
    result = patent_collection.aggregate(pipeline)
    for doc in result:
        print(doc)
    return result

def map_reduce_applicant_by_state():
    patent_collection = get_collection()
    # obvious problem here is that multiple applicants mean that it's not per patent, it's per applicant per patent
    mapToState = Code("""
        function () {
            if(this.us_bibliographic_data_grant && this.us_bibliographic_data_grant.parties && this.us_bibliographic_data_grant.applicants && this.us_bibliographic_data_grant.applicants.applicant && this.us_bibliographic_data_grant.applicants.applicant.length > 0) {
                this.us_bibliographic_data_grant.applicants.applicant.forEach(function (applicant) {
                    if(applicant && applicant.addressbook && applicant.addressbook.address && applicant.addressbook.address.state) {
                        emit(applicant.addressbook.address.state, 1);
                    }
                });
            }
        }
        """)
    toStateReducer = Code("""
        function (key, values) {
            var total = 0;
            for (var i = 0; i < values.length; i++) {
                total += values[i];
            }
            return total;
        }
        """)
    result = patent_collection.map_reduce(mapToState, toStateReducer, "myresults")
    for doc in result:
        print(doc)
    return result
