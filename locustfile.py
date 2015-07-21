#!/usr/bin/python


from locust import HttpLocust, TaskSet, task

token = 'NDRhY2U3ZjYtNDY1OC00N2QzLWFkNzEtM2E5NGQ1NmM3YTUx'

class MyTaskSet(TaskSet):
    @task
    def index(self):
	headers={"Content-Type": "application/json",
        "Authorization" : "Bearer (%s)" % (token) }
        self.client.patch("/services/avid.iam/tokens/current",headers=headers)


class MyLocust(HttpLocust):
    task_set = MyTaskSet
    min_wait = 5000
    max_wait = 15000
