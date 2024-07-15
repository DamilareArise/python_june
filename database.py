import mysql.connector as sql

mycon = sql.connect(
    host="127.0.0.1",
    user="root",
    password="",
    database="mySchool_db"
)

mycursor = mycon.cursor()
mycon.autocommit = True

# mycursor.execute('CREATE DATABASE mySchool_db')
# mycursor.execute('DROP DATABASE mySchool_db')

# mycursor.execute('SHOW DATABASES')
# for db in mycursor:
#     print(db)

# mycursor.execute('CREATE TABLE user_table(id INT(4) PRIMARY KEY AUTO_INCREMENT, fullname VARCHAR(50), email VARCHAR(50) UNIQUE, phone_no VARCHAR(11) UNIQUE, CGPA FLOAT(2), course VARCHAR(20), isAdmin BOOLEAN, isStudent BOOLEAN, date_created DATETIME DEFAULT CURRENT_TIMESTAMP)')

# mycursor.execute('DROP TABLE user_table')

# mycursor.execute('SHOW TABLES')
# for table in mycursor:
#     print(table)


# mycursor.execute('ALTER TABLE user_table CHANGE CGPA cgpa FLOAT(2) DEFAULT 5.0')
# mycursor.execute('ALTER TABLE user_table CHANGE isGraduate isGraduate BOOLEAN DEFAULT FALSE')
# mycursor.execute('ALTER TABLE user_table CHANGE course department VARCHAR (30)')
# mycursor.execute('ALTER TABLE user_table ADD password VARCHAR(20)')



# query = 'INSERT INTO user_table(fullname, email, phone_no, cgpa, course, isGraduate)VALUE(%s, %s, %s, %s, %s, %s)'
# values = ('John Doe', 'johndoe@gmail.com', '08012345678',5.0, 'Datascience', False)

# mycursor.execute(query,values)
# mycon.commit()

def home():
    user = input("""
        Welcome to the School Management System
    1. Login
    2. Register
    #. Exit      
          
    Option:- """)
    if user == '1':
        login()
    else:
        register()

def register():
    print('''
        Register as;
        1. Student
        2. Admin
        #. Exit
    ''')
    choice = input('Your Option: ')
    if choice == '1':
        studentReg()
    elif choice == '2':
        adminReg()
    elif choice == '#':
        exit()
    else:
        print('Invalid Choice')
        register()

def studentReg():
    print('Student Registration')
    fullname = input('Fullname: ')
    email = input('Email: ')
    phone_no = input('Phone Number: ')
    department = input('Course: ')
    password = inputPassword()

    query = 'INSERT INTO user_table(fullname, email, phone_no, department, isStudent, password) VALUE(%s, %s, %s, %s, %s, %s)'
    values = (fullname, email, phone_no, department, True, password)
    mycursor.execute(query, values)
    print('Registeration Successfull, kindly proceed to login..')
    login()


    
def adminReg():
    print('Admin Registration')

    fullname = input('Fullname: ')
    email = input('Email: ')
    phone_no = input('Phone Number: ')
    department = input('Course: ')
    password = inputPassword()

    query = 'INSERT INTO user_table(fullname, email, phone_no, department, isAdmin, password) VALUE(%s, %s, %s, %s, %s, %s)'
    values = (fullname, email, phone_no, department, True, password)
    mycursor.execute(query, values)
    print('Registeration Successfull, kindly proceed to login..')
    login()



def inputPassword():
    password = input('Password: ')
    confirm_password = input('Confirm Password: ')
    if password == confirm_password:
        return password
    else:
        print('Password does not match')
        inputPassword()

def login():
    print('Login')
    email = input('Email: ').strip()
    password = input('Password: ').strip()
    query = 'SELECT * FROM user_table WHERE email = %s AND password = %s'
    values = (email, password)
    mycursor.execute(query, values)
    details = mycursor.fetchone()
    # print(details)
    if details:
        print('Login Successfully')
        if details[6]:
            adminLogin(details)
        else:
            studentLogin(details)

    else:
        print('Incorrect email or password')
        login()

def adminLogin(details):
    print(f'''
        Welcome {details[1]}

    1. Set Test Questions
    2. View Test Questions
    #. Exit
    ''')

def studentLogin(details):
    print(f'''
        Welcome {details[1]}
          
    1. Take Test
    2. View Result
    #. Exit
    ''')



home()


# SELECT QUERY
# mycursor.execute('SELECT * FROM user_table')
# mycursor.execute('SELECT * FROM user_table WHERE id = 2')
# details = mycursor.fetchone()
# print(details)