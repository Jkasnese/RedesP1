#!/usr/bin/python
# -*- coding: utf-8 -*-

# Testando abertura de sockets pra comunicação

import socket
socket.error
import sys
from thread import *

HOST = ''   # Symbolic name, meaning all available interfaces. Quando põe nome não roda, não entendi pq.
PORT = 8888 # Arbitrary non-privileged port

#   - - -   Criando socket - - - 

try:
    # Retorna descrição do socket
    # Cria um socket da familia de endereços INET, usado pra protocolos ipv4.
    #   A familia de endereços diz que tipos de endereços podem se acoplar a esse socket. Pra internet, INET. Tem tb INET6 pra ipv6.
    bocal = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

except socket.error as msg:
    print 'Nao foi possivel criar o socket. ERro: ' + str(msg[0]) + ' , Mensagem: ' + msg[1]
    sys.exit();

print "Socket criado!"

#   - - - Atribuindo dados ao socket - - - 

try:
    # Atribuindo ao meu socket atual o nome HOST e a porta do socket.
    bocal.bind((HOST, PORT))

except socket.error as msg:
    print 'Erro na atribuicao. Codigo: ' + str(msg[0]) + ' Mensagem: ' + msg[1]
    sys.exit()

print "Atribuido porta e nome!"

#   - - - - Criando "fila", começando a ouvir - - - 

# Fazer o socket começar a ouvir. Fila máxima de 3 conexões.
bocal.listen(3)

print "Bocal eh boca mas ta ouvindo!"

# Definindo uma funcao pra trabalhar com multiplas threads

def clienteThread(conn):
    # Mandar msg a todo cliente que se conectar
    conn.send("Ola mundo! Bem vindo ao servidor que não faz nada! Vamos conversar!\n")
    
    # Deixar a thread pra sempre recebendo dados
    while True:
        # data recebe os dados de no maximo 140, neste caso. Acho que bytes.
        data = conn.recv(140)
        # Seja educado e responda
        resposta = 'Beleza! Você disse: ' + data
        if not data:
            break;
        
        conn.sendall(resposta)

    conn.close()

# - - - -   Rodando - - - -

# Criando threads pra sempre

while True:
    # Aguardando ligacoes
    conn, addr = bocal.accept()
    print "Nova conexão! " + addr[0] + ':' + str(addr[1])

    # Os argumentos de começar uma nova thread é a função e sua lista de argumentos.
    # Os argumentos da função tem que vir em formato de tupla. Creio que pq tupla é imutável.
    start_new_thread(clienteThread, (conn,))

bocal.close()
