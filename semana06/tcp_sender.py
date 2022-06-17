# Importa biblioteca -------
import socket 
import sys
# --------------------------
TCP_IP = "127.0.0.1" # Define o IP
FILE_PORT = 5005 # Define a porta de envio
DATA_PORT = 5006 # define a porta que recebe
buf = 1024 1024 # Tamanho do buffer
file_name = sys.argv[1] # Nome do arquivo

try:
	
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Criando o socket para internet, com parâmetros de rede ip e protocolo tcp
    # Iniciando a conexão usando o ip e porta de envio de arquivo
    sock.connect((TCP_IP, FILE_PORT))  # Inicia a conexão usando o ip e porta de envio
    sock.send(file_name.encode('utf-8')) # Envia o tipo do nome do arquivo
    sock.close() # Fecha a conexão
    print ("Sending %s ..." % (file_name))

	
    f = open(file_name, "rb") # Abrindo o arquivo como leitura
   
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Abrindo novamente a conexão
    # Iniciando a conexão usando o ip e porta de envio de dado
    sock.connect((TCP_IP, DATA_PORT # Iniciando a conexão usando o ip e porta de envio de dado
    data = f.read() # Lendo o que há no arquivo
    sock.send(data) # Enviando o conteúdo do arquivo

finally:
	# Fechando a conexão e o arquivo
    sock.close()
    f.close()
    