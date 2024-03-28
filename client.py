from socket import socket , AF_INET , SOCK_STREAM
from threading import Thread as thr

client = socket(AF_INET,SOCK_STREAM)
client.connect(('localhost',6000))

name = input('NAME ?> ')

def recv():
    while True:
        try:
            message = client.recv(1024).decode('ascii')
            if message == 'name':
                client.send(name.encode('ascii'))
            else:
                print(message)
        except:
            print('Error !!!')
            client.close()
            break

def wr():
    while True:
        message = f'{name} {input('messge :> ')}'
        client.send(message.encode('ascii'))


thr(target=recv).start()
thr(target=wr).start()
