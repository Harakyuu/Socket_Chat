import socket #importa modulo socket

TCP_IP = '192.168.86.25' # endereço IP do servidor 
TCP_PORTA = 32031      # porta disponibilizada pelo servidor
TAMANHO_BUFFER = 1024


MENSAGEM  = input("Digite sua mensagem para o servidor: ")

# Criação de socket TCP do cliente
cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conecta ao servidor em IP e porta especifica 
cliente.connect((TCP_IP, TCP_PORTA))

# envia mensagem para servidor 
cliente.send(MENSAGEM.encode('UTF-8'))

conectado = True
while conectado:
    # recebe dados do servidor 
    data, addr = cliente.recvfrom(1024)
    if data: 
        print ("Mensagem recebida:", data)
        MENSAGEM = input("Digite sua mensagem para o servidor: ")
        cliente.send(MENSAGEM.encode('UTF-8'))
        if MENSAGEM == "QUIT":
            print("Saindo do cliente...")
            conectado = False
            cliente.close()
# fecha conexão com servidor
cliente.close()
