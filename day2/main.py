# Data types

# String
# To access character of the string :
print("Hello"[0])
print("Hello"[4])
print("123" + "345")

# Integer
print(123 + 345)
# Can we make our numbers easy to read like this 123,323,000?
# Yes, we can use underscore(_) instead of comma(,)
num1 = 123_323_000
print(num1)

# Float
pi = 3.14159
print(pi)

# Boolean
# starts with capital letter unlike java
print(True, False)

# Type error, type checking and type conversion

# 1) We can not concat int to a string
num = 197
# TypeError: can only concatenate str (not "int") to str
# print("This is " + num + "string" )

# 2) type() function is used  to check the Datatype of the variable
print(type(num))
print(type(123))
print(type("Hello"))
print(type(3.145))

# type conversion
num1 = 1223
print(type(num1))
num1 = str(num1)
print(type(num1))

num1 = float(num1)
print(type(num1))
