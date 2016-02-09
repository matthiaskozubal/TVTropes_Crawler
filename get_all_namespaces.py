#!/usr/bin/env python
import os
import sys
import re


NAMESPACE_PATTERN = re.compile('\[\[folder:.+\]\]')


def get_namespaces_from_page(file_handle):
    src = file_handle.read()
    src = src.replace('<br>', '\n')
    return re.findall(NAMESPACE_PATTERN, src)


if __name__ == '__main__':
    trope_dir = sys.argv[1]
    all_namespaces = []
    for filename in os.listdir(trope_dir):
        with open(os.path.join(trope_dir, filename)) as f:
            current_namespaces = get_namespaces_from_page(f)
            all_namespaces += current_namespaces
    for i in all_namespaces:
        print(i)


