import socket
import json

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('127.0.0.1', 9897))
server.listen()
client, address = server.accept()

steps = []
with open('file.json', 'r') as f:
    data = f.read()
    if steps == []:
        pass
    else:
        steps.append(data)

flag = True
while flag:
    print('\nВы ходите крестиком')
    message = client.recv(1024).decode('utf-8')
    if message == 'quit':
        flag = False
    else:
        print()
        sign = 'o'
        steps.append({message: sign})
        with open('file.json', 'a') as f:
            json.dump({message: sign}, f)
    client.send(input('\nВаш ход (Введите номер ячейки) - ').encode('utf-8'))

client.close()
server.close()
