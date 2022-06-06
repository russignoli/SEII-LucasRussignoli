"""
Atividade Semana 04 - Sistemas Embarcados
Lucas Russignoli 11721EAU004
"""

import os

print(dir(os))
print(os.getcwd())
os.chdir('/Users/coreyschafer/Desktop/')
os.mkdir('OS-Demo-2/Sub-Dir-1')
os.makedirs('OS-Demo-2/Sub-Dir-1')
os.rmdir('OS-Demo-2/Sub-Dir-1')
os.removedirs('OS-Demo-2/Sub-Dir-1')
os.rename('demo.txt')

print(os.stat('demo.txt').st_size)
print(os.stat('demo.txt').st_mtime)
print(os.listdir())

from datetime import datetime
os.chdir('/Users/coreyschafer/Desktop/')
print(os.environ.get('HOME'))
file_path = os.environ.get('HOME') + 'test.txt'
print(file_path)

for dirpath , dirnames, filenames in os.walk('/Users/coreyschafer/Desktop/'):
	print('C urrent Path:', dirpath)
	print('Directories:', dirnames)
	print('Files:', filenames)
	print()

