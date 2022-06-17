# Importa biblioteca ------------
import socket
import threading 
import time 
# -------------------------------

SERVER_IP = socket.gethostbyname(socket.gethostname()) # Cria o IP baseado no host
PORT = 5050 # Define a porta
ADDR = (SERVER_IP, PORT) # Determina o endereço
FORMATO = 'utf-8' # Define o formato das mensagens 'pt'

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Cria o socket padrão TCP
server.bind(ADDR) # Vincula com o endereço

conexoes = [] # Lista as conexões
mensagens = [] #Lista as mensagens

def enviar_mensagem_individual(conexao):
    print(f"[ENVIANDO] Enviando mensagens para {conexao['addr']}")
    for i in range(conexao['last'], len(mensagens)): # Vai enviar as mensagens desde a ultima recebida até a quantidade total
        mensagem_de_envio = "msg=" + mensagens[i] # Concatena a mensagem com o inicio "msg="
        conexao['conn'].send(mensagem_de_envio.encode()) # Envia a mensagem para a conexão
        conexao['last'] = i + 1 # Atualiza a última mensagem enviada
        time.sleep(0.2) # Tempo antes de enviar a próxima mensagem

def enviar_mensagem_todos():
    global conexoes
    for conexao in conexoes: # Enviando a mensagem individual para cada conexão
        enviar_mensagem_individual(conexao)


def handle_clientes(conn, addr):
    print(f"[NOVA CONEXAO] Um novo usuario se conectou pelo endereço {addr}") # Mostra que uma nova conexão foi criada
    global conexoes # Variáveis globais
    global mensagens
    nome = False

    while(True):
        msg = conn.recv(1024).decode(FORMATO) # Codifica e armazena a mensagem recebida
        if(msg):
            if(msg.startswith("nome=")): # Se a mensagem começar com "nome=", armazena o nome
                mensagem_separada = msg.split("=") # A mensagem é separada
                nome = mensagem_separada[1] # O noome é armazenado para Conexão
                mapa_da_conexao = { # Mapa com informações do cliente
                    "conn": conn,
                    "addr": addr,
                    "nome": nome,
                    "last": 0
                }
                conexoes.append(mapa_da_conexao) # Mapa do novo cliente adicionado as conexões
                enviar_mensagem_individual(mapa_da_conexao) # Recebe mensagens antigas
            elif(msg.startswith("msg=")): # Se a mensagem começa com "msg=", temos uma nova mensagem
                mensagem_separada = msg.split("=") # A mensagem é separada
                mensagem = nome + "=" + mensagem_separada[1] # Armazena a mensagem
                mensagens.append(mensagem) # Adicionando as mensagens
                enviar_mensagem_todos() # Envia mensagem para todos


def start():
    print("[INICIANDO] Iniciando Socket") # Inicia o socket
    server.listen() # Estabelece conexão com o socket
    while(True):
        conn, addr = server.accept() # Quando ouver conexão, ele armazena o socket e o enredeço
        thread = threading.Thread(target=handle_clientes, args=(conn, addr)) # Cria uma thread para a conexão 
        thread.start() # Inicia a thread

start()
