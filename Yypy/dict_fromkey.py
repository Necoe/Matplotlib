def count_words(file, words):
    d = dict.fromkeys(words,0)

    f = open(file,'r',encoding='utf-8')

    for s in f.readlines():
        for name in d:
            d[name] = d[name] + s.count(name)

    f.close()
    return d


n = ['民可','不可']

r = count_words("C:/Users/20619/Desktop/新建 文本文档.txt",n)

print(r)


def get_words(file1,file2):

    # 读取传入的文件
    f = open(file1,'r')

    words=[]

    # 分隔每一个单词
    for s in f.readlines():
        s = s.replace(',',' ')
        s = s.replace('.',' ')
        s = s.replace('-',' ')
        s = s.lower()

        # 将分割的每行单词串给line_words
        line_words = s.split(' ')

        print(line_words)

        words.extend(line_words)

    # 删除重复的元素
    words = set(words)
    words = list(words)

    f2 = open(file2,'w')
    f2.write('\n'.join(words))
    f2.close()


get_words("C:/Users/20619/Desktop/en_test.txt", "C:/Users/20619/Desktop/新建 文本文档.txt")

