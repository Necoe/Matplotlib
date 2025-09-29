def chNum(x):
    
    print("转换函数：")

    s ={ 1 : 'one', 2: 'two', 3: 'three', 4: 'four'}

    c = s[x]

    return c

x = int(input("输入数字"))

print(chNum(x))