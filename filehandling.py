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

# with open('file.pdf', 'x'):
#     print('File created successfully')

president_name = []
all_scores = []
# with open('president_height.csv', 'r') as file:
#     president_infos = file.readlines()
#     president_infos = president_infos[1:]

    
#     for each in president_infos:
#         info_list = each.split(',')
#         president_name.append(info_list[1])
#         score = int(info_list[2].strip('\n'))
#         all_scores.append(score)


# print(all_scores)
# print(president_name)


import csv


# with open('president_height.csv', 'r') as file:
#     reader = csv.DictReader(file)
#     for row in reader:
#         all_scores.append(int(row['height(cm)']))
#         president_name.append(row['name'])

# print(president_name)
# print(all_scores)


import os
# os.rename('usPresident.csv', 'president_height.csv')
# try:
#     os.mkdir('newFolder')
#     print('folder created')
# except FileExistsError:
#     print('Folder already exists')
#     # os.remove('file.pdf') #deletes a file
#     os.rmdir('newFolder') # deletes a folder
#     print('folder deleted')


# if os.path.exists('president_height.csv'):
#     print('path exists')

# for file in os.environ.keys():
#     print(file)


print(os.getcwd()) #current working directory
