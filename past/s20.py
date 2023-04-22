
# ex1
'''
*
* *
* * *
* * * *
* * *
* *
*
'''

# ex2 :
'''
write a students management system

menu:
0 -> exit
1 -> show all students
2 -> add new student
3 -> remove a student
4 -> update a student

'''

all_students = []
while True:

    print('''Welcome to our program.
    out student management system.
    to exit -> 0
    to show all students -> 1
    to add new student -> 2
    to remove a student -> 3
    to update a student -> 4
    ''')
    user_input = input('> ')
    if user_input == '0':
        exit()
    elif user_input == '1':
        print("all students are :", all_students)
    elif user_input == '2':
        student = {}
        studen_name = input('enter student`s name: ')
        studen_age = input('enter student`s age: ')
        studen_grade = input('enter student`s grade: ')
        student['name'] = studen_name
        student['age'] = studen_age
        student['grade'] = studen_grade
        all_students.append(student)
    elif user_input == '3':
        name_to_delete = input('enter a name to delele from our list:> ')
        for i in range(len(all_students)):

            if all_students[i]['name'] == name_to_delete:
                del all_students[i]
                break
    elif user_input == '4':
        name_to_edit = input('enter a name to edit from our list:> ')
        for i in range(len(all_students)):
            if all_students[i]['name'] == name_to_edit:
                print(
                    "which one to edit?\nEnter 'n' for change the name | 'a' for age | 'g' for grade: ")
                edit_entry = input('> ')
                if edit_entry == 'n':
                    all_students[i]['name'] = input('enter new name> ')
                elif edit_entry == 'a':
                    all_students[i]['age'] = input('enter new age:> ')
                elif edit_entry == 'g':
                    all_students[i]['grade'] = input('enter new grade:> ')
            break
