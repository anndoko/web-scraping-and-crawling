# 507/206 Homework 7 Part 1
import requests
import json
from bs4 import BeautifulSoup

#### Your Part 1 solution goes here ####
# ---------- Caching ----------
CACHE_FNAME = "cache.json"
try:
    cache_file = open(CACHE_FNAME, "r")
    cache_contents = cache_file.read()
    CACHE_DICTION = json.loads(cache_contents)
    cache_file.close()
except:
    CACHE_DICTION = {}

def get_unique_key(url):
    return url

def make_request_using_cache(url):
    header = {"User-Agent": "SI_CLASS"}
    unique_ident = get_unique_key(url)

    if unique_ident in CACHE_DICTION:
        print("Getting cached data...")
        return CACHE_DICTION[unique_ident]
    else:
        print("Making a request for new data...")
        # make the request and cache the new data
        resp = requests.get(url, headers=header)
        CACHE_DICTION[unique_ident] = resp.text # only store the html
        dumped_json_cache = json.dumps(CACHE_DICTION) # use the json file for the dic (we're not dealing with json but html)
        fw = open(CACHE_FNAME,"w")
        fw.write(dumped_json_cache)
        fw.close() # Close the open file
        return CACHE_DICTION[unique_ident]

def get_umsi_data(page):
    #### Implement your function here ####
    # form the link
    baseurl = "https://www.si.umich.edu/directory?rid=All"
    page = "&page=" + str(page)
    url = baseurl + page

    # scrap the webpage using BeautifulSoup
    page_text = make_request_using_cache(url)
    page_soup = BeautifulSoup(page_text, "html.parser")

    # create an empty dictionary to store the data
    umsi_titles = {}

    # get the info: name, title, email
    content_div = page_soup.find(class_ = "view-content")


    name_items = content_div.find_all(class_ = "field-name-title")
    title_items = content_div.find_all(class_ = "field-item even")

    for item in name_items:
        name = item.find("h2").text
        umsi_titles[name] = {}

    print(umsi_titles)

#### Execute funciton, get_umsi_data, here ####
get_umsi_data(1)



#### Write out file here #####
