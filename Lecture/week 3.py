# （一）If statement
happy = True
if happy is True:
    print("I am happy")  #空了四格 if的条件满足时，会执行
print("This will print regardless of the value of happy")  #没有空格 无论怎样都会被打出来

# White space： if套if
happy = True
very_happy = True

if happy is True:
    print("I am happy")                         # <-- four-spaces indentation
    if very_happy is True:                      # <-- four-spaces indentation
        print("Actually, I'm really happy!")    # <-- eight-spaces indentation

#数字
happy = 1 #除了0，任何数字都会被当成True
if happy:
    print("I am happy")
print("This will print regardless of the value of happy")

# Boolean logic 先执行not，然后and，最后执行or。
if not False:
   print("not False is True")

if not True is False:
   print("not True is False")

#（二）
#else           当if条件不满足，会执行else
b = False
if b is True:
   print("b is True")
else:
   print("b is not True")

#elif           第一个判定失败，进行第二个 如果成功即结束，如果失败继续第三个判定 以此类推
a = 0
b = True
if a != 0:
   print("a is non-zero")
elif b is True:
   print("b is True")
elif a < 0 and b is True:
   print("a is negative and b is True")
else:
   print("None of the conditions above hold")


#pass           什么都不做。写了他 不完整的代码不会报错


#（三）：loop
#Tuples
for v in ('string', True, 1):
    print(v)
#Sets
tickers = set()
tickers.add("QAN.AX")
tickers.add("QAN.AX")
tickers.add("WES.AX")
for tic in tickers:
    print(tic)



#（四）；Range
#The first version is range(start, stop[, step])
for i in range(0, 5):
    print(f"i is now {i}")
#等同于
for i in range(0, 5, 1):
    print(f"i is now {i}")
#间隔2
for i in range(0, 5, 2):
    print(f"i is now {i}")


#（五）：Enumerations     相比range，会加上位置信息
letters = ["a", "b", "c", "d", "e"]
for tup in enumerate(letters):
    print(tup)
#可以加上位置的起止信息
letters = ["a", "b", "c", "d", "e"]
for tup in enumerate(letters,start = 1000):
    print(tup)


#课上练习 找出序列中的最大值： number = [3,9,1,5,7,2,11,0,3,12,3,15]
numbers = [3,9,1,5,7,2,11,0,3,12,3,15]
temp_largest = None
print('Before', temp_largest)

for number in numbers:
    if temp_largest is None:
        temp_largest = number
    elif number > temp_largest:
        temp_largest = number
    print(number,temp_largest)
print(f'The largest value is {temp_largest}')


#（六）while loop：只要条件满足会一直运行下去
the_sum = 0
for i in range(1,101):
   the_sum = the_sum + i
print(the_sum)
#（七）：Nested structures and conditional statements 嵌套 注意空格
years = [2018, 2019, 2020]
months = [
    "Jan",
    "Feb",
    "Mar",
    "Apr",
    "May",
    "Jun",
    "Jul",
    "Aug",
    "Sep",
    "Oct",
    "Nov",
    "Dec",
    ]

for year in years:
   for month in months:
       print("Year: {}, Month: {}".format(year, month))

#（八）：continue 为跳出这次迭代进入下一个迭代（仍在loop中）；break 为跳出loop，是执行loop后的语句
#continue 在后 打出来都是奇数
for i in range(1,10):
    if i % 2 == 1: # i is odd
        print(i)
        continue
#continue 在前 打出来是偶数
for i in range(1,10):
    if i % 2 == 1:
        continue
    print(i)
#break
for even in range(0,10,2):
    print(even)
    if even > 2:
        break


#(九）Funtion：用def定义
#功能就是把QAN.AX打出来
def qan_tic():  #()里面放参数
    tic = 'QAN.AX' #下面三行都是运行内容
    print(tic) #执行这个function时会执行的任务
    return tic #定义了返回值
res = qan_tic() # call the function
#带参数
# def mk_csv_name(tic):
#     tic = tic.lower()
#     tic_base = tic.split('.')[0]
#     csv_name = f'{tic_base}_stk_prc.csv'
#     return csv_nam


#（十）Comprehensions
# Create a list with 1～10
L = [x for x in range(10+1)]
print(L)
# Create a list with all even integers from 0 to 1 million
evens = [x for x in range(1_000_000 + 1) if x % 2 == 0]
print(evens[:10])
# Dictionary comprehensions
pairs = [
  ('a', 1),
  ('b', 2),
  ('c', 3),
  ]
dic = {key:value for key,value in pairs}
print(dic)
#Set comprehensions
dic = {'a': 1, 'b': 2, 'c': 3}
keys = {key for key in dic}# Create a set comprehension with the keys from `dic`
print(f'The type of {keys} is {type(keys)}')
