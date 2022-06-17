# importar bibliotecas ------------
import socket
import select
# ---------------------------------

# definir o ip, as portas de envio e o tempo limite
UDP_IP = "127.0.0.1"
IN_PORT = 5005
timeout = 3

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # Criando o socket para internet, com parâmetros de rede ip e protocolo udp
sock.bind((UDP_IP, IN_PORT)) # Vinculando ao ip e a porta de recebimento do nome do arquivo

while True:
	
    data, addr = sock.recvfrom(1024) # Recebendo dados de 1024 bytes. Retornando o dado e o endereço de origem
    if data:
        print ("File name: ", data) # Printando o nome do arquivo recebido
        file_name = 'novo_' + data.strip().decode() # Retirando espaços no inicio e fim

    f = open(file_name, 'wb') # Abrindo arquivo no modo de escrita

    while True:
        ready = select.select([sock], [], [], timeout) #Aguarda até estar pronto para a leitura
        if ready[0]:
            data, addr = sock.recvfrom(1024)# Se existir, recebe a quantidade de dado e escreve no arquivo
            f.write(data)
        else:
        	# Finaliza e fecha o arquivo
            print ("%s Finish!" % (file_name))
            f.close()
            break
        