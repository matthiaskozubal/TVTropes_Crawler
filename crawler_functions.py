#!/usr/bin/env python
import urllib.request
import urllib.parse


BASE_URL = "http://tvtropes.org/pmwiki/pmwiki.php/"
URL_QUERY = "?action=source"


def sanitize_link(link_txt):
    # + shows a specific bullet
    link_txt = link_txt.replace('+ ', '')
    # * is another kind of bullet
    link_txt = link_txt.replace('* ', '')
    # no parenthesis or colons
    link_txt = link_txt.replace('[[', '').replace(']]', '')
    link_txt = link_txt.replace('{{', '').replace('}}', '')
    link_txt = link_txt.replace(':', '')
    # only the first word
    link_txt = link_txt.split()[0]
    return link_txt


def download_page_source(title, namespace="Main"):
    url = BASE_URL + urllib.parse.quote(namespace + '/' + title) + URL_QUERY
    with urllib.request.urlopen(url) as request:
        source = request.read()
    return source.decode('Windows-1252')


def get_subindexes_from_index(page_src):
    page_src = page_src.split('----')[1]
    page_lines = page_src.split('<br>')
    return [sanitize_link(i) for i in page_lines if i.startswith('+')]


def get_entries_from_page(page_src):
    # TODO: TropesAToC...
    page_src = page_src.split('----')[1]
    page_lines = page_src.split('<br>')
    return [sanitize_link(i) for i in page_lines if i.startswith('*')]
