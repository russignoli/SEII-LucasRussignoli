import socket # Importa a biblioteca

TCP_IP = "127.0.0.1" # Define o IP
FILE_PORT = 5005 # Define a porta de envio
DATA_PORT = 5006 # define a porta de recepção
timeout = 3 # Definição do tempo limite
buf = 1024 # Define o tamanho do buffer


sock_f = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Cria o socket para internet, com o parametro de rede ip e protocolo tcp
sock_f.bind((TCP_IP, FILE_PORT)) # Vincula o nome do arquivo ao ip e a porta de recebimento.
sock_f.listen(1) #Escutando um de cada vez

sock_d = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Cria o socket para internet, com o parametro de rede ip e protocolo tcp
sock_d.bind((TCP_IP, DATA_PORT)) # Vincula o dado ao ip a porta de recebimento
sock_d.listen(1)


while True:
	# Conexão aceita com o socket do envio de nome do arquivo
	# retornando o socket e o endereço vinculado
    conn, addr = sock_f.accept()
    # Recebe o buffer e armazena em data
    data = conn.recv(buf).decode()
    # Se tiver algo, printa o nome do arquivo
    if data:
        print ("File name:", data)
        # Retirando espaços no inicio e fim
        file_name = 'novo_' + data.strip()

	# Abrindo o arquivo como escrita
    f = open(file_name, 'wb')

	# Conexão aceita com o socket do envio de dados retornando o socket e o endereço vinculado
    conn, addr = sock_d.accept()
    while True:
    	# Recebe os dados e escreve em um arquivo
        data = conn.recv(buf).decode()
        if not data:
            break
        f.write(data.encode('utf-8'))

	# Finaliza o arquivo
    print ("%s Finish!" % file_name)
    f.close()
    