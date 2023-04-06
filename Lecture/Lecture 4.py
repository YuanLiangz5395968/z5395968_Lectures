def qan_tic():
 tic = "QAN.AX"
 print(tic)
 return tic

test_list = [0,1,2,3,4,5,6,7,8,9,10,20,22,23,25,29,30,31]
# def is_even_num(lis):
#  evennum = []
#  for n in lis:
#  if n % 2 == 0:
#  evennum.append(n)
#  return evennum
# is_even_num(test_list)

# Create a dictionary
dic = {'a': 1, 'b': 2, 'c': 3}
# Create a list of (key, val) tuples called `pairs`
pairs = []
for key, value in dic.items():
 pairs.append((key,value))
print(pairs)
#
# # Some data (list of tuples)
# data = [
#  ('a', 1),
#  ('b', 2),
#  ('c', 3),
#  ]
# # Create a dict comprehension
# dic = {k:v for k, v in data}
# print(f'`dic` is {dic}')
# print(f'type(dic) is: {type(dic)}')
# # Create a list comprehension
# lst = [(k, v) for k, v in data]
# print(f'`lst` is {lst}')
# print(f'type(lst) is {type(lst)}')
# # Create a set comprehension
# st = {k for k, v in data}
# print(f'`st` is {st}')
# print(f'type(st) is {type(st)}')
#
# lst = [2, 3, 10, 14, 20, 21, 25, 13, 15]
# new_lst = [x**2 for x in lst if x**2>150]
# print(f'the new list with value of square greater than 150 is {new_lst}')


# numbers = [0, 1, 1, 2, 5, 6, 8, 2, 4, 6, 8]
#
# result = list({i for i in numbers if i % 2 == 0})
#
# result = [i for i in set(numbers) if i % 2 == 0]
#
# result.sort()
# print(result)
#
# import yfinance as yf
# def yf_prc_to_csv(tic, pth, start=None, end=None):
#
#  df = yf.download(tic, start=start, end=end, ignore_tz=True)
#  df.to_csv(pth)
# if __name__ == "__main__":
#  import os
#  tic = 'QAN.AX'
#  datadir = '/home/fintec/pycharm/toolkit/data'
#  pth = os.path.join(datadir, 'qan_stk_prc.csv')
#  yf_prc_to_csv(tic, pth)