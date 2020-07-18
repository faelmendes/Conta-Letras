#!/bin/bash/python2
import socket
from threading import Thread


class ServerThread(Thread):

    def __init__(self, con):
        ''' Constructor. '''
        Thread.__init__(self)
        self.con = con
        self.con.send = con.send
        self.con.recv = con.recv
        self.start()

    def run(self):
        palavra = self.con.recv(1024)
        self.con.send("ack")
        self.con.recv(1024)
        print palavra
        i=0
        s=0
        numero=0
        numeros = "0123456789"
        while i < len(palavra):
            for a in numeros:
                if a == palavra[i]:
                   s+= 1
            i+=1
        calculo = (i - s)
        fim = "numero de letras e "+str(calculo)
        self.con.send(fim)
        self.con.close()

ip = socket.gethostbyname(socket.gethostname())
porta = int(2222)
print ("Servidor executando. "+ip)
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
try:
    server.bind((ip,porta))
except:
    print "porta em uso"
server.listen(10)
while True:
    con, cliente = server.accept()
    print 'conectado com ',cliente
    conexao = ServerThread(con)
















