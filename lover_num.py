from matplotlib import pyplot as plt
from matplotlib import font_manager


font = font_manager.FontProperties(fname="D:/正楷字体.TTF")

x = range(11, 31)

y = [1, 0, 1, 1, 2, 4, 3, 2, 3, 4, 4, 5, 6, 5, 4, 3, 3, 1, 1, 1]

y_deskmate = [1, 0, 3, 1, 2, 2, 3, 3, 2, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1]


plt.figure(figsize=(15, 8), dpi=80)

plt.plot(x, y, label='自己', linestyle='--', linewidth=1, alpha=0.5,color = "#e30fff")

plt.plot(x, y_deskmate, color='r', label='同桌', linestyle=':')


# 设置x的刻度
_xticks_labels = ["{}岁".format(i) for i in x]

plt.xticks(x, _xticks_labels, fontproperties=font)
plt.yticks(range(0, 8))

# 绘制网格 可以发现网格是跟随x、y的刻度来绘制的。
plt.grid(alpha=1,linestyle = '-.')


plt.xlabel("年龄", fontproperties=font)
plt.ylabel("女朋友个数", fontproperties=font)
plt.title("某男子女朋友个数随年龄变化", fontproperties=font)


plt.legend(prop=font, loc=0)
plt.show()
