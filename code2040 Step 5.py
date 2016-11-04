# -*- coding: utf-8 -*-
"""
Created on Wed Nov  2 20:35:07 2016

@author: Virginia
"""
import json
import requests
import dateutil.parser
from datetime import datetime, timedelta

#send intial request
headers = {'Content-Type':'application/json'}
url = 'http://challenge.code2040.org/api/dating' 
data_2 = {"token": "efb1889aaabf1700dbd03ec4fcc27c17"}     
request = requests.post(url, data=json.dumps(data_2), headers=headers)
print(request.status_code, request.reason)


#parse http response
dic=request.content
dic=dic.decode("utf-8")

#convert the string into dict
dic=json.loads(dic)

#convert time to useable time form
time = dateutil.parser.parse(dic['datestamp'])

#add original time and time delta together
new_time = time + timedelta(seconds= dic['interval'])

#convert new time back into rcf3339 format
final_time = datetime.isoformat(new_time)[:-6] + "Z"


#post final request
url_5='http://challenge.code2040.org/api/dating/validate'
data_5= {"token": "efb1889aaabf1700dbd03ec4fcc27c17", "datestamp": final_time}
answer= requests.post(url_5, data=json.dumps(data_5), headers=headers)
print(answer.status_code, answer.reason)