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
        calculo=0
        letras = [65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,
                   97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122]
        while i < len(palavra):
            for a in letras:
                if chr(a) == palavra[i]:
                   calculo+= 1
            i+=1
        fim = "numero de letras e "+str(calculo) #funciona com letras maiúsculas e menusculas
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
