#!/usr/bin/env python
import urllib.request
import urllib.parse
import re


BASE_URL = "http://tvtropes.org/pmwiki/pmwiki.php/"
URL_QUERY = "?action=source"
DEEP_LINK_PATTERN = re.compile('/Tropes.To.')


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
    page_src = page_src.split('----')[1]
    page_lines = page_src.split('<br>')
    return [sanitize_link(i) for i in page_lines if i.startswith('*')]


def check_deep_link(link_txt):
    return DEEP_LINK_PATTERN.search(link_txt) is not None


def deep_get_entries_from_page(page_src):
    links = get_entries_from_page(page_src)
    # TODO: I think we don't need a loop here, because links are not nested that much
    deep_links = [i for i in links if check_deep_link(i)]
    for i in deep_links:
        deep_page_src = download_page_source(i.split('/')[1], i.split('/')[0])  # TODO: it's ugly
        links.extend(get_entries_from_page(deep_page_src))
    links = [i for i in links if not check_deep_link(i)]
    return links
