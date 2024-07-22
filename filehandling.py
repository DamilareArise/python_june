# filehandling

# r => read only
# w => write only
# a => append only
# x => create

path = r"C:\All_Python\python_june\newSchool.py"
# file = open(path)
# print(file.read())
# file.close()

# with open(path) as file:
#     print(file.read())


# with open('file.txt', 'w') as file:
#     file.write('Hello World!')

# with open('file.txt', 'a') as file:
#     file.write('\nmy name is Arise Damilare')

with open('file.pdf', 'x'):
    print('File created successfully')