from config import app

@app.task
def reverse(string):
    return string[::-1]

@app.task()
def say_hello():
    print("Hello Celery")

@app.task
def add(x,y):
    return x+y

