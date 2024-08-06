import datetime as dt

dt_now = dt.datetime.now()
# print(dt_now)
# print(dt_now.date())
# print(dt_now.time())
# print(dt_now.hour)
# print(dt_now.minute)
# print(dt_now.second)

# my_dt = dt.datetime(2020, 3, 21, 11)
# print(my_dt)

# strftime
# print(dt_now.strftime("%a,%b,%Y %H:%M:%S"))



# %a	Weekday, short version	Wed	

# %A	Weekday, full version	Wednesday	

# %w	Weekday as a number 0-6, 0 is Sunday	3	

# %d	Day of month 01-31	31	

# %b	Month name, short version	Dec	

# %B	Month name, full version	December	

# %m	Month as a number 01-12	12	

# %y	Year, short version, without century	18	

# %Y	Year, full version	2018	

# %H	Hour 00-23	17	

# %I	Hour 00-12	05	

# %p	AM/PM	PM	

# %M	Minute 00-59	41	

# %S	Second 00-59	08	

# %f	Microsecond 000000-999999	548513	

# %z	UTC offset	+0100	
# %Z	Timezone	CST	
# %j	Day number of year 001-366	365	

# %U	Week number of year, Sunday as the first day of week, 00-53	52	

# %W	Week number of year, Monday as the first day of week, 00-53	52	

# %c	Local version of date and time	Mon Dec 31 17:41:00 2018	

# %C	Century	20	

# %x	Local version of date	12/31/18	

# %X	Local version of time	17:41:00
# 	
# # %%	A % character	%	

# %G	ISO 8601 year	2018	

# %u	ISO 8601 weekday (1-7)	1	

# %V	ISO 8601 weeknumber (01-53)	01




import time
import pygame


# file = (r"C:\Users\Hp\Downloads\X2Convert.cc - PRAISE & MY WORSHIP AFRO-INFUSED VERSION BY TC MUSIC (128 kbps).mp3")
# pygame.init()
# pygame.mixer.music.load(file)
# pygame.mixer.music.play()
# time.sleep(10)
# pygame.mixer.music.stop()
# pygame.quit()


# while True:
#     tm = dt.datetime.now()
#     if tm.strftime("%I") == "08" and tm.strftime("%M") == "44" and tm.strftime("%S") == "00" and tm.strftime("%p") == "AM":
#         print("Its time to play.")

#         pygame.init()
#         pygame.mixer.music.load(file)

#         pygame.mixer.music.play()

#         time.sleep(10)

#         # Stop the music
#         pygame.mixer.music.stop()

#         # Quit pygame
#         pygame.quit()
       
