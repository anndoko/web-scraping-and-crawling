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
        # access the existing data
        print("Getting cached data...")
        return CACHE_DICTION[unique_ident]
    else:
        print("Making a request for new data...")
        # make the request and cache the new data
        resp = requests.get(url, headers=header)
        CACHE_DICTION[unique_ident] = resp.text # only store the html
        dumped_json_cache = json.dumps(CACHE_DICTION)
        fw = open(CACHE_FNAME,"w")
        fw.write(dumped_json_cache)
        fw.close() # Close the open file
        return CACHE_DICTION[unique_ident]

# ---------- Class ----------
class Member:
    def __init__(self, name, title, email):
        self.name = name
        self.title = title
        self.email = email

def get_umsi_data(page):
    #### Implement your function here ####
    # form the link
    baseurl = "https://www.si.umich.edu"
    page = "/directory?rid=All&page=" + str(page)
    url = baseurl + page

    # scrap the webpage using BeautifulSoup
    page_text = make_request_using_cache(url)
    page_soup = BeautifulSoup(page_text, "html.parser")

    # get the Contact Detail links
    content_div = page_soup.find(class_ = "view-content")
    links_items = content_div.find_all(class_ = "field-name-contact-details")

    results_lst = []
    for item in links_items:
        url_node = item.find("a")["href"] # get the node
        details_url = baseurl + url_node # form the link
        details_page_text = make_request_using_cache(details_url)
        details_page_soup = BeautifulSoup(details_page_text, "html.parser")

        # get the name
        name_section = details_page_soup.find(class_ = "field-name-title")
        name = name_section.find("h2").text

        # get the title
        title_section = details_page_soup.find(class_ = "field-name-field-person-titles")
        title = title_section.find(class_ = "field-item even").text

        # get the email
        email_secntion = details_page_soup.find(class_ = "field-name-field-person-email")
        email = email_secntion.find("a")["href"]

        # create an instance
        results_lst.append(Member(name, title, email))

    return results_lst # return the dictionary


#### Execute funciton, get_umsi_data, here ####
umsi_titles = {}
for i in range(6): 
    for result in get_umsi_data(i):
        umsi_titles[result.name]  = {
            "title": result.title,
            "email": result.email
        }

#### Write out file here #####
print("Creating a file...")
umsi_data_file = open("directory_dict.json", "w") # create a json file
umsi_data_file.write(json.dumps(umsi_titles, indent = 4)) # dump the dicitonary, format it with indents
umsi_data_file.close() # close the file
print("The file has been created successfully.")
