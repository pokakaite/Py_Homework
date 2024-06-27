import json
import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.2', 9897))

login = 'koka'
client_msg = client.send(login.encode('utf-8'))

while True:
    client_msg = input('Вы: ')
    client.send(client_msg.encode('utf-8'))
    with open('file.json', 'w') as f:
        json.dump({login: client_msg}, f)
    server_msg = client.recv(1024).decode('utf-8')
    print(server_msg)