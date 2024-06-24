import json
import socket
import concurrent.futures
import time

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind(('127.0.0.2', 9897))
server.listen()

def get_client():
    client, address = server.accept()
    clients = []
    if address not in clients:
        clients.append(address)

def login(client):
    time.sleep(2)
    login = client.recv(1024).decode('utf-8')
    client_msg = client.recv(1024).decode('utf-8')
    time.sleep(1)
    with open('file.json', 'r+') as f:
        data = json.load(f)
        print(data)
    for c in clients:
        client.sendto(f'{login}: {data[login]}'.encode('utf-8'), address)


    with concurrent.futures.ThreadPoolExecutor() as executor:
        result = executor.submit(get_client)
        result_2 = executor.submit(login)
