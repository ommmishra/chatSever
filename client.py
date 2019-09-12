from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread

def receive():
    while True:
        try:
            print(client_socket.recv(BUFSIZ).decode("utf8"))
        except OSError:
            break

def send():
    msg = input()
    client_socket.send(bytes(msg, "utf8"))
    if msg== "{quit}":        
        client_socket.close()

HOST = '127.0.0.1'
PORT = 33000

BUFSIZ = 1024
ADDR = (HOST, PORT)

client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect(ADDR)


THREAD_RECEIVE = Thread(target=receive)
THREAD_RECEIVE.start()

while True:
    send()


