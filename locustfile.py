#!/usr/bin/python


from locust import HttpLocust, TaskSet, task
import json
import requests

token = 'MWM3NDRmNjAtYWJjZS00YzllLTg2NWItY2VhN2Q2ZjA1ODNh'
stgurl = 'api-stg1.us-east-1.everywhere.avid.com'

class MyTaskSet(TaskSet):
    @task(1)
    def task1(self):
	headers={"Content-Type": "application/json",
        "Authorization" : "Bearer (%s)" % (token) }
        r = self.client.patch("/services/avid.iam/tokens/current",headers=headers)
	url = 'https://%s/services/avid.asset/assets'
	data = {"alias" : "$date",
        	"kind" : "asset" }
	data = json.dumps(data)
	r = self.client.post(url=str(url) % (stgurl),data=data,headers=headers)
	resp = json.loads(r.content.decode())
	assetId = resp["assetId"]
	print assetId
	url = 'https://%s/services/avid.asset/assets/%s'
	r = self.client.delete(url=str(url) %(stgurl,assetId),headers=headers)
	print r

class MyLocust(HttpLocust):
    task_set = MyTaskSet
    min_wait = 5000
    max_wait = 15000
