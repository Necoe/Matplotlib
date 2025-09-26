from matplotlib import pyplot as plt
import random
from matplotlib import font_manager

# 设置字体的方式 无效
# font = {'family': 'MicroSoft YaHei',
#         'weight': 'bold',
#         'size': 'larger'}


# matplotlib.rc("font",**font)

# 另一种设置字体的方法
my_font = font_manager.FontProperties(fname="D:/正楷字体.TTF")

x = range(0,120)
y = [random.randint(20, 35) for i in range(120)]



plt.figure(figsize=(15,8),dpi=80)


# 调整x轴的刻度

_x = list(x)
_xticks_labels = ['10时:{}分'.format(i) for i in range(60)]
_xticks_labels += ['11时:{}分'.format(i) for i in range(60)]

# 取步长，数字和字符串长度一一对应，数据的长度一样
plt.xticks(_x[::3], _xticks_labels[::3],rotation = 45,fontproperties=my_font)  # rotation 旋转的度数




# 添加描述信息
plt.xlabel("时间",fontproperties = my_font)
plt.ylabel("温度 单位（摄氏度）",fontproperties = my_font)
plt.title("10点到12点每分钟温度的变化",fontproperties = my_font)


plt.plot(x,y)
plt.show()