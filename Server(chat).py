import socket #importa modulo socket
 
TCP_IP = '192.168.86.25' # endereço IP do servidor 
TCP_PORTA = 32031       # porta disponibilizada pelo servidor
TAMANHO_BUFFER = 1024     # definição do tamanho do buffer
 
# Criação de socket TCP
# SOCK_STREAM, indica que será TCP.
servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# IP e porta que o servidor deve aguardar a conexão
servidor.bind((TCP_IP, TCP_PORTA))

#Define o limite de conexões. 
servidor.listen(1)

print("Servidor disponivel na porta 5005 e escutando.....") 
# Aceita conexão 
conn, addr = servidor.accept()
print ('Endereço conectado:', addr)

conectado = True
while conectado:
    #dados retidados da mensagem recebida
    data = conn.recv(TAMANHO_BUFFER)
    if data: 
        print ("Mensagem recebida:", data)
        MENSAGEM  = input("Digite sua mensagem para o cliente: ")
        conn.send(MENSAGEM.encode('UTF-8'))  
        if MENSAGEM == "QUIT":
            print("Saindo do servidor...")
            conectado = False
conn.close()
