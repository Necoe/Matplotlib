import os
import time
import random

i = 1
while i <= 7:

    num = random.randint(1,8)

    loc = "D:\music\基本音阶"+str(num)  +".mp3"
    os.system(loc)

    time.sleep(1)

