"""
Atividade Semana 04 - Sistemas Embarcados
Lucas Russignoli 11721EAU004
"""

import builtins

def outer():
	x = 'outer x'

	def inner():
		x = 'inner x'
		print(x)

	inner()
	print(x)

outer()