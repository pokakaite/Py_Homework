import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 9897))
client_msg = input(f'''\nЧто вы хотите сделать?
        1 - Передать файл
        2 - Выйти
Ваш выбор - ''')
if client_msg == 2:
    client.close()
else:
    client.send(client_msg.encode('utf-8'))
    message = client.recv(1024).decode('utf-8')
    match message:
        case '1':
            file_name = input('\nСервер согласился.\nВведите название файла, который хотите передать - ')
            with open(file_name, 'rb') as f:
                data = f.read(1024)
            client.send(file_name.encode('utf-8'))
            client.send(data)
            print('Файл успешно доставлен.')
        case '2': client.close()