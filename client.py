import socket
from time import sleep

sock = socket.socket()
sock.setblocking(1)
sock.connect(('localhost', 9090))


while True:
    msg = input("Input message: ")
    if msg == "exit":
        sock.close()
        break
    sock.send(msg.encode())
    data = sock.recv(1024)
