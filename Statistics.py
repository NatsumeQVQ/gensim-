from collections import Counter
f = open('问题_分词.csv','r',encoding='utf_8_sig')
target = open('统计.txt','w',encoding='utf-8')
line = f.readline()
while line:
    words = line.split(',',4)[4].split(' ')
    result = Counter(words)
    line = f.readline()
    line = f.readline()
    line = f.readline()
    target.writelines(str(result)+'\n')
f.close()
target.close()