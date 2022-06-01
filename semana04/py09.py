"""
Atividade Semana 04 - Sistemas Embarcados
Lucas Russignoli 11721EAU004
"""
import random
import math
import datetime
import calendar
import os

courses = ['History', 'Math', 'Physics', 'CompSci']

random_course = random.choice(courses)
rads = math.radians(90)
today = datetime.date.today()

print(random_course)
print(math.sin(rads))
print(today)
print(calendar.isleap(2017))
print(os.getcwd())
print(os.__file__)

