numbers = []

for i in range(5):  # [0,1,2,3,4]
    n = float(input('enter a number: '))
    numbers.append(n)


print(numbers)
print(sum(numbers))
total = 0

for n in numbers:
    total += n   # total = total + n

print(total)

# exercise 1 : write a program that gets 5 names from input and put them in a list called names
# remove second name from this list
# append a new name to the list
# print the list
##########################################################################################
# exercise 2:
# write a program that gets 6 numbers from input and print sum of them and then subtract the result
# by 10
# print the above result
# slice 3 first number from the list
