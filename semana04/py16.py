"""
Atividade Semana 04 - Sistemas Embarcados
Lucas Russignoli 11721EAU004
"""

import csv

html_output = ''
names = []

with open('patrons.csv', 'r') as data_files:
	csv_data = csv.DictReader(data_file)


	next(csv_data)
	next(csv_data)

	for line in csv_data:
		if line[0] == 'No Rewards':
			break
		names.append(f"{line[0]} {line [1]}")

html_output += f'<p> There are currently {len(names)} public contributors. Thak You!</p>'

html_output += '\n</ul>'

print(html_output)

	print(line)

for name in names:
	print(name)
