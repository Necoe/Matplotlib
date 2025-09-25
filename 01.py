import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-1, 1, 50)
y1 = x**2 + 1
y2 = x * 2 + 1

# plt.figure()
# plt.plot(x,y1)

plt.figure(num=3, figsize=(8, 4))
plt.plot(x, y2)
plt.plot(x, y1, color='red', linewidth=1.0, linestyle='--')

plt.xlim(-1, 1.5)
plt.ylim(-2,1.5)

plt.xlabel('i am x')
plt.ylabel('i am y')


# ticks 单位的小标

new_ticks = np.linspace(-1,2,5)
print(new_ticks)
plt.xticks(new_ticks)
plt.yticks([-2,-1.8,-1,1.22,3],[r'$really\ bad\alpha$',r'$bad$',r'$normal$',r'$good$',r'$really\ good$'])

plt.show()

# figure 的使用


