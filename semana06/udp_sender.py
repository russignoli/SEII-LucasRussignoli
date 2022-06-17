# importar bibliotecas ------------
import socket
import time
import sys
# ---------------------------------

# definir o ip, as portas de envio e o tamanho do buffer
UDP_IP = "127.0.0.1"
UDP_PORT = 5005
buf = 1024
file_name = sys.argv[1] # Recolher o nome do arquivo

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # Criando o socket para internet, com parâmetros de rede ip e protocolo udp

sock.sendto(file_name.encode('utf-8'), (UDP_IP, UDP_PORT)) # Iniciando a conexão usando o ip e porta udp
print ("Sending %s ..." % (file_name))

f = open(file_name, "r") # Abrindo o arquivo como leitura

data = f.read(buf) # Lendo o que há no arquivo
while(data):
	# Enviando o dado para a porta
    if(sock.sendto(data.encode('utf-8'), (UDP_IP, UDP_PORT))):
        data = f.read(buf)
        time.sleep(0.02) # Da ao receptor um pouco de tempo para economizar

# Fechando o socket e o arquivo
sock.close()
f.close()
