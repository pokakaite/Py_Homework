import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 9897))

client_msg = input('Client: ')
client.send(client_msg.encode('utf-8'))
server_msg = client.recv(1024).decode('utf-8')

print(server_msg)

client.close()