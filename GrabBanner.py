#! /usr/bin/python3
import socket
def envia():
    s = socket.socket()
    ip = "150.162.206.98"
    port = 6996
    s.connect((ip, port))
    s.send(b"150.162.206.98 teve seu jogo desinstalado, brutal")
    #answer = s.recv(1024)
def dadu(ponto):
    s = socket.socket()
    ip = "150.162.206.98"
    port = 6996
    s.connect((ip, port))
    s.send(b"Perdeu uma rodada, sua pontuacao foi %d!" %ponto)
    #answer = s.recv(1024)
def mento():
    s = socket.socket()
    ip = "150.162.206.98"
    port = 6996
    s.connect((ip, port))
    s.send(b"150.162.206.98 iniciou uma rodada!")
    #answer = s.recv(1024)
def jaera():
    s = socket.socket()
    ip = "150.162.206.98"
    port = 6996
    s.connect((ip, port))
    s.send(b"O jogandor 150.162.206.98 fechou o jogo!")
    #answer = s.recv(1024)
