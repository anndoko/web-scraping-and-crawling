# 507/206 Homework 7 Part 1
import requests
import json
from bs4 import BeautifulSoup

#### Your Part 1 solution goes here ####
def get_umsi_data(page):
    #### Implement your function here ####
    # form the link
    baseurl = "https://www.si.umich.edu/directory?rid=All"
    page = "&page=" + str(page)
    url = baseurl + page

    # header
    header = {"User-Agent": "SI_CLASS"}

    # scrap the webpage using BeautifulSoup
    page_text = requests.get(url, headers = header).text
    page_soup = BeautifulSoup(page_text, "html.parser")

    # create an empty dictionary to store the data
    diction = {}

    # get the info: name, title, email
    content_div = page_soup.find(class_ = "view-content")
    title_items = content_div.find_all(class_ = "field-name-title")
    for item in title_items:
        name = item.find("h2").text
        diction[name] = {}

    return(diction)

#### Execute funciton, get_umsi_data, here ####
print(get_umsi_data(4))


#### Write out file here #####
