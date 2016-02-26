#!/usr/bin/env python
import os, sys
from crawler_functions import get_namespace_from_page



def get_media_from_dir(trope_dir, namespaces):
    media_titles = {i: [] for i in namespaces}
    for filename in os.listdir(trope_dir):
        #print(filename)
        with open(os.path.join(trope_dir, filename)) as f:
            page_src = f.read()
        for namespace in namespaces:
            current_titles = get_namespace_from_page(page_src, namespace)
            media_titles[namespace].extend(current_titles)
            #print(namespace + ' ' + str(media_titles[namespace]))
    for namespace in namespaces:
        media_titles[namespace] = list(set(media_titles[namespace]))
        media_titles[namespace].sort()
    return media_titles


if __name__ == '__main__':
    trope_dir = sys.argv[1]
    namespaces = sys.argv[1:]
    media_titles = get_media_from_dir(trope_dir, namespaces)
    for k,v in media_titles.items():
        with open(k + '_titles.txt', 'w') as f:
            f.write('\n'.join([i.split('/')[1] for i in v]))
