import socket

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client.connect(('127.0.0.2', 9897))
server = ('127.0.0.2', 9897)

make_login = input('Придумайте логин: ')
make_password = input('Придумайте пароль: ')

choice = int(input('''Что вы хотите сделать?
        1 - Войти в чат
        2 - Выйти
        '''))

match choice:
    case 2:
        client.close()
    case 1:
        login = input('Введите логин: ')
        client.send(login.encode('utf-8'))
        password = input('Введите пароль: ')

        if login == make_login and password == make_password:
            print('Вы вошли в чат и можете отправлять сообщения.')
            while True:
                client_msg = input(f'\n{login}: ')
                client.send(client_msg.encode('utf-8'))
                server_msg = client.recv(1024).decode('utf-8')
                print(server_msg)