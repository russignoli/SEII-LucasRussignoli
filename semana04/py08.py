"""
Atividade Semana 04 - Sistemas Embarcados
Lucas Russignoli 11721EAU004
"""

month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] 

def is_leap(year):

	return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def days_in_mounth(year, mounth):

	if not 1 <= mounth <= 12:
		return 'Invalid Month'

	if mounth == 2 and is_leap(year):
		return 29

	return mounth_days[mounth] 

print(is_leap(2020))
print(days_in_mounth(2017, 2))

