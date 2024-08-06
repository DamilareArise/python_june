
arr = ['tomayo', 'pepper', 'fish']

# file = open('file2.txt', 'w')
# file.write(arr)

import json

# new = json.dumps(arr)
# file = open('file2.json', 'w')
# file.write(new)

def home():
    print('''
    Welcome to ***
    1. Sign Up
    2. Sign In
    3. Exit
    ''')
    user = input("option: ")

    if user == '1':
        signup()
    elif user == '2':
        signin()
    elif user == '3':
        print("Goodbye")

def signup():
    user  = {
        "fullname": input('Fullname: '),
        'email': input('Email: '),
        "password": input("Passsword: ")
    }

    file = open('file2.json')
    database_str = file.read()
    database_json = json.loads(database_str)
    
    database_json.append(user)

    database_str = json.dumps(database_json)

    file = open('file2.json', 'w')
    file.write(database_str)
    
    print('Registration Succesful')

    signin()


def signin():
    email = input('Email: ')
    password = input('Password: ')

    
    file = open('file2.json')
    database_str = file.read()
    database_json = json.loads(database_str)
    for user in database_json:
        if user['email'] == email:
            if user['password'] == password:
                print('Login successfully')
            else: 
                print('Incorrect password')
    
    print('Wrong login details')


home()