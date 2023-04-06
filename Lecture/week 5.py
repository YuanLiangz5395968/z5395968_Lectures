#查询列表中带条件的字符串
#目标：找e开头的字符串

list_b = ['apple','new','nenb','arq','caeg','dawge','efga','efza']
words_start_with_e = [] #创建新列表，存储e开头的词

# # # 方法一
for word in list_b:
    if word[0] == 'e':   #index方法 看首字母是否为e
        words_start_with_e.append(word)
print(words_start_with_e)

#print('apple'.startwih('a')) ###判断字符串apple是否以a开头  是就会返回True

# # # 方法二
for word in list_b:
    if word.startswith('e'):   #string方法：只要开头是e，就返回true，因此会执行下面命令
        words_start_with_e.append(word)
print(words_start_with_e)

print('\n')



#目标：找ef开头的字符串
words_start_with_ef = []
for word in list_b:
    if word[0:2] == 'ef':   #index方法 看首字母是否为e
        words_start_with_ef.append(word)
print(words_start_with_ef)
print('\n')



print('\t OS模块') #tap
#toolkit 23-132

print('\t Pandas') #tap
import pandas as pd
