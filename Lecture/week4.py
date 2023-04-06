#一. Comprehensions
#[i for i in iterable if condition]
# Eg1:Create a list with all odd integers from 1 to 30
odd_list = [i for i in range(1,31) if i % 2 != 0]
print(odd_list)

#Eg2: assenment Ban:98,Ann:95,Leo:98, Dan:96. 做成List并且排序
assessment = {'Ban': 98,'Ann': 95,'Leo': 98,'Dan':96}
names = sorted([key for key in assessment.keys()])
print(names)

#Extract(key,value) pairs as tuples and put into a list
#正常方法：
pairs = []
for key,value in assessment.items():
    pairs.append((key,value))
print(pairs)
#comprehension:
pairs = [(key,value)for key,value in assessment.items()]
print(pairs)

#Eg3:creat a new list given a condition on other data structure
num_set = {1,2,3,4,5,6} #注意这是一个set集合 创建一个element是他们平方的一个new list
squares = [i**2 for i in num_set]
print(squares)

#Set comprehension
dic_a = {'one':1,'two':2,'three':3}
#key 集合
key_set = {key for key in dic_a.keys()}
print(key_set)
#value集合
values_set = {value for value in dic_a.values()}
print(values_set)



#二. Dictionary comprehension
#Eg1.
# #update dictionary
assessment = {}
update = [('Ban', 98), ('Carot', 95),('Ann', 95)]
#for loop
for name, mark in update: #因为列表里每个元素都是tuple(key,value), 我们的for loop要用两个variable
    print(name,mark)
#comprehension
#方法1
update_dict = {name:mark for name, mark in update}
print(update_dict)
#方法2
assessment.update({name:mark for name,mark in update})
print(assessment)

#Eg2:creat a new dictionary without apple
prices = {'apple':5,'banana':6,'orange':3,'melon':7}
new_dictionary = {key: value for key,value in prices.items() if key != 'apple'}
print(new_dictionary)

#Eg3:Modity key and value
#replace "sun" to "sat"
days = {'Mon':1,'Tue':2,'Wed':3,'Thur':4,'Fri':5,"Sun":6}
days['Sat'] = days.pop('Sun')
print(days)



#三.generator ---not cover
tup = (i for i in range(10))
print(tup)
print(type(tup))
print(sum(tup))



#四.Function
def func(a,b,c):
    return a+b+c
#一般调用
print(func(1,2,3))
#用字典存储要输入的参数 然后再调用函数
params = {'a':1,'b':2,'c':3}
print(func(**params))

#Eg1
def func_1(a):
    a = a**2 #赋值为参数a的平方
    return a #返回a的平方作为结果

a = 3 #global--定义在函数外
func_1(a) #调用了函数,虽然又返回结果，但没有变量
print(a) #a取的还是在函数外定义的值
#
a = 3
a = func_1(a) #这是就是对a重新赋值了
print(a)

#Eg2:
def func_1():
    res = func_2()
    print(res)
#func_1() #如果在这里运行，会报错。因为从上往下 python无法识别

def func_2():
    return 10
func_1() #在这里运行就可以识别了



# function complex example
#Eg1：make string in upper letters
s = "Hello World"
s = s.split(' ')
print(s)
s = [word.upper() for word in s]
print(s)
#设计一个公示，可以大写所有字幕
def upper_word(string):
    string = string.split(' ')
    string = [word.upper() for word in string]
    return string

print(upper_word('Hi class')) #一个函数的构造可以反复使用

#Eg2：select words based on index in a list
long_sentance = 'I have  very interesting class tomorrow'
long_sentance = long_sentance.split(' ')
print(long_sentance)

#用comprehension挑选选定位置的字母
words_selected = [element for index,element in enumerate(long_sentance) if index % 2 != 0]
print(words_selected)

#Eg3: cumulative sun based on conditions:give a range 0~30(inclusive),add to sum only if divisable by 3
s = 0
for i in range(31):
    if i % 3 == 0:
        s = s + i
print(s)



#特殊字符  unicode
print('\n') #new line
print('\t') #tap
print('\t apple')
print('\u00A9')  #copyright