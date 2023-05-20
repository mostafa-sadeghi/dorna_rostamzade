# number = input('enter a number: ')
# print(number[0])
# print(number[1])
# print(number[2])

# با روش بالا برنامه ای بنویس که یک عدد از ورودی بگیرد و تمامی ارقام آن را نمایش دهد
# 23478
# "1th digit is 2"
# "2th digit is 3"
# .....
# در نهایت مجموع رقم های آن عدد را محاسبه و پرینت کن
# همینطور مجموع رفم های فرد عدد را محاسبه و نمایش بده


# با روش ریاضی هم انجام

# number = int(input('enter a number: '))
# i = 1
# while number != 0:
#     print(i, number % 10)
#     number = number // 10
#     i = i + 1



import random

# def 

# print("hi",1,1+2,"hello")


# def add(n1,n2,n3):
#     print(n1+n2+n3)

# add(2,3,4)


# def my(name,n1,n2,n3):
#     if (0<= n1 <=100) and (0<= n2 <=100) and (0<= n3 <=100):
#         ave = (n1 + n2 + n3)/3
#         return f'{name}, your average is {ave:.2f}'

#     return 'scores are not correct'

# name = input('enter your name: ')
# number1 = int(input('Enter first number: '))
# number2 = int(input('Enter second number: '))
# number3 = int(input('Enter third number: '))
# result = my(name,number1,number2,number3)

# print(result)


def generate_secrent_number():
    numbers = list('0123456789')
    random.shuffle(numbers)  
    return''.join(numbers[:3])

def check_user_guess(user_guess, secret_number):
    if user_guess == secret_number:
        return 'You won!'
    help = []
    for i in range(len(user_guess)):
        if user_guess[i] == secret_number[i]:
            help.append("Fermi")
        elif user_guess[i] in secret_number:
            help.append("Pico")

    if len(help) == 0:
        return 'Bagels'
    return help

secret_number = generate_secrent_number()

user_guess = input('Enter your guess: ')
print(secret_number)
result = check_user_guess(user_guess, secret_number)
print(result)
