import math
import winsound
import os

# python3 中 汉字也是可以作为变量或者函数的名称的，不能直接输出，只能改为字符串输出

name = input("请输入你的名字:")
weight = int(input("请输入重量："))
speed = int(input("请输入速度："))
armor = float(input("请输入armor:"))

power_level = math.log(0.5*weight*speed**2*(1+armor))

print(name, '的战斗力指数是：', power_level)

# if等关键词后面必须有空格
# if、else句尾必须有冒号
# 分支中语句必须整齐缩进（表示从属关系）
# 最好不用tab使用缩进
# 上下句没有从属关系不可以用缩进

if power_level <= 15:
    os.system('start D:\Kuakepan\周杰伦青花瓷.mp3')
else:
    winsound.Beep(int(200*(power_level)), 1000)

print("Over")
