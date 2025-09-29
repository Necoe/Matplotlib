f1 = open("C:/Users/20619/Desktop/en_test.txt", 'r')


# readline 是每个单词分开
# readlines 是每个词分开
p = f1.readlines()

words_all = []

for s in p:
    s = s.replace(',', ' ')
    s = s.replace('.', ' ')
    s = s.lower()
    words_line = s.split(' ')

    words_all.extend(words_line)

    
    print(words_all)
    words_all = set(words_all)
    words_all = list(words_all)
    print(words_all)


words_all.sort()

f2 = open('C:/Users/20619/Desktop/en_word.txt', 'w')
f2.write('\n'.join(words_all))
f2.close()
