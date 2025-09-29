# s = "倒背如流"

# s = s[::-1]
# print(s)

# 找李白
s = input("请输入诗句，我帮你来找李白：")

if "李白" in s:
    print('yes')
else:
    print('no')

s = s.replace('a', 'b')

print(s)


x = ['人生啊,','到底该如何过','人生啊,','又能有几轮']

k = '+'

print(k.join(x))