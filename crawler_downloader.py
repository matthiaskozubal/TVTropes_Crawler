#! python3
import crawler_functions
import string
from time import sleep

# CONSTANTS
CRAWL_PAUSE = 1

# Main Page
page_src = crawler_functions.download_page_source("Tropes")
subindex_list  = crawler_functions.get_subindexes_from_index(page_src) # initial list of subindexes

# Subindexes from Main Page
trope_list = []
checked_subindex_list = [] 
for subindex in subindex_list:
    print('Current subindex page: ' + subindex)    
    page_src = crawler_functions.download_page_source(subindex)
    sleep(CRAWL_PAUSE)   
    
    # Subindexes
    current_page_subindex_list = crawler_functions.get_subindexes_from_index(page_src) # gets subindexes from current page    
    if current_page_subindex_list is None:
        print('IndexError for page: ' + subindex)
        exit(1)
    for current_page_subindex in current_page_subindex_list:
        if current_page_subindex not in subindex_list:
            subindex_list.append(current_page_subindex)
    subindex_list.remove(subindex)
    checked_subindex_list.append(subindex)
    
    # Tropes
    current_tropes = crawler_functions.get_tropes_from_page(page_src)
    crawler_functions.catch_exception('A', current_tropes, subindex)
    trope_list.extend(current_tropes) # gets tropes
    # TODO: some subindexes (e.g. Opera) are already Tropes, we need function to check if a page is already a Trope
    
    # Write to file list of checked subindexes
    with open('checked_subindex_list.txt', 'w') as output_checked_subindex_list:
        output_checked_subindex_list.write('\n'.join(sorted(checked_subindex_list)))
    # Write to file list of checked subindexes
    with open('trope_list.txt', 'w') as output_trope_list:
        output_trope_list.write('\n'.join(sorted(trope_list)))
    # visual check
    # print('\n'.join(sorted(trope_list[0:9])))
    # print('\n'.join(sorted(checked_subindex_list)[0:9])))






