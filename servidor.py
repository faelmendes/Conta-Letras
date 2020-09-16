import socket
from threading import Thread

def tred(con):
	palavra = con.recv(1024)
	con.send("ack")
	con.recv(1024)
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
	con.send(str(calculo))
	con.close()

ip = socket.gethostbyname(socket.gethostname())
porta = int(2222)
print ("Servidor executando. "+ip)
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
try:
    server.bind((ip,porta))
except:
    print ("porta em uso")
server.listen(10)
while True:
    con, cliente = server.accept()
    print ('conectado com ',cliente)
    t1 = Thread(target=tred, args=(con,)).start()
