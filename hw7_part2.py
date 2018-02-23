# 507/206 Homework 7 Part 2
import json

count = 0
#### Your Part 2 solution goes here ####
f = open("directory_dict.json", "r") # open the file
data_dic = json.load(f) # load the json string and convert it to a python dictionary
for dic in data_dic.items():
    name, info_dic = dic # unpack the tuple
    if info_dic["title"] == "PhD student":
        count += 1
f.close() # close the file

#### Your answer output (change the value in the variable, count)####
print("The number of PhD students: ", count)
