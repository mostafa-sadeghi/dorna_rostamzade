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

number = int(input('enter a number: '))
i = 1
while number != 0:
    print(i, number % 10)
    number = number // 10
    i = i + 1