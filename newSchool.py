from index import School
import random as rnd
import time
import datetime as dt
import numpy as np
from colorama import just_fix_windows_console, Fore, Back, Style
import pwinput


# newSchool = School('Oshogbo')
# newSchool.home_page()

class NewSchool(School):
   def __init__(self, branch, location=None):
      super().__init__(branch, location)
      self.name = 'Yello Schools'


# newschool = NewSchool('Oyo')
# newschool.home_page()

# var = rnd.randint(1000000000, 1099999999)
# print(var)
# x=['Apple', 'Banana', 'Tangerine']
# rnd.shuffle(x)
# print(x)

# x = rnd.random()
# print(x)


# print('Loading...')
# time.sleep(2)
# print('Welcome')

# now = dt.datetime.now()
# print(now.date())


# just_fix_windows_console()
# print(Fore.MAGENTA+'Hello everyone!')
# print(Style.RESET_ALL)


# password = pwinput.pwinput(mask='+')
# print(f'Password: {password}')

