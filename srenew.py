#!/usr/bin/python

import os
import sys
import requests
import time

#token = str(sys.argv[1])
token = 'NDRhY2U3ZjYtNDY1OC00N2QzLWFkNzEtM2E5NGQ1NmM3YTUx'

#while True:
headers={"Content-Type": "application/json",
        "Authorization" : "Bearer (%s)" % (token) }
r = requests.patch("https://api-stg1.us-east-1.everywhere.avid.com/services/avid.iam/tokens/current",headers=headers)
#print(str(r.content))
print r.status_code
rdate = r.content.split(',')
print rdate[0], rdate[7]
