"""
Atividade Semana 04 - Sistemas Embarcados
Lucas Russignoli 11721EAU004
"""
student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}

student['phone'] = '555-555'
student['name'] = 'Jane'
student.update({'name': 'Jane', 'age': 26, 'phone': '555-5555'})
print(student)
print(student['courses'])
print(student.get('phone', 'Not Found'))

age = student.pop('age') 
print(student)
print(age)
print(len(student))
print(student.keys())
print(student.values())
print(student.items())

for key, value in student.items:
   print(key, value)


