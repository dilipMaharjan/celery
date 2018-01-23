from tasks import *
import datetime 

dt_start=datetime.datetime.now().second
result=add.delay(2,3)
if result.ready:
    for i in range(1,10000):
        print(result.get())
    print("Time taken: {} secs".format(datetime.datetime.now().second-dt_start ))
