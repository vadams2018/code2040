# -*- coding: utf-8 -*-
"""
Created on Sat Oct 29 17:59:02 2016

@author: Virginia
"""


import requests
import json


#send intial request
headers = {'Content-Type':'application/json'}
url = 'http://challenge.code2040.org/api/haystack' 
data_3 = {"token": "efb1889aaabf1700dbd03ec4fcc27c17"}     
request = requests.post(url, data=json.dumps(data_3), headers=headers)

#parse http response
dic=request.content
dic=dic.decode("utf-8")

#convert the string into dict
dic=json.loads(dic)

#iterate through haystack to find needle while keeping track of index(location)
for i in range(len(dic["haystack"])):
    if dic["haystack"][i]==dic["needle"]:
        index=i

#send needle location back
url_2= 'http://challenge.code2040.org/api/haystack/validate'
headers = {"Content-Type":"application/json"}
answer=requests.post(url_2, data=json.dumps({"token": "efb1889aaabf1700dbd03ec4fcc27c17", "needle": index}),headers=headers)
print(answer.status_code, answer.reason)
