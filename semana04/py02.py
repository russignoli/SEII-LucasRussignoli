"""
Atividade Semana 04 - Sistemas Embarcados
Lucas Russignoli 11721EAU004
"""

message = 'Olá Mundo'
print('Olá Mundo')
print(message)
print(len(message))
print(message[0])
print(message[0:3])
print(message[4:])
print(message.lower())
print(message.upper())
print(message.count('Olá'))
print(message.find('Olá'))
print(message.find('Universo'))
new_message = message.replace('Mundo', 'Universo')
print(new_message)
greeting = 'Olá'
name = 'Lucas'
message2 = greeting + ', ' + name + '. Welcome!'
print(message2)
message3 = '{}, {}. Welcome!'.format(greeting, name)
print(message3)
message4 = f'{greeting}, {name}. Welcome!'
print(message4)
print (dir(name))
