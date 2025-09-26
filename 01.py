import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-5, 5, 50)  #图像展现的距离
y1 = x**2 + 1
y2 = x * 2 + 1

# plt.figure()
# plt.plot(x,y1)

plt.figure(num=3, figsize=(8, 6))  

plt.xlim(-1, 3)
plt.ylim(-2,3)

plt.xlabel('i am x')
plt.ylabel('i am y')


# ticks 单位的小标

# gca 'get current axis'
ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
ax.spines['bottom'].set_position(('data',0))
ax.spines['left'].set_position(('data',0))

new_ticks = np.linspace(-3,3,5)
print(new_ticks)
plt.xticks(new_ticks)
plt.yticks([-2,-1.8,-1,1.22,3],[r'$really\ bad\alpha$',r'$bad$',r'$normal$',r'$good$',r'$really\ good$'])


line1, = plt.plot(x, y2, label = 'straight')
line2, = plt.plot(x, y1, color='red', linewidth=1.0, linestyle='--',label = 'tortuous')
plt.legend(handles = [line1,line2,],labels =['aaa','bbb'] ,loc = 'best')

x0 = 1
y0 = 3
plt.scatter(x0, y0, s=50,color='r')

plt.show()

# figure 的使用


