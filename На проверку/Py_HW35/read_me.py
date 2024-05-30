# Задание 1
# Реализуйте клиент — серверное приложение, позволяющее двум людям играть в игру крестики — нолики.
# Один из игроков инициирует игру, если второй игрок
# подтверждает, то игра начинается. Игру можно прекратить,
# тот кто прекратил игру считается проигравшим. После
# завершения игры, можно инициировать повторный матч.

# Задание 2
# Реализуйте клиент — серверное приложение, позволяющее передавать файлы. Один пользователь инициирует
# передачу файла, второй подтверждает. После подтверждения начинается отправка. Если отправка была удачной
# необходимо сообщить об этом отправителю.

# Задание 3
# Реализуйте клиент — серверное приложение, позволяющее пользователям общаться в одном чате. Каждый
# пользователь входит в чат под своим логином и паролем.
# Сообщение, отправленное в чат видно всем пользователям чата.


# import socket
#
# while True:
#     server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     server.bind(('127.0.0.1', 9897))
#     server.listen()
#     client, address = server.accept()
#     message = client.recv(1024).decode('utf-8')
#     if message == 'quit':
#         pass
#     else:
#         print(message)
#     client.send(input('Server: ').encode('utf-8'))
#
#     client.close()
#     server.close()
#
#
#
#
# import socket
#
# while True:
#     client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     client.connect(('127.0.0.1', 9897))
#
#     client.send(input('Client: ').encode('utf-8'))
#     message = client.recv(1024).decode('utf-8')
#     if message == 'quit':
#         pass
#     else:
#         print(message)
#
#     client.close()


field = {}
field.update({1: 'x'})
print(field)
field.update({2: 'o'})
print(field)
print(type(field))