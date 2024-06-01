import socket

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind(('127.0.0.2', 9897))

clients = []

login = server.recv(1024).decode('utf-8')
while True:
    client_msg, address = server.recvfrom(1024)

    if address not in clients:
        clients.append(address)

    print(f'{login}: {client_msg.decode('utf-8')}')

    for client in clients:
        if address != client:
            server.sendto(f'{login}: {client_msg.decode('utf-8')}'.encode('utf-8'), client)

server.close()