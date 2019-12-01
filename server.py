# coding:utf-8

import socket

host, port = ('', 6666)
socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
socket.bind((host,port))
print("Le serveur est UP...")


while True:
    socket.listen(5)
    conn, address = socket.accept()
    print("en écoute....")

conn.close()
socket.close()
