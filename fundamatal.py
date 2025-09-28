x = ['a', 'b', 'c', 'd', 'e', 'f']

# 切片操作不改变原列表
print(x[: : -1])
print(x)

# reverse 方法改变原列表
x.reverse()

print(x )


# range() 也可以使用负数步长
for i  in range(10,0,-1):
    print(i )

shici = "桃花怒放千万朵，色彩鲜艳红似火。这位姑娘嫁过门，夫妻美满又和顺"


# 序列元素都可以用[]下标切片的方式 和 in 函数，len操作
print(shici[0:7])
shici[::-1]
print(len(shici ))

print(shici * 2)

# 字符串和列表的区别：
"""
    1.列表元素可以是任何类型，而字符串只能包含字符
    2.列表元素可以被替换修改，字符串的内容不可修改
"""


s = "bai li is amazing"
s_change = s.replace('b','a')

# 为什么reverse方法永久改变列表，但是字符串的replace不会永久改变字符串
# list 是可变对象
# str 是不可变对象
print(s)


# 字符串的查找与统计
# count 方法  统计某个字符的个数  （为什么叫方法不叫函数呢？因为只有object才有方法，对象）
print(s.count('a'))

# find 返回第一个字符串符合的下标 
# 如果要找的字符串不存在，则返回-1
print(s.find('a'))














