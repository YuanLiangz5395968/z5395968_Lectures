happy = True # <-- This is now True
if happy is True:
 print("I am happy")
print("This will print regardless of the value of happy")

hours = input('Enter number of hours you worked this week: ')
hours = int(hours)
normal_rate = 51.45
overload_rate = 88.9
if hours > 35 :
 pay = (35 * normal_rate) + ((hours - 35) * overload_rate)
else :
 pay = hours * normal_rate
print(f'This weekly payment is: {pay}')

# numbers = [3, 9, 1, 5, 7, 2, 11, 0, 3, 12, 3, 15]
# temp_largest = numbers[0]
# print('Before', temp_largest)
# for number in numbers:
#  if number > temp_largest:
#  temp_largest = number
#  print(number, temp_largest)
# print(f'The largest value is {temp_largest}')

numbers = [3, 9, 1, 5, 7, 2, 11, 0, 3, 12, 3, 15]
largest = max(numbers)
print(f'The largest value is {largest}')

# for i in range(1, 4):
#  for j in range(1, 4):
#  if i <= j:
#  print(i, j)

 # the_sum = 0
 # for i in range(1, 101):
 #     if i % 2 == 0:
 #         continue
 #     if i % 3 == 0:
 #         continue
 #     if i % 7 == 0:
 #         continue
 #     if i % 13 == 0:
 #         continue
 #     print(f' the_sum is {the_sum}')
 #     the_sum = the_sum + i
 # print(f'Sum is {the_sum}')