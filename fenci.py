import jieba
import csv
name = '问题'
f = open('{}.csv'.format(name),'r',encoding='utf_8_sig')
target = open('{}_分词.csv'.format(name),'w',encoding='utf_8_sig')
writer = csv.writer(target)
line = f.readline()
count = 1
while line:
    line_list = line.split(',', maxsplit=4)
    line_list[4] = ' '.join(jieba.cut(line_list[4]))
    writer.writerow(line_list)
    print('------------',count,'------------')
    count += 1
    line = f.readline()
    line = f.readline()
f.close()
target.close()