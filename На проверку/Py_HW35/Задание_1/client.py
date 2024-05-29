import socket
import json

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 9897))

steps = []
with open('file.json', 'r') as f:
    data = f.read()
    if steps == []:
        pass
    else:
        steps.append(data)




flag = True
while flag:
    print('\nВы ходите ноликом.')
    client.send(input('Ваш ход (Введите номер ячейки) - ').encode('utf-8'))
    message = client.recv(1024).decode('utf-8')
    if message == 'quit':
        flag = False
    else:
        print()
        sign = 'x'
        steps.append({message: sign})
        with open('file.json', 'a') as f:
            json.dump({message: sign}, f)


client.close()
