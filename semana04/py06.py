"""
Atividade Semana 04 - Sistemas Embarcados
Lucas Russignoli 11721EAU004
"""
language = 'Python'

if language == 'Python':
	print('Language is Python')

elif language == 'Java':
	print('Language is Java')

else:
	print('No match')

user = 'Admin'
logged_in = True

if user== 'Admin' and logged_in:
	print('Admin Page')
else:
	print('Bad Creds')

a = [1, 2, 3]
b = [1, 2, 3]

print(id(a))
print(id(b))
print(a is b)
