Configurations steps:
1.Install rabbitmq-server
-sudo apt-get install rabbitmq-server
2.Install Celery
-pip install celery

3.Afer creating tasks.py and celery.py files and writing some tasks and configs,run following command to run worker
-celery -A tasks worker --loglevel=info