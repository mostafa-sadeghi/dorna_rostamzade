# people = ['sara', 'armin', 'tina', 'rozha', 'dorna', 'artin']
# for person in people:
#     print(person, end=' ')

# for i in range(len(people)):
#     print(str(i)+'.'+people[i], end=' ')


# for index, person in enumerate(people):
#     print(str(index) + '.' + person, end=' ')


# people = ['sara', 'armin', 'tina', 'rozha', 'dorna', 'artin']

# i = 0
# while i < len(people):
#     print(str(i)+'.' + people[i], end=' ')
#     i += 1


# quit = 'n'
# while quit == 'n':
#     quit = input('Do you want to quit? ')

# done = False
# while not done:
#     quit = input("Do you want to Quit? ")
#     if quit == 'y':
#         done = True


# for i in range(10, 0, -1):
#     print(i, end=' ')
# print()
# i = 10
# while i > 0:
#     print(i, end=' ')
#     i -= 1


# import pygame

# # Initialize the game engine
# pygame.init()

# BLACK = (0, 0, 0)
# WHITE = (255, 255, 255)
# RED = (255, 0, 0)
# size = (700, 500)

# screen = pygame.display.set_mode(size)
# pygame.display.set_caption("Our first game")

# screen.fill(WHITE)
# pygame.draw.rect(screen, RED, [0, 0, 100, 100])
# font = pygame.font.SysFont('Arial', 25, True, False)
# text = font.render("My text", BLACK, BLACK)
# screen.blit(text, [250, 250])
# pygame.display.flip()


# done = False
# while not done:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             done = True
#         if event.type == pygame.KEYDOWN:
#             print("User pressed a key....")

# exercise 1:
'''
* * * * * * * * * *
'''
# exercise 2:
'''
* * * * * * * * * *
* * * * * 
* * * * * * * * * * * * * * * * * * * *
'''
# exercise 3:
'''
* * * * * * * * * *
* * * * * * * * * *
* * * * * * * * * *
* * * * * * * * * *
* * * * * * * * * *
* * * * * * * * * *
* * * * * * * * * *
* * * * * * * * * *
* * * * * * * * * *
* * * * * * * * * *

'''
# exercise 4:
'''
* * * * * 
* * * * * 
* * * * * 
* * * * * 
* * * * * 
* * * * * 
* * * * * 
* * * * * 
* * * * * 
* * * * * 

'''
# exercise 5:
'''
* * * * * * * * * * * * * * * * * * * *
* * * * * * * * * * * * * * * * * * * *
* * * * * * * * * * * * * * * * * * * *
* * * * * * * * * * * * * * * * * * * *
* * * * * * * * * * * * * * * * * * * *
'''

# exercise 6:
'''
0 1 2 3 4 5 6 7 8 9 
0 1 2 3 4 5 6 7 8 9 
0 1 2 3 4 5 6 7 8 9 
0 1 2 3 4 5 6 7 8 9 
0 1 2 3 4 5 6 7 8 9 
0 1 2 3 4 5 6 7 8 9 
0 1 2 3 4 5 6 7 8 9 
0 1 2 3 4 5 6 7 8 9 
0 1 2 3 4 5 6 7 8 9 

'''
# exercise 7:
'''
0 0 0 0 0 0 0 0 0 0
1 1 1 1 1 1 1 1 1 1
2 2 2 2 2 2 2 2 2 2
3 3 3 3 3 3 3 3 3 3

.
9 9 9 9 9 9 9 9 9 9
'''

# exercise 7:
'''
0
0 1
0 1 2 
0 1 2 3
0 1 2 3 4


0 1 2 3 4 5 6 7 8 9
'''
# exercise 8:
'''
0 1 2 3 4 5 6 7 8 9
  0 1 2 3 4 5 6 7 8
    0 1 2 3 4 5 6 7 
      0 1 2 3 4 5 6 
      

                  0
'''
# exercise 9:
'''
0 1 2 3 4 5 6 7 8 9
0 1 2 3 4 5 6 7 8
0 1 2 3 4 5 6 7
0 1 2 3 4 5 6
0 1 2 3 4 5
0 1 2 3 4
0 1 2 3
.

0

'''
# exercise 10:
'''
1   2   3   4   5   6   7   8   9
2   4   6   8  10  12  14  16  18 
3   6   9  12  15  18  21  24  27 
..


9  18  27                      81


'''

# exercise 11:
'''
                1
...
      1 2 3 4 5 6 5 4 3 2 1
    1 2 3 4 5 6 7 6 5 4 3 2 1
  1 2 3 4 5 6 7 8 7 6 5 4 3 2 1
1 2 3 4 5 6 7 8 9 8 7 6 5 4 3 2 1
'''


# print(type(5))
# print(type(5.3))
# print(type("hi"))
# print(type(True))
# print(type([1,2,3]))
# print(type((1,2,3)))


# my_list = [[2, 3],   [4, 3],   [6, 7]]
# for item in my_list:
#     print(item)
#     print(type(item))
#     print(len(item))
#     print(item[0],item[1])

# names = ["reza", "reza", "artin"]
# print(names.count("reza"))

# print([0]*100)

# my_list = [2,3,4,5,6,7]
# print(sum(my_list))
# total = 0
# for i in range(len(my_list)):
#     total += my_list[i]


# print(total)


plain_text = "This is a test. ABC abc"

for c in plain_text:
    x = ord(c) + 1
    print(chr(x), end=" ")
