#!/usr/bin/python

import os
import sys
import requests
import time
import datetime as dt
import json

#token = str(sys.argv[1])
token = 'NDRhY2U3ZjYtNDY1OC00N2QzLWFkNzEtM2E5NGQ1NmM3YTUx'
url = 'api-stg1.us-east-1.everywhere.avid.com'
headers={"Content-Type": "application/json",
        "Authorization" : "Bearer (%s)" % (token) }
r = requests.patch("https://api-stg1.us-east-1.everywhere.avid.com/services/avid.iam/tokens/current",headers=headers)
print r.status_code
rdate = r.content.split(',')
print rdate[0], rdate[7]


#date = dt.date.today()
#data = {"alias" : "$date",
#	"kind" : "asset" }
#data = json.dumps(data)
r = requests.delete("https://api-stg1.us-east-1.everywhere.avid.com/services/avid.asset/assets/633413ac-0b5f-4c92-93f0-23d3c930348b",headers=headers)
print r.status_code
print str(r.content)
