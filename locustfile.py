#!/usr/bin/python


from locust import HttpLocust, TaskSet, task
import json
import requests

token = '{TOKEN}'
stgurl = 'api-stg1.us-east-1.everywhere.avid.com'

class MyTaskSet(TaskSet):
    @task(2)
    def task1(self):
	headers={"Content-Type": "application/json",
        "Authorization" : "Bearer (%s)" % (token) }
        self.client.patch("/services/avid.iam/tokens/current",headers=headers)

    @task(1)
    def task2(self):
        headers={"Content-Type": "application/json",
        "Authorization" : "Bearer (%s)" % (token) }
	url = 'https://%s/services/avid.asset/assets'
	data = {"alias" : "$date",
        	"kind" : "asset" }
	data = json.dumps(data)
	r = requests.post(url=str(url) % (stgurl),data=data,headers=headers)
	resp = json.loads(r.content.decode())
	assetId = resp["assetId"]
	url = 'https://%s/services/avid.asset/assets/%s'
	r = requests.delete(url=str(url) %(stgurl,assetId),headers=headers)


class MyLocust(HttpLocust):
    task_set = MyTaskSet
    min_wait = 5000
    max_wait = 15000
