#!/usr/bin/env python3
import sys
import crawler_functions
from time import sleep


CRAWL_DELAY = 1


def download_from_list(media_list, namespace):
    for title in media_list:
        try:
            print('Downloading ' + title)
            crawler_functions.download_page_source(title, namespace=namespace,
                delay=CRAWL_DELAY,
                local_file='Tropes/' + namespace + '/' + title.replace('/', '_'))
        except:
            print('ERROR! Check page ' + title + ' for problems')


if __name__ == '__main__':
    namespace = sys.argv[1]
    with open(sys.argv[2]) as f:
        titles = [i.rstrip('\n') for i in  f.readlines()]
    download_from_list(titles, namespace)
