# name1 = 'a'
# name2 = 'b'


# name = name1 + name2

# print(name)

# numbers = [1, 2, 3, 4]
# charcters = ['a', 'b']

# result = numbers + charcters
# print(result)

# name = '*'

# print(name * 10)
# print('*' * 10)

# numbers = [1, 2, 3, 4]
# print(numbers * 5)

# name = 'dorna' * 'asd' -> error
# name = 'dorna ' * 3
# print(name)

# chars = ['d', 'o', 'r', 'n', 'a'] * 3
# print(chars)


# numbers = [1, 2, 3, 4, 5]
# names = ["vihan", "nikan"]

# my_list = [numbers, names]

# print(my_list)
# print(my_list[0])
# print(my_list[1])
# print(my_list[1][0])
# print(my_list[1][1])


# shopping_list = []
# print(shopping_list)
# shopping_list.append("egg")
# shopping_list.append("apple")
# print(shopping_list)

# del shopping_list[0]
# print(shopping_list)

# shopping_list.append("tomato")
# shopping_list.append("potato")
# print(shopping_list)
# shopping_list.remove("potato")


# print(shopping_list)


numbers = [1, 2, 3, 4, 5, 6]

# del numbers[2]
# numbers.remove(4)
# print(numbers)


names = ["nikan", "vihan", "rozhman", "pezhman", "tina", "sima", "dorna"]

# names.remove("rozhman")
# names.remove("sima")

# del names[0]
# print(names)

# all_data = numbers + names
# print(all_data)
# print(len(all_data))
# del all_data[8]
# print(all_data)
# all_data.remove("tina")
# print(all_data)


# tuple data type
numbers1 = [1, 2, 3, 4, 5, 6, 7]  # mutable قابل تغییر
print(type(numbers))
numbers1[0] = 100
numbers1.append(234)
numbers1.remove(4)


numbers2 = (1, 2, 3, 4, 5, 6, 7)  # immutable غیر قابل تغییر
print(type(numbers2))
# numbers2[0] = 200  # error  تاپل غیر قابل تغییر است
# numbers2.append(234) # error
# numbers2.remove(6)

print(numbers2[4])
print(numbers2[1:4])
