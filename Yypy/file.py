f = open('C:/Users/20619/Desktop/新建 文本文档.txt','r',encoding='UTF-8')

p = f.readlines()


# p是列表类型，返回一个大列表，容纳每一个段落
print(p)

# 列表有有序类型，可以用for循环输出
for s in p  :
    if '可' in  s:
        print('ke',s)
    

f.close()
