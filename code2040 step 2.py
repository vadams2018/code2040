# -*- coding: utf-8 -*-
"""
Created on Sat Oct 29 09:30:01 2016

@author: Virginia
"""

import json
import requests 


#send intial request
url = 'http://challenge.code2040.org/api/reverse' 
dic = {"token": "efb1889aaabf1700dbd03ec4fcc27c17"}     
 
headers = {'Content-Type':'application/json'}
request=requests.post(url, data=json.dumps(dic), headers=headers)
print(request.status_code, request.reason)

#parse http response
string=request.content
string=string.decode("utf-8")

#reverse response
reverse=string[::-1]

#send reversed string back
url_2= 'http://challenge.code2040.org/api/reverse/validate'
data_2={"token": "efb1889aaabf1700dbd03ec4fcc27c17", "string": reverse}

answer=requests.post(url_2, data=json.dumps(data_2), headers=headers)
print(answer.status_code, answer.reason)
