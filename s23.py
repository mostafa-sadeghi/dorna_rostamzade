# plain_text = 'This is a test. ABC abc'
# for char in plain_text:
#     print(ord(char), end=" ")
# print()
# for char in plain_text:
#     print(char, end=" ")
# print()
# for char in plain_text:
#     x = ord(char)
#     x = x + 1
#     char2 = chr(x)
#     print(char2, end=" ")

# plain_text = "dorna"
# password = ''
# for char in plain_text:
#     x = ord(char)
#     x = x + 1
#     char2 = chr(x)
#     password = password + char2
# print(password)

# password = 'epsob'
# original_text = ''
# for s in password:
#     x = ord(s)
#     x = x - 1
#     char2 = chr(x)
#     original_text += char2

# print("original text:",original_text)

x = {}

x["sandal"] = 15
x["python ebook"] = 10
x["bread"] = 50

# print(x)
print("welcome to our shop")
print('-'*40)
print(f'{"Product Name":16}{"InventoryCount":>18}')
print('-'*40)

for key, value in x.items():
    print(f'{key:16}{value:>18}')
print('-'*40)

print("select a product: ")
product = input('> ')
