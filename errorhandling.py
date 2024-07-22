# two types of error in python
# 1. runtime error
# mylist = ['Apple', 'Mango', 'Cashew']
# print(mylist.pop(9))

# 2. compile type error
# print(x)

# error handling
# 1. try
# 2. except
# 3. else
# 4. finally

def home():
    print('Welcome to home')

def dashboard():
    print('Welcome to home')

# x:str = 'tyu'

# try:
#     user = int(input('A number: '))
#     print(x)

# except ValueError:
#     print('Please enter a number')

# except NameError:
#     print('Variable has not declared')

# except Exception as e:
#     print(f"There's an error -> {e}")

# else:
#     print('No error')

# finally:
#     print('Thank you for using our app')



# def divide():
#     try:
#         val1 = int(input('Value 1: '))
#         val2 = int(input('Value 2: '))
#         result = val1 / val2
#     except ValueError:
#         print('Please enter a number')
#         divide()
#     except ZeroDivisionError:
#         print('Please enter a number other than 0')
#         divide()
#     except Exception as e:
#         print(f'Something went wrong -> {e}')
#     else:
#         print(result)

# divide()
