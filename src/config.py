from celery import Celery
import random

app = Celery('tasks',
             broker='amqp://guest@localhost//',
             backend='amqp://guest@localhost//',
             include=['tasks'] 
             )