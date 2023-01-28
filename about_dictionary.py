# product_1 = {
#     'id': 1,
#     'name': 'spaghetti',
#     'price': 10,
#     'weight': 300
# }
# product_2 = {
#     'id': 2,
#     'name': 'mashrrom',
#     'price': 8,
#     'weight': 500
# }
# shopping_list = [product_1, product_2]
# print(shopping_list)
# product_3 = {}
# product_3['id'] = 3
# product_3['name'] = 'tomato'
# product_3['price'] = 20
# product_3['weight'] = 1000
# shopping_list.append(product_3)
# print(shopping_list)
# print(len(shopping_list))

# price = shopping_list[0]['price'] + \
#     shopping_list[1]['price'] + shopping_list[2]['price']

# print("amount of money to pay:", price, '$')

'''
Exercise 1: 
make a list of students.
each student is a dictionary which has id, name, age, family, grade, amount_paid, father_name
add 3 students to list
remove one of them 
show all students list
calculate schools gain_money.
'''

# removing item from dictionary


product_2 = {
    'id': 2,
    'name': 'mashrrom',
    'price': 8,
    'weight': 500
}

del product_2['weight']

# print(product_2)

# update dictionary value
# product_2['price'] = 10
# print(product_2)
# print(product_2['price'])
# print(list(product_2.keys())[0])
print(product_2.values())
print(list(product_2.values()))
print(list(product_2.values())[0])
