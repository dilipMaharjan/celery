Configurations steps:
1.Install rabbitmq-server(message brokers)
-sudo apt-get install rabbitmq-server
2.Install Celery
-pip install celery
3.Afer creating tasks.py and writing some tasks and configs,run following command to run worker
-celery -A tasks worker --loglevel=info
4.Open up terminal and run python shell
-python (as I have created a virtual environment, I don't need to specify the version of python)
5.Import everything from tasks.py
6.Call any functions from tasks.py and see the async result in the terminal opened by step 3.
