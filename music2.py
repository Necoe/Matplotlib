import os
import random


guess = 0
i = 0
num = random.randint(1,8)

fname = "D:\music\基本音阶"+ str(num)  + ".mp3"
os.system(fname)


while guess != num:
    i += 1


    guess = int(input("请输入你猜测的音阶："))

    if guess != num:
        print("猜错了，重新输入")
    else:
        print("猜对了")
print("你一共回答了{}次".format(i))







    