#!/usr/bin/env python
import os
import pymongo


MONGODB_HOST = 'localhost'
MONGODB_PORT = 27017


def put_file_into_mongodb(filename, namespace, mongodb_collection):
    mtime = os.path.getmtime(filename)
    with open(filename) as f:
        post = {
            'name': os.path.basename(filename),
            'namespace': namespace,
            'modification': mtime,
            'source': f.read()
        }
    mongodb_collection.insert_one(post)


if __name__ == '__main__':
    client = pymongo.MongoClient(MONGODB_HOST, MONGODB_PORT)
    db = client.get_database('tvtropes')
    media_collection = db.get_collection('media')

    trope_dir = os.path.join(os.getcwd(), 'Tropes')
    namespaces = os.listdir(trope_dir)
    namespaces.remove('Main')
    namespaces.remove('Subindex')   # Disney, Literature, Franchise, Blog, Theatre, Wrestling, Advertising,
    for namespace in namespaces:
        print('INSERTING ' + namespace)
        current_dir = os.path.join(trope_dir, namespace)
        for i in os.listdir(current_dir):
            print('\tinserting ' + i)
            put_file_into_mongodb(os.path.join(current_dir, i), namespace, media_collection)

    print('-------------------------------------------------------------------')

    trope_collection = db.get_collection('tropes')
    main_trope_dir = os.path.join(trope_dir, 'Main')
    print('INSERTING TROPES')
    for i in os.listdir(main_trope_dir):
        print('\tinserting ' + i)
        put_file_into_mongodb(os.path.join(main_trope_dir, i), 'Main', trope_collection)
