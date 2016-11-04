# -*- coding: utf-8 -*-
"""
Created on Sat Oct 29 18:21:16 2016

@author: Virginia
"""

import requests
import json


#post intial request
headers = {'Content-Type':'application/json'}
url = 'http://challenge.code2040.org/api/prefix' 
data_2 = {"token": "efb1889aaabf1700dbd03ec4fcc27c17"}     
request = requests.post(url, data=json.dumps(data_2), headers=headers)

#parse http response
dic=request.content
dic=dic.decode("utf-8")

#convert the string into dict
dic=json.loads(dic)


#iterate through array and select the words that don't have the prefix in them
#by compairing the first letters of the words in the array with those of the prefix
pre_length=len(dic["prefix"])
p=dic["prefix"]
non_prefix=[]

for word in dic["array"]:
    if word[:pre_length]!=p:
        non_prefix.append(word)
        

#I would need to add some more code if the array given had "words" shorter
#than the prefix given, but this doesn't appear to be needed here

#send non_prefeix back
url_4='http://challenge.code2040.org/api/prefix/validate'
headers={"Content-Type":"application/json"}
answer=requests.post(url_4, data=json.dumps({'token': 'efb1889aaabf1700dbd03ec4fcc27c17', 'array': non_prefix}),headers=headers)
print(answer.status_code, answer.reason)




























