# Downloads Qantas share price beginning 1 January 2020
import yfinance                                           # (1)
tic = "QAN.AX"                                            # (2)
start = '2020-01-01'                                      # (3)
end = None                                                # (4)
df = yfinance.download(tic, start, end, ignore_tz=True)   # (5)
print(df)                                                 # (6)
df.to_csv('qan_stk_prc.csv')                              # (7)

#同时需要两只股票
# Loop
import yfinance
start = '2020-01-01'
end = None

tickers = ["QAN.AX", "WES.AX"] #需要迭代两次
for tic in tickers:
    df = yfinance.download(tic, start, end, ignore_tz=True)
    print(df)
    tic_base = tic.lower().split('.')[0]
    df.to_csv(f'{tic_base}_stk_prc.csv')

print('\n')
print('\t week 5 OS模块')
import yfinance as yf
df = yf.download('aapl',start='2023-01-01')
df.to_csv('AAPL_price.csv')

import os
#用现在的路径想要查看的csv文件用os.path.join()链接起来，就是这个文件的absolute path
current_directory = os.getcwd()
file = os.path.join(current_directory,'AAPL_price.csv')
print(file)

# # # open函数
file_object = open(file='AAPL_price.csv',mode='rt')   #r = read mode 可以把file和mode不写，如果没有special mode就默认rt
#mode参数，可以是一位r，也可以是两位rt
#前面是读取/写作模式，'w'-写入，'r'-读取，'a'-append-不会改变已有数值
#后面是数据类型 't'-text 'b'-binary，这门课都是t
# print(file_object)
# # 调用读取这个对象的方法
contents = file_object.read()
# # string的类型
print(type(contents))
# # 整个string的长度
print(len(contents))
print(contents)
#关闭它
file_object.close()
print(file_object.closed)

#怎么一行一行的看信息
file_object = open('AAPL_price.csv')
for line in file_object:
    print(line)


print('\nNext表示对于一个iterable对象来说，接下来的信息')
#Next
file_object = open('AAPL_price.csv')
#第一次next代表第一行
fobj = next(file_object)
print(fobj)
#第二次next代表第二行
fobj = next(file_object)
print(fobj)

##Context manager - 最安全的方法，自带close
info = []
file_object = open('AAPL_price.csv')
for line in file_object:
    line = line.strip()  #读取并且去掉空行
    info.append(line)
print(info)

contents = []
with open('AAPL_price.csv') as file_object:   #这时候的file_object相当于file_object = open('AAPL_price.csv')
    for line in file_object:
        line = line.strip()  #因为这个方法每一行都有空行，所以去掉空行
        contents.append(line)  #添加到外面的列表里
    print(file_object.closed)  #在context manager里看文件是否关闭了（以True/False为结果）
                               #会看到False，因为还在里面，文件在工作中
print(file_object.closed)
print(contents)

print('\n相关题型')
#exeption - 手动报错
#lesson = 10
#if lesson == 10:
    #raise Exception #符合条件下会自己报错，并且终止代码运行

print('\n')
#查看一个文件是否存在
import os
condition = os.path.exists('qan_stk_prc.csv')
print(condition)

print('\n')
#查看一个字符串是否包含某些字母
word = 'abcdefg'
a_exists = 'a' in word
print(a_exists)

#设计一个只可以读取文件'r'，不能是'w'/'a'的mode的函数
#粗肥文件不存在，或者文件是空的，才允许'w'/'a'
#知识点：只要函数动用return，整个函数就终止了
def open_only(pth,mode='rt'):  #默认reading text rt
    #第一个提哦啊见：看mode里面的字符串是否有r
    if 'r' in mode: #磨mode= 'r'
        return open(pth,mode=mode) #有r就说明没有'w'/'a'了，然后允许打开，mode就用返回参数的mode
    #第二个条件是看mode是否有'w'/'a'
    elif 'w' in mode or 'a' in mode:
        #有的话就进入下一个条件 （有多个，注意缩进）

        #里面的第一个条件是，要是路径不存在这个文件，就允许用含有'w'/'a'demode的open（）
        if not os.path.exists(pth):
            return open(pth,mode=mode)
        #里面的第二个条件是存在，存在就读取里面的内容
        elif os.path.exists(pth):
            contents = open(pth,mode='rt')  #先用'rt'来读取
            length = len(contents.read())  #.read()把内容集中在一个string内，看长度

            #注意这里又有一层条件判断内容的长度
            #文件存在，但没有内容，允许'w'/'a'
            if length == 0:
                return open(pth,mode=mode)
            #文件存在，也有内容，就不允许'w'/'a'，报异常
            else:
                raise Exception
#file = open_only('wes_stk_prc.csv',mode='r') #没报错，说明成功
#file = open_only('wes_stk_prc.csv',mode='w') #报错
#file = open_only('finance.csv',mode='w') #不报错，因为不存在，当你运行后，就会自动生成一个空的文件





