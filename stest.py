#!/usr/bin/python

import os
import sys
import requests
import time
import datetime as dt
import json

#token = str(sys.argv[1])
token = 'YmUyMjBkYzktMDM3OC00ZWYxLTljOTUtZGY5MzYzYzU4ZDk3'
stgurl = 'api-stg1.us-east-1.everywhere.avid.com'


#RENEW TOKEN
############
url = 'https://%s/services/avid.iam/tokens/current'
headers={"Content-Type": "application/json",
        "Authorization" : "Bearer (%s)" % (token) }
r = requests.patch(url=str(url) % (stgurl),headers=headers)
#print r.status_code
resp = json.loads(r.content)
identity = resp["entity"]["identityId"]
print identity
print "\n"
#CREATE ASSET
#############
url = 'https://%s/services/avid.asset/assets'
data = {"alias" : "$date",
	"kind" : "asset" }
data = json.dumps(data)
r = requests.post(url=str(url) % (stgurl),data=data,headers=headers)
#print r.status_code
resp = json.loads(r.content)
assetId = resp["assetId"]
print assetId
print "\n"
#DELETE ASSET
#############
url = 'https://%s/services/avid.asset/assets/%s'
r = requests.delete(url=str(url) %(stgurl,assetId),headers=headers)
#print r.status_code
print str(r.content)
print "\n"
