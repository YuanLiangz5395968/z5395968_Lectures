#John said: "Let's learn Python together".

# # Using triple quotes
# str1 = '''John said, "Let's learn Python together".''' str2 = """John said, "Let's learn Python together"."""
# # Using backslash to escape the quotation mark
# str3 = "John said, \"Let's learn Python together\"." str4 = 'John said, "Let\'s learn Python together".'


a = 1# This is an integer of value 1
b = 1.0 # This is a float of value 1.0
c = -1# Negative numbers are preceded by a negative sign


i=1
test = i == 1 # --> True
print(test)

f = 0.2 + 0.2 + 0.2
print(f == 0.6) # --> False


import math
f = 0.2 + 0.2 + 0.2
print(math.isclose(f, 0.6)) # --> True

#Booleans: A type for True/False data
x = True # --> boolean representing true y = False # --> boolean representing false
# Less-than and less-than or equal tests
print( 1 < 2 )
print( 2 < 2 )
print( 2 <= 2 )
# Greater-than or greater-than or equal tests
print( 1 > 2 ) # `False`
print( 2 > 2 ) # `False`
print( 2 >= 2 )# `True



# Equality tests
1 == 2 # --> `False`
2 == 2 # --> `True`


i=1
type(i) # -> <class 'int'>
f = 1.0
type(f) # -> <class 'float'>
type(1.) # -> <class 'float'>


#Other example
x=1
print(type(x))# <class 'int'>
xstr = '1'
print(type(xstr))# <class 'str'>
test = x == xstr
print(test) # --> False
print(type(test))# <class 'bool'>


weird_case = "My fUnNy tYpEcAsE sTrInG"
# First convert the string to uppercase:
weird_case_upper = weird_case.upper() # --> "MY FUNNY TYPECASE STRING" # Then, convert the uppercase version to lowercase
weird_case_lower = weird_case_upper.lower() # --> "my funny typecase string"

#you should do
weird_case = "My fUnNy tYpEcAsE sTrInG"
# Convert the string to upper case and then to lower case
weird_case_lower = weird_case.upper().lower() # --> "my funny typecase string"


