#!/usr/bin/env python
import os
import sys
import re


NAMESPACE_PATTERN = re.compile('[A-Z]\w+/\w+')


def get_namespaces_from_page(file_handle):
    src = file_handle.read()
    src = src.replace('<br>', '\n')
    return re.findall(NAMESPACE_PATTERN, src)


if __name__ == '__main__':
    trope_dir = sys.argv[1]
    for filename in os.listdir(trope_dir):
        with open(os.path.join(trope_dir, filename)) as f:
            current_namespaces = get_namespaces_from_page(f)
            for i in current_namespaces:
                print(i.split('/')[0])
