#!/usr/bin/env python
import urllib.request
import urllib.parse


BASE_URL = "http://tvtropes.org/pmwiki/pmwiki.php/"
URL_QUERY = "?action=source"



def download_page_source(title, namespace="Main"):
    url = BASE_URL + urllib.parse.quote(namespace + '/' + title) + URL_QUERY
    with urllib.request.urlopen(url) as request:
        source = request.read()
    return source
