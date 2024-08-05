import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind(('127.0.0.1', 9897))
server.listen()
client, address = server.accept()

flag = True
while flag:
    message = client.recv(1024).decode('utf-8')
    match message:
        case '1': print('''\nКлиент хочет отправить вам файл.
        Хотите принять файл?
        1 - Да
        2 - Нет''')
        case '2': break

    server_msg = input('Ваш выбор - ')
    if server_msg == '2':
        break
    client.send(server_msg.encode('utf-8'))
    while flag:
        file_name = client.recv(1024).decode('utf-8')
        f = open(file_name, 'wb')
        flag1 = True
        while flag1:
            data = client.recv(1024)
            f.write(data)
            print('Файл успешно доставлен.')
            flag = False
            flag1 = False
            f.close()
client.close()
server.close()