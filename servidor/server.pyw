import socket
import os
from sys import path
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#ifnet = ipv4, sock_stream = tcpip
s.bind((socket.gethostbyname("23.1.1.238"), 12397))
s.listen(5)
print("conectado")
while True:
    clientsocket, addres = s.accept()
    print(f"CONNECTION FROM {addres} has been established!")
    while True:
        msg = clientsocket.recv(1024)
        if msg:
            try:
                caminho = path[0]+"/main.pyw"
                print(msg.decode())
                os.system("python "+caminho)
            except:
                print("ocorreu um erro")
        else:
            break
