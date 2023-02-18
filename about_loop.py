# for loop

# string = 'abcdefghi'
# print("each char below")
# print(string[0])
# print(string[1])
# print(string[2])
# print(string[3])
# print(string[4])
# print(string[5])
# print(string[6])
# print(string[7])
# print(string[8])
# for s in string:
#     print(s)
# print('each char after with space')
# print(string[0], string[1], string[2], string[3])
# for s in string:
#     print(s, end=' ')
# exercise : write a program that gets a name from input and prints each char's of the name with - separator
name = input('enter a name: ')
for n in name:
    print(n)
for n in name:
    print(n, end=" ")
for n in name:
    print(n, end="-")
######################################
print(len(name))

for i in range(len(name)):
    print(name[i], end="-")


#######################################
for i in range(len(name)):
    if i == len(name) - 1:
        print(name[i])
    else:
        print(name[i], end="-")
