a = 4
b = 5

# if a <= b:
#     print(f"{a} is lower than or equal to {b}")
# else:
#     print(f"{a} is greater than {b}")

# if a == b or a < b:
#     print(f"{a} is lower than or equal to {b}")

# else:
#     print(f"{a} is greater than {b}")

# if a != b:
#     print("a and b are not equal")
# if not a==b:
#     print("a and b are not equal")

# if True:
# print("ok")
# if not True:
#     print("ok")


# age = int(input('enter your age: '))
# if age >= 13 and age < 19:
#     print("your are teenager!")
# else:
#     print("some thing else...")

# lower than 13 => kid.
# between 13 and 19 => teenager
# greater than 18 => adult
# age = int(input('enter your age:> '))
# if age < 13:
#     print("you are kid!")
# elif 13 <= age < 19:  # elif age >= 13 and age < 19
#     print("you are teenager!")
# elif age >= 18:
#     print("your are adult!")


# a = 3
# b = 5
# c = 2

# if a < b and a < c:
#     print('a is lower than b and c')

# if a < b or a < c:
#     print('a is lower than b or c')


# user_name = input('enter the user name:> ')
# password = input('enter the password:> ')
# if user_name == 'root' and password == "root":
#     print('you can login now...')

# else:
#     print('user name or password is not correct!')

# if user has two user names:
# user_name = input('enter the user name:> ')
# password = input('enter the password:> ')
# if (user_name == 'root' or user_name == "admin") and password == "root":
#     print('you can login now...')

# else:
#     print('user name or password is not correct!')


# case sensitive
# user_name = input('enter the user name:> ')
# password = input('enter the password:> ')
# if (user_name.lower() == 'root' or user_name.lower() == "admin") and password == "root":
#     print('you can login now...')

# else:
#     print('user name or password is not correct!')


# exercise 1 : analyse this code
# Basic comparisons
# if a < b:
#  print("a is less than b")
# if a > b:
#  print("a is greater than than b")
# if a <= b:
#  print("a is less than or equal to b")
# if a >= b:
#  print("a is greater than or equal to b")
# NOTE: It is very easy to mix when to use == and =.
# Use == if you are asking if they are equal, use =
# if you are assigning a value.
# if a == b:
#  print("a is equal to b")
# Not equal
# if a != b:
#  print("a and b are not equal")
# And
# if a < b and a < c:
#  print("a is less than b and c")
# Non-exclusive or
# if a < b or a < c:
#  print("a is less than either a or b (or both)")
# Boolean data type. This is legal!
# a = True
# if a:
#  print("a is true")
# if not a:
#  print("a is false")
# a = True
# b = False
# if a and b:
#  print("a and b are both true")
# a = 3
# b = 3
# c = a == b
# print(c)


# if -1:
#     print("1")
# if "A":
#     print("A")
# if "":
#     print("A")
# This will not trigger as true because it is zero.
# if 0:
#  print("Zero")
# Comparing variables to multiple values.
# The first if statement appears to work, but it will always
# trigger as true even if the variable a is not equal to b.
# This is because "b" by itself is considered true.
# a = "c"
# if a == "B" or "b":
#  print("a is equal to b. Maybe.")
# This is the proper way to do the if statement.
# if a == "B" or a == "b":
#  print("a is equal to b.")
# Example 1: If statement
# temperature = int(input("What is the temperature in Fahrenheit? "))
# if temperature > 90:
#  print("It is hot outside")
# print("Done")
# Example 2: Else statement
# temperature = int(input("What is the temperature in Fahrenheit? "))
# if temperature > 90:
#  print("It is hot outside")
# else:
#  print("It is not hot outside")
# print("Done")
# Example 3: Else if statement
# temperature = int(input("What is the temperature in Fahrenheit? "))
# if temperature > 90:
#  print("It is hot outside")
# elif temperature < 30:
#  print("It is cold outside")
# else:
#  print("It is not hot outside")
# print("Done")

# if 3 < 4:
#     print("A")
# else:
#     print("B")
#     print("C")


# Which statement will check if a is less than or equal to b?
# a. if a < or = b:
# b. if a <= b:
# c. if a < = b:
# d. if a >= b:
# e. if a =< b:
# f. if a < b or == b:
# g. if a <== b:


# Which statement will check if a is less b and less than c?
# a. if a < b and < c:
# b. if a < b & c:
# c. if a < b and a < c:
# d. if a < b and c:
a = 1
b = 2
c = 3
if a < b & c:
    print('ok')
if a < b and a < c:
    print('ok')
if a < b and c:
    print('ok')
