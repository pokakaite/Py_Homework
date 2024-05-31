import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 9897))
client_msg = input(f'''\nЧто вы хотите сделать?
1 - Передать файл
2 - Выйти
''')
if client_msg == 2:
    client.close()
else:
    while True:
        client.send(client_msg.encode('utf-8'))
        message = client.recv(1024).decode('utf-8')
        file_name = input('\nВведите название файла, который хотите передать - ')
        if message == '1':
            client.send(file_name.encode('utf-8'))
        elif message == '2':
            client.close()
        elif message == 'quit':
            client.close()
        else:
            print(message)