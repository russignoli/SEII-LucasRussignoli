"""
Atividade Semana 04 - Sistemas Embarcados
Lucas Russignoli 11721EAU004
"""
import csv

with open('names.csv', 'r') as csv_file:
	csv_reader = csv.reader(csv_file)

	with open('new_names.csv', 'w') as new_file:
		fieldnames = ['first_name', 'last_name', ' email']

		csv_writer = csv.DicWriter(new_file, fieldnames=fieldnames, delimiter='\t')

		csv_writer.writeheader()

		for line in csv_reader:
			csv_write.writerow(line)