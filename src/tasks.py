from .celery import app
import random

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

read.apply_async(retry=True)
add.delay(random.randint(0,1),5)
say_hello.delay()