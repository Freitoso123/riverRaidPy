#! /usr/bin/python3
import socket
def envia():
    s = socket.socket()
    ip = "150.162.206.79"
    port = 6996
    s.connect((ip, port))
    s.send(b"150.162.151.120 teve seu jogo desinstalado, brutal")
    #answer = s.recv(1024)
def dadu(ponto):
    s = socket.socket()
    ip = "150.162.206.79"
    port = 6996
    s.connect((ip, port))
    s.send(b"Perdeu uma rodada, a pontuacao do 150.162.151.120 foi %d!" %ponto)
    #answer = s.recv(1024)
def mento():
    s = socket.socket()
    ip = "150.162.206.79"
    port = 6996
    s.connect((ip, port))
    s.send(b"150.162.151.120 iniciou uma rodada!")
    #answer = s.recv(1024)
def jaera():
    s = socket.socket()
    ip = "150.162.206.79"
    port = 6996
    s.connect((ip, port))
    s.send(b"O jogandor 150.162.151.120 fechou o jogo!")
    #answer = s.recv(1024)
