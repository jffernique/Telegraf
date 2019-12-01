#coding:utf-8

import socket

host, port = ('localhost', 6666)
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:

    socket.connect((host,port))
    print("serveur connecté!!!")

except:
    print("Connection erreur:::")
finally:
    socket.close()
