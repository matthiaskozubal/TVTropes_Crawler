#!/usr/bin/env python
import os
import re
import pymongo
from crawler_functions import download_page_source


MONGODB_HOST = 'localhost'
MONGODB_PORT = 27017


def find_subpages(media_doc):
    pattern = re.compile(media_doc['name'] + '/\w+')
    return pattern.findall(media_doc.get('source', ''))


if __name__ == '__main__':
    client = pymongo.MongoClient(MONGODB_HOST, MONGODB_PORT)
    db = client.get_database('tvtropes')
    media_collection = db.get_collection('media')

    trope_subpages_dir = os.path.join(os.getcwd(), 'Tropes', 'Subpages')

    for media in media_collection.find():
        subpages = find_subpages(media)
        if len(subpages) > 0:
            media_collection.find_one_and_update({'_id':media['_id']},
                {"$set": {'subpages': subpages}})
            subpage_sources = []
            for page in subpages:
                print(page)
                title, subtitle = page.split('/')
                source = download_page_source(subtitle, namespace=title,
                    delay=1,
                    local_file=os.path.join(trope_subpages_dir, page.replace('/', '_'))
                    )
                subpage_sources.append(source)
            media_collection.find_one_and_update({'_id':media['_id']},
                {"$set": {'subpage_sources': subpage_sources}})
