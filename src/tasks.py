from celery import Celery
import random

app=Celery('tasks',broker='amqp://localhost//')

@app.task
def reverse(string):
    return string[::-1]

@app.task()
def say_hello():
    print("Hello Celery")

@app.task
def add(x,y):
    return x+y

@app.task
def read():
    print("yo")
    file=open("src/read.txt","r")
    if file.readline() is None:
        print("Finished.")
