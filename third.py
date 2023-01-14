
# message = 'He said, "Aren\'t can\'t shouldn\'t wouldn\'t."'
# print(message)


# message = '''He said, "Aren't can't shouldn't wouldn't."'''
# print(message)

age = 13

# message = "tina is %s years old"%age
# print(message)

# name = "tina"
# age = 13

# message = "%s is %s years old"%(name,age)
# print(message)

# # using f string to form our strings
# name = "tina"
# age = 13

# message = f"{name} is {age} years old"
# print(message)


# + - * /

# s1 = 'a'
# s2 = 'b'

# s = s1 + s2
# print(s)

# y = s1 * 4
# print(y)

# name = "dorna"
# print(name[0])
# print(name[1])
# print(name[2])
# print(name[3])
# print(name[4])
# print(name[5]) -> error


# list data type
# shopping = []

# print(type(shopping))

# shopping = ['bread', 'egg', 'apple', 'banana']
# print(shopping[0])
# print(shopping[1])
# print(shopping[2])
# print(shopping[3])

# shopping.append("tomato")
# print(shopping)

# del shopping[1]
# print(shopping)

# shopping.remove('apple')
# print(shopping)

# exercise 1: یک لیست از اعداد 1 تا 5 بسازی و سومین عدد را نمایش بدی
# exercise 2: دومین عدد را از لیست بالا حذف کنی
# exercise 3: عدد بیست را به لیست اضافه کن


# numbers = [1, 2, 3]
# list is mutable
# numbers[2] = 5
# print(numbers)


# name = 'dorna'
# str is immutable
# name[0] = 'x' -> error نوع داده رشته غیر قابل تغییر می باشد.

# name = ['d', 'o', 'r']
# name[0] = 'x'
# print(name)

# name = ['dorna']
# name[0] = 'x'
# print(name)


# slicing on str:

name = "dorna"
print(name[0:3])  # "dor"

print(name[0:2])
print(name[:2])
print(name[2:4])

# slicing on list

numbers = [1, 1, 2, 3, 3, 4, 4]
my_slice = numbers[4:]
print(my_slice)
