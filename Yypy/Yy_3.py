print('欢迎进入会员录入系统，请开始录入')

s = 'y'


# 循环条件的变量要事先赋值
# 循环体统一缩进
# 循环避免死循环

while s == 'y':
    i = 0
    total = 0

    house_num = int(input('输入房产数量'))

    if house_num > 3:
        print('gaoji ')
    elif house_num > 1:
        print('huiyuan')
    else:
        print('putong')

    i += 1
    total += house_num
    s = input('请问是否继续录入(y/n)')

print("计数器i的值为:",i)
print("累加器total的值为:", total)
print('程序结束')
