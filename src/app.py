from tasks import *

result=add.delay(2,3)
if result.ready:
    print(result.get())