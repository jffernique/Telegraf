# coding:utf-8

import socket
import threading

class MultiClient(threading.Thread):
    def __init__(self,client):
        threading.Thread.__init__(self)
        self.conn=conn
    def run(self):
        data =self.conn.recv(1024)
        data=data.decode("utf8")
        print(data)



host, port = ('', 6666)
socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
socket.bind((host,port))
print("Le serveur est UP...")


while True:
    socket.listen(5)
    conn, address = socket.accept()
    print("en écoute....")
    my_thread = MultiClient (conn)
    my_thread.start()

conn.close()
socket.close()
