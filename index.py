# print("Hello world")

"""
afslasfalsfjal kasndlkandla
mansdnlasdnl asndnlaksdn
mdsdnnsdldnslad kasndalsdn
msandasnd kasdnasdlnasldsd

"""

# Python variables

# print('You are welcome Abdulahi')

# container = 'water'
# container = 'Oil'
# print(container)

# name = 'Abdulahi'

# print('You are welcome', name)

# Rules guiding variable declaration
# , variable name should start with a letter or underscore
# , variable name should not start with a number
# , variable name should not contain special characters except underscore
# , variable name should not be a reserved keyword in Python
# , variable name should be descriptive and concise
# , variable name should not contain space character hence use the following casing method

# pascal casing
FirstName = 'Dami'
# Camel casing
firstNameOfTheStudent = 'Dami'
# snake casing
first_name_of_the_student = 'Dami'

# concatenation
first_name = 'Dami'
last_name = 'Ade'
age = 30

# print(text,first_name)
# print('My name is ' +first_name + ' ' +last_name + '. I am '+ str(age) + 'years old')

# Types of variables
# 1. single variable multiple values
# var = 'Temi', 'Yemi', 34
# 2. multiple variables single value
# var1 = var2 = var3 = 'Temi'
# 3. multiple variables multiple values
# var1, var2, var3 = 'Temi', 'Yemi', 34

# print(var1)



# python datatypes
# 1. Text type /strings; str(), "Bola", '34'
var = '23'
# print(type(var))
# 2. Numeric type /integers; 
    # i. int(), 34, 45
var = 87

    # ii. float(), 34.5, 67.345
var = 87.6
    # iii. complex(), 2 + 1j
var = 2 + 1j

# 3. sequence type
    # i. list(), ['Temi', 34, 'ade']
# var = ['Temi', 34, 'ade']
    # ii. tuple(), ('Temi', 34, 'ade')
# var = ('Temi', 34, 'ade')
    # iii. range()
# var = list(range(20))

# 4. Boolean type; bool(), True, False
# var = True

# 5. mapping type
# i. dict(key=value), {'name': 'Temi', 'age': 34}
# var = {'name': 'Temi', 'age': 34}

# 6. set type
# i. set(), {'Temi', 34, 'ade'}
var = {'Temi', 34, 'ade'}

# 7. binary type
# i. bytes(), b'Temi'
var = b'temi'
# ii. bytearray(), bytearray(b'Temi')
# var = bytearray(b'Temi')
# iii. memoryview(), memoryview(b'Temi')
# var = memoryview(b'Temi')

# print(type(var))


first_name = 'BUSOLA'
last_name = "OJO"
age = 35
# print(f"My name is {first_name} {last_name}. I am {age}years old")

# Datatypes conversion
# 1. int() - convert to integer
var = int('34')
var = int(34.89)


# 2. float() - convert to float
# var = float('34.5')
var = float(33)

# 3. str() - convert to string
var = str(34)
var = str(34.5)
var = str([23, 45, 'temi'])

# 4. list() - convert to list
var = list(('temie'))
var = list(('temie',))
var = list({'temie': 34, 'ade': 45})
var = list({'temie', 'ade', 34, 45})
var = list(range(20))

# print(var)
# print(type(var))


# python operator
# 1. Arithmetic operators; +, -, /, //, *, **, %
# print(5%2)
# 2. assignment operator; =, +=, -=, *=, /=, **=, //=, %=
var = 5
var += 1 # var = var + 1
# print(var)
# 3. comparison operator; ==, !=, >, <, >=, <=
var = 5
# print(var >= 5)
# 4. logical operator; and, or, not
rice = False
beans = True

# 5. identity operator; is, is not
var1 = 5
var2 = 5
# print(var1 is not var2)

# 6. membership operator; in, not in
numbers = [23, 5, 6, 4,]
# print(5 in numbers)
# print(5 not in numbers)

# 7. bitwise operator; &, |, ^, ~
val1 = bin(23)
# print(val1)
val2 = bin(24)
# print(val2)
# print(bin(~24))

# print(bin(23 ^ 24)) # XOR- exclusive or



# conditional statement
# if beans and rice:
#     print('I will buy beans and rice')
# elif beans:
#     user = input('Do you have bread: ')
#     if user.lower() == 'yes':
#         print('I will buy beans and bread')
#     else:
#         print('I am not interested anymore')
# elif rice:
#     print('I will buy rice')
# else:
#     print('I will not buy')


# python strings
var = 'Hello world and everyone!' #['H', 'e', 'l', 'l', 'o']

# print(len(var))
# print(ord('h'))
# print(chr(37))
# print(var[-1])
# print(var[0:3])

# strings method
# print(var.upper())
# print(var.lower())
# print(var.swapcase())
# print(var.title())
# print(var.capitalize())

# print(len(var.strip()))
# var = var.rstrip('.')
# print(var)

# var = var.replace('world', 'everyone!')
# print(var)


# splited = var.split()
# print(splited)

# var = ' + '.join(splited)
# print(var)

# print(var.startswith('hello'))
# print(var.endswith('everyone!'))

# print(var.find('and'))
# print(var.index('Hello'))
# print(var.isalnum())
# print(var.isdigit())

# escape characters
var = r'Hello\rworld'
# \t
# \n
# \r

var = 'he\'s'

# print(var)


# python collection
# 1. list
# 2. tuple
# 3. set
# 4. distionary

# list:
# i. changeable
# ii. indexed
# iii. can accept duplicate value
# iv. ordered

var = [12, 34.4, 'Yemi', 'Yemi', False, ['apple', 'mango']]
# print(var)
# print(var[-1][0][0])
# print(var[-3:-1])

# var[2] = 'Olayemi'


# list methods/function

# var.append('Nigeria')
# var.extend(['Nigeria', 'Ghana'])
# var.reverse()
# var.insert(0, 'Nigeria')
# print(var.count('Yemi'))
# print(var.index(False))
# var.pop(2)
# var.remove('Yemi')
# print(var)

# for loop

# names = ['ade', 'ola', 'mide', 'sola']

# for name in names:
#     print('welcome',name)
#     print('_'*18)

# for char in 'SQI':
#     print(char)

# for number in range(20):
#     print(number)

# for x in range(1, 7):
#     print(f'{x} Times Table')
#     for y in range(1, 7):
#         print(f'{x} X {y} = {x*y}')


# namesOfStudent = []
# user = int(input('No of student: '))
# for student in range(user):
#     name = input(f'Enter student name {student+1}: ')
#     namesOfStudent.append(name)

# for each in namesOfStudent:
#     print(f'Welcome, {each}!')

score = 0

# print('1. Is Nigeria a country a.) Yes b.) No')
# user = input('answer: ')
# if user.lower() == 'a' or user.lower() == 'yes':
#     print('Correct! Nigeria is a country')
#     score += 1
# else:
#     print('Incorrect! Nigeria is a country')

# print(f'Your score is {score}')

score = 0
questions = [
    '1. Is Nigeria a country a.) Yes b.) No',
    '2. Is Python a programming language a.) Yes b.) No',
    '3. Is Lagos a state in Nigeria a.) No b.) Yes',
]

answers = ['a', 'a', 'b']

# for quest, ans in zip(questions, answers):
#     print(quest)
#     # print(ans)
#     user = input('Ans: ')
#     if user.lower() == ans:
#         print('Correct!')
#         score += 1
#     else:
#         print('Incorrect!')

# print(f'you got {score}/{len(questions)}')


# Assignment
'''
Section A
1. Get the number of student taking the test
2. Register each student
3. call out the student one after the other to take the test
4. get the student with the heighest score
5. get the student with the lowest score
6. get the average score of all the student

Section B
Develop a ussd application

'''


# scores = [ 23, 45, 64]
# print(min(scores))

# student_nos = int(input('How many student are you registering: '))
# students = []
# for i in range(student_nos):
#     name = input(f'Register student {i+1} name: ')
#     students.append(name)

# all_scores = []
# questions = [
#     '1. Is Nigeria a country a.) Yes b.) No',
#     '2. Is Python a programming language a.) Yes b.) No',
#     '3. Is Lagos a state in Nigeria a.) No b.) Yes',
# ]

# answers = ['a', 'a', 'b']

# for student in students:
#     print(f'Welcome {student} to the test')
#     score = 0
#     for question, answer in zip(questions,answers):
#         print(question)
#         user = input('Answer: ').lower()
#         if user == answer:
#             print('Correct!')
#             score += 1
#         else:
#             print('Incorrect!')

#     all_scores.append(score)

# print(students)
# print(all_scores)


# 2. tuple: it is indexed, ordered, accept dupliccate but unchangeable
var = ('ayo@', 'ope@', 'fola@', 'fola@')
# print(len(var))
# print(var[0])
# var[0] = 'dare@' #TypeError: 'tuple' object does not support item assignment

# list_var = list(var)
# print(list_var)
# list_var[0] = 'dare@'
# var = tuple(list_var)

# unpacking
# a, b, c, d = var
# print(b)
# *all, = var
# a, b ,*all = var

# print(all)

# tuple functions
# print(var.count('fola@'))
# print(var.index('ope@'))

# list of tuples
# list_of_tuples = [
#     ('ayo', 20, True), 
#     ('ope', 30, False), 
#     ('fola',25, False)
#     ]

# for name, age, married in list_of_tuples:
#     if married:
#         print(f'{name} is {age} years old and married')
#     else:
#         print(f'{name} is {age} years old and not married')
    
# 3. set: it is unindexed, unchangeable, it does not accept duplicate value, not ordered

# set_var = {'ayo', 'ope', 'fola', 'fola'}
# print(set_var[2]) #TypeError: 'set' object is not subscriptable
# set_var[0] = 'dare' #TypeError: 'set' object does not support item assignment
# print(len(set_var))

# set functions
# set_var.add('Abbey')
# set_var.remove('opes')
# set_var.clear()
# set_var.discard('dare')
# set_var.update(('yemi', 'femi'))
# pop_item = set_var.pop()
# print(pop_item)
# print(set_var)

# setA = {1, 2, 4, 5, 6, 7, 9}
# setB = {2, 4, 3 , 10, 8}
# setC = {1, 4, 5}

# # print(setA.union(setB))
# # print(setA.intersection(setB))
# # print(setB.difference(setA))
# # print(setA.symmetric_difference(setB))

# # setA.difference_update(setB)
# # setA.symmetric_difference_update(setB)
# # setA.intersection_update(setB)
# # print(setA)

# # print(setC.isdisjoint(setA))

# # WHILE LOOP

# # i = 0
# # while i < 10:
# #     print(i)
# #     i += 1

# # i = 10
# # while i > 0:
# #     print(i)
# #     i-=1

# # ussd = input('ussd code: ')

# # while ussd != '*312#':
# #     print('Invalid code. Try again!')
# #     ussd = input('ussd code: ')
# # else:
# #     print('welcome to our ussd app')


# # expectedAge = 18
# # userAge = int(input('Your Age: '))
# # while userAge < expectedAge:
# #     print('You are not eligible to vote. Try again!')
# #     userAge = int(input('Your Age: '))
# # else:
# #     print('You are eligible to vote!')

# # while True:
# #     userChoice = input('Do you want to continue? (yes/no): ')
# #     if userChoice.lower() == 'yes':
# #         print('Welcome back!')
# #     elif userChoice.lower() == 'no':
# #         print('Goodbye!')
# #         break
# #     else:
# #         print('Invalid choice. Try again!')


# # ticket = 10
# # while ticket > 0:
# #     user = int(input('Age: '))
# #     if user < 18:
# #         print('You are not eligible to buy a ticket.')
# #     else:
# #         print('Ticket sold!')
# #         ticket -= 1

# #     print(f'Tickets remaining: {ticket}')
# # else:
# #     print('No more tickets available!')

# items = {'Apple', 'Orange', 'Mango', 'Cashew'}
# print(items)
# my_guess = items.pop()
# print(my_guess)


# balance = 500
# while True:
    
#     stake = float(input('Stake Amount: '))

#     if balance >= stake:

#         print(f'''
#             Welcome to my guess app, your balance is #{balance}
#             1. Apple
#             2. Orange
#             3. Mango
#             4. Cashew
#         ''')

        
#         # print(items)
#         user = input('Guess the fruit: ').capitalize()
        
#         # print(my_guess)

#         if user == my_guess:
#             print('You guess right')
#             balance += stake*2
#             print(f'Your balance is #{balance}')
#         else:
#             print('You are wrong')
#             balance -= stake
#             print(f'Your balance is #{balance}')

#         items.add(my_guess)
#         print(items)

#     else:
#         print('Insufficient balance')
#         break

# 4. Dictionary: its ordered, changeable, its key doesn;t allow duplicate
# dict('key'='value')
myDict = {
    'name':'Damilare', 
    'course':'Data science', 
    'age':23,
    'married': False,
    'avaliable_docs':{
        'SOP':True,
        'CV':True,
        'Resume':False
    }
    }
# print(myDict['avaliable_docs']['SOP'])

# myDict['name'] = 'Arise Damilare'
# print(myDict.keys())
# print(myDict.values())
# print(myDict.items())

# for key, value in myDict.items():
#     print(key, value)

# questions = {
#     'a':'1. Is lagos a state in Nigeria a) yes b) no', 
#     'b':'2.) Oyo state is not an eastern part of Nigeria a.) no b.) yes'
#     }

# for ans, ques in questions.items():
#     print(ques)
#     user = input('Answer: ').lower()
#     if user == ans:
#         print('Correct')
#     else: 
#         print('Incorrect')

# print(myDict.get('Age','Not found'))
# myDict.update({'Nationality':'Nigeria'})
# myDict['Nationality'] = 'Nigeria'
# myDict.pop('age')
# myDict.popitem()
# myDict.clear()

# print(myDict)
# {
#     student1:{
#         name: 'dami'
#         course: 'maths'
#     }
# }

# student_details = {}
# x = 1
# while True:
#     user = input('press enter to continue and 1 to exit this page: ')
#     if user == '1':
#         print('Goodbye!')
#         break
    
#     student_info = {}
#     name = input('Enter student name: ')
#     course = input('Enter course: ')
#     student_info.update({'name':name, 'course':course})
#     student_details[f'student{x}'] = student_info
#     x += 1

#     print(student_details)


# print(student_details)


# Python Functions

# unparametized
def greet():
    print('Hello, world!')

# greet()


# Parametized
def greet(name):
    print(f'Hello everyone! from {name}')


# my_name = input('Your name: ')
# greet(my_name)

# Return function 

# def greet():
#     return 'Hello Everyone!'

# greetings = greet()
# print(greetings)


# function suppliment

def addition(value1:float, value2:float = 10) -> float:
    '''
    This function add up two value\n
    value1\n
    value 2
    '''
    return value1 + value2

# print(addition(20))


# global and local variables

val1 = 20  #Global variable
val2 = 10


def addition():
    global val3

    val3 = 30 #local variable
    return val1 + val2 + val3

def subtraction():
    addition()
    return val1 - val2 - val3

def main():
    user = input('''
    Choose your option
    1. addition
    2. subtraction
    #. exit
    ''')

    if user == '1':
        print(addition())
    elif user == '2':
        print(subtraction())
    elif user == '#':
        print('Goodbye!')
    else:
        print('Invalid option Try again')
        main() #Reccursive function



# main()



def landingPage():
    print('Welcome to our landing page')
    user = input('Enter Ussd code: ').strip()
    if user == '*312#':
        main()
    else:
        print('Invalid USSD code. Please try again')
        landingPage()

def main():
    print('''
    1. Data plan
    2. Check Balance
    ''')
    user = input('Choose your option: ')


# landingPage()

# OOP- Object Oriented programming

class School:
    def __init__(self, branch, location = None):
        self.name = 'Adex Group of schools'
        self.founded = 2001
        self.branch = branch
        self.location = location
        self.student_data = {}

    
    def home_page(self):
        print(f'Welcome to {self.name} {self.branch} branch.')
        print('''
            1. Student Registeration
            2. Take Test
            #. Exit
        
        ''')
        user = input('Option: ')

        if user == '1':
            self.registration()
        elif user == '2':
            self.take_test()
        elif user == '#':
            print('GoodBye!')

    def registration(self):
        print(f'Student registeration portal for {self.branch} Branch.')
        x = 1
        while True:
            user = input('press enter to continue and 1 to exit this page: ')
            if user == '1':
                print('Goodbye!')
                break
            
            student_info = {}
            name = input('Enter student name: ')
            course = input('Enter course: ')
            student_info.update({'name':name, 'course':course})
            self.student_data[f'student{x}'] = student_info
            x += 1

    def take_test(self):
        pass

    

branch1 = School('Lagos')
# print(branch1.branch)

branch2 = School('Ibadan')
# print(branch2.branch)
# print(type(first_school))

# branch1.registration()
# branch2.intro()


# Inheritance

class Father:
    def __init__(self) -> None:
        self.last_name = "Badmus"
        self.first_name = "Oluwaseun"
        self.hobby = 'Singing'

    def intro(self):
        print(f'My name is {self.first_name} {self.last_name} and my hobby is {self.hobby}')

    def doings(self, adjective):
        print(f'{self.first_name} is {self.hobby} {adjective}')


father = Father()

# father.intro()
# father.doings('Very well')

class Child(Father):
    def __init__(self) -> None:
        super().__init__()
        # or
        # Father.__init__(self)
        self.first_name = 'Ayomide'
        self.hobby = 'Dancing'

    def goals(self):
        print(f'{self.first_name} wants to be a {self.hobby} star')

child1 = Child()
# child1.intro()

# child1.goals()


class Grandchild(Child):
    def __init__(self) -> None:
        super().__init__()
        self.first_name = 'Kemi'
        self.hobby = 'Acting'

grand1 = Grandchild()

if __name__ == "__main__":
    grand1.intro()

# print(__name__)


# Modularization

# modules
# script
# library