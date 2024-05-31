import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind(('127.0.0.1', 9897))
server.listen()
client, address = server.accept()

while True:
    message = client.recv(1024).decode('utf-8')
    if message == 'quit':
        client.close()
        server.close()
    elif message == '1':
        print('Клиент хочет отправить вам файл.')
        print('''\nХотите принять файл?
        1 - Да
        2 - Нет''')
    else:
        print(message)
    server_msg = input('Ваш выбор - ')
    client.send(server_msg.encode('utf-8'))