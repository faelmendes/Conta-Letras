#!/bin/bash/python2
import socket
import sys
serverName = sys.argv[1]  # args[0]
serverPort = int(sys.argv[2]) # args[1]
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
clientSocket.send(sys.argv[3])
clientSocket.recv(1024)
clientSocket.send("ack")
msg = clientSocket.recv(1024)
print msg
clientSocket.close()

