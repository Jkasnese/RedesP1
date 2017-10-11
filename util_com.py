import socket
from queue import Queue

# Comunicação UDP

""" Cria socket e envia mensagem"""
def enviarUDP(MESSAGE, UDP_IP, UDP_PORT=5005):
    sock = socket.socket(socket.AF_INET, # Internet
                         socket.SOCK_DGRAM) # UDP
    sock.sendto(str.encode(MESSAGE), (UDP_IP, UDP_PORT))
    return sock

def abrirSocketUDP(UDP_PORT=5005):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(('', UDP_PORT))
    return sock

def ouvir_socket(socket):
    while True:
        data, addr = socket.recvfrom(1024) # buffer size is 1024 bytes
        return bytes.decode(data), addr

""" Cadastrar sensor
    Cria socket, envia mensagem, recebe resposta e fecha conexão
    Atributos:
        mensagem
        ip
        porta"""
def enviar_cadastro_TCP(mensagem, bocal):
    bocal.send(mensagem.encode('utf-8'))
    resposta = bocal.recv(1024) # Buffer de 1024 pra resposta
    resposta = resposta.decode('utf-8')
    if ('0' == resposta):
        bocal.close()
    return resposta

def enviar_TCP(mensagem, bocal):
    bocal.send(mensagem.encode('utf-8'))
    return

def abrirSocketTCP(porta=8080, host=''):
    #   - - -   Criando socket - - - 
    try:
        # Retorna descrição do socket
        # Cria um socket da familia de endereços INET, usado pra protocolos ipv4.
        #   A familia de endereços diz que tipos de endereços podem se acoplar a esse socket. Pra internet, INET. Tem tb INET6 pra ipv6.
        bocal = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error as msg:
        print ('Nao foi possivel criar o socket. Erro: ' + str(msg[0]) + ' , Mensagem: ' + msg[1])
        sys.exit();

    #   - - - Atribuindo dados ao socket - - - 
    try:
        # Atribuindo ao meu socket atual o nome HOST e a porta do socket.
        bocal.bind((host, porta))
    except socket.error as msg:
        print ('Erro na atribuicao. Codigo: ' + str(msg[0]) + ' Mensagem: ' + msg[1])
        sys.exit()

    return bocal

""" Pede um socket e retorna a string de resposta"""
def ouvirTCP(bocal):
    # Deixar a thread pra sempre recebendo dados
    while True:
        # data recebe os dados de no maximo 1024 bytes, neste caso.
        mensagem = (bocal.recv(1024)).decode('utf-8')
        # Seja educado e responda
        return mensagem        

def aceitar_conexoes(bocal, lista_conexoes):
    # Ouvindo
    while True:
        # Coloca na lista uma tupla contendo bocal de conexão e endereço
        conexao = bocal.accept()
        lista_conexoes.put(conexao)
        lista_conexoes.task_done()
        print ("Nova conexão TCP! " + conexao[1][0] + ':' + str(conexao[1][1]))

