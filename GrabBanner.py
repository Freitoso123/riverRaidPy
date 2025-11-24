#! /usr/bin/python3
import socket
def envia():
    s = socket.socket()
    ip = "150.162.206.65"
    port = 6996
    s.connect((ip, port))
    s.send(b"Teve seu jogo desinstalado")
    #answer = s.recv(1024)
def dadu():
    s = socket.socket()
    ip = "150.162.206.65"
    port = 6996
    s.connect((ip, port))
    s.send(b"Perdeu uma rodada!")
    #answer = s.recv(1024)
def mento():
    s = socket.socket()
    ip = "150.162.206.65"
    port = 6996
    s.connect((ip, port))
    s.send(b"Iniciou uma rodada!")
    #answer = s.recv(1024)
def jaera():
    s = socket.socket()
    ip = "150.162.206.65"
    port = 6996
    s.connect((ip, port))
    s.send(b"Fechou o jogo!")
    #answer = s.recv(1024)
    
