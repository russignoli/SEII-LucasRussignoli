"""
Atividade Semana 04 - Sistemas Embarcados
Lucas Russignoli 11721EAU004
"""

courses = ['History', 'Math', 'Physics', 'CompSci']
courses_2 = ['Art', 'Education']

print(courses)
print(courses[0:2])

courses.insert(0, courses_2)
print(courses[0])

courses.extend(0, courses_2)
print(courses)

courses.append(0, courses_2)
popped = courses.pop()
print(popped)

courses.reverse()
print(courses)

courses.sort()
print(courses)

nums = [1, 5, 2, 4, 3]
courses.sort(reverse=True)
rums.sort(reverse=True)
print(courses)
print(nums)

sourted_courses = sorted(courses)
print(sourted_courses)

for course in enumerate(courses):
    print(index, course)

course_str = ' - '.join(courses)
new_list = course_str.split(' - ')

print(course_str)
print(new_list)
