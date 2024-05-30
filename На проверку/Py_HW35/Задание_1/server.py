import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('127.0.0.1', 9897))
server.listen()
client, address = server.accept()
client_msg = client.recv(1024).decode('utf-8')

print(client_msg)
server_msg = input('Server: ')
client.send(server_msg.encode('utf-8'))

client.close()
server.close()