#!/usr/bin/env python3
import sys
import crawler_functions
from time import sleep


CRAWL_DELAY = 1


def download_from_list(trope_list):
    for trope in trope_list:
        print('Downloading ' + trope)
        crawler_functions.download_page_source(trope, delay=CRAWL_DELAY, local_file='Tropes/Main/' + trope.replace('/', '_'))


if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        tropes = [i.rstrip('\n') for i in  f.readlines()]
    download_from_list(tropes)
