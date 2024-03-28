from socket import socket , AF_INET , SOCK_STREAM
from threading import Thread as thr

s = socket(AF_INET,SOCK_STREAM)
s.bind(('localhost',6000))
s.listen()

clients = []
names = []

def main(message):
    for client in clients:
        client.send(message)

def handel(client):
    while True:
        try:
            message = client.recv(1024)
            main(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            clients.close()
            name = names(index)
            print(f'{name} Lefted The Chat Room'.encode('ascii'))
            names.remove(name)
            break

def recvv():
    while True:
        client, addres = s.accept()
        print('Client Connected !!!')
        client.send('name'.encode('ascii'))
        name = client.recv(1024).decode()
        clients.append(client)
        print(f'Hello {name}')
        main(f'{name} joined the chat !'.encode('ascii'))
        client.send(f'{name} Connected To Server !!!'.encode('ascii'))
        t = thr(target=handel, args=(client,)).start()

recvv()
