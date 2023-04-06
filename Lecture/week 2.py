#一. Namespaces
#(1) Global
x = 1 #定义x
print(x) #单独运行这一行 会报错
#(2) Build-in
print #不会报错
x = str('abc') #x = 'abc' 是他的捷径
print(x)



#(二)Method
x = str.upper('abc') #从class中调用
print(x)
y = 'abc'.upper() #从instance中调用
print(y)
#方法1
weird_case = 'My fUnNy TyPecASe sTRiNg'
weird_case_lower = weird_case.upper().lower() #从upper转化成lower
print(weird_case_lower)
#方法2
weird_case = 'My fUnNy TyPecASe sTRiNg'
weird_case_fn = weird_case.lower
print(weird_case_fn())



#(三) method中的参数
#my_method(para1,[para2],para3=0,*para4.**para5)
#以上method有五个参数：
#para1；直接写出来为required
#[para2]:方括号内的为optional 可有可无
#para3=0: 有赋值
#*para4、**para5: 前面有一个或两个星号的为多值参数



#（四）Formatting strings       有两种方法可以将变量中得知带入string中
a = True
b = 5
#方法一
print(f'The value of a is {a} and the value of b is {b}')
#方法二
print('The value of a is {} and the value of b is {}'.format(a,b))



#（五） List 是有序的，可更改数据结构
#list的创建
lst = [1,'string',True,None]

#list中可以包含另一个list
lst_a = [1,'string',True,None]
lst_b = ['a',lst_a]

#用以下方式创建空list
empty_list = []
mot_empyu_lst = [None]

#捷径
lst = list[1,2,3] #lst = [1,2,3]是捷径

#slice
# P  y  t  h  o  n
# 0  1  2  3  4  5
#-6 -5 -4 -3 -2 -1
lst = ['p','y','t','h','o','n']
print(lst[1:4]) #取到4的前一位
print(lst[-5:-2]) #取到-2前一位
print(lst[:3])
print(lst[0:100000])

#添加                         append
lst_a = [1]#方法一
list.append(lst_a, 2)
print(lst_a)
lst_a = [1]#方法二
lst_a.append(2)
print(lst_a)

#合并                         extend
lst_a = [1]
lst_b = [2,3]
lst_a.extend(lst_b)
print(lst_a)

#插入                         insert
lst = [1, True, None]
print(f'lst is originally {lst}')
lst.insert(1,'string')
print(f'After insertion, lst is now {lst}')

#删除                         remove\pop
lst = ['string',True,None,True] #方法一
print(f'lst is originally {lst}')
lst.remove(True)
print(f'lst after removing the first True is {lst}')

lst = ['string',True,None,True] #方法二
print(f'lst is originally {lst}')
lst.pop(1)
print(f'lst after removing the element currently at index 2 is {lst}')

#算长度                        len
lst = ['string',True,None,True]
no_of_items = len(lst)
print(f'lst has {no_of_items} items')



#（六）Tuples 固定长度，不可更改内容的序列
#Tuple的创建，index，slice的方法与list一致，不过用圆括号
#pack是Tuple的创建 unpack是将Tuple中的item单独分散开
tup = (1, 2)
(a, b) = tup
print(f"'a' is {a} an 'b' is {b}")



#(七) Set 无序 不重复
s = {1,2,3,4,5,5,5,5,}
print(s)
#可以用 add和remove修改set的内容;  可以用len测长度
#可以用 in 和 not in 判断某个体是否存在于set中
s = {1, 2, 3}
print(1 in s)
print(4 in s)
print(1 not in s)
print(4 not in s)

