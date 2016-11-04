# -*- coding: utf-8 -*-
"""
Created on Sat Oct 29 09:18:36 2016

@author: Virginia
"""

import json
import requests

url = 'http://challenge.code2040.org/api/register' # Set destination URL here
diction = {"token": "efb1889aaabf1700dbd03ec4fcc27c17", "github":"https://github.com/vadams2018/code2040"}     # Set POST fields here

headers = {'Content-Type':'application/json'}
answer=requests.post(url, data=json.dumps(diction), headers=headers)
print(answer.status_code, answer.reason)