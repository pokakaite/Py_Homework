import socket
import json
def save_to_json(message, sign):
    with open('file.json', 'r+') as f1:
        data = json.load(f1)
        data.update({message: sign})
    with open('file.json', 'w') as f2:
        json.dump(data, f2)

def show_field():
    with open('file.json', 'r') as f:
        data = json.load(f)

    return f'''\n {data['1']} | {data['2']} | {data['3']} 
---+---+---
 {data['4']} | {data['5']} | {data['6']}
---+---+---
 {data['7']} | {data['8']} | {data['9']}'''

def show_win_or_lose(place_1, place_2, place_3):
    with open('file.json', 'r') as f:
        data = json.load(f)
    if data[str(place_1)] == 'o' and data[str(place_1)] == data[str(place_2)] and data[str(place_1)] == data[str(place_3)]:
        print('\nВЫ ПОБЕДИЛИ.')
        print('Конец игры')
        client.close()
        server.close()
    elif data[str(place_1)] == 'x' and data[str(place_1)] == data[str(place_2)] and data[str(place_1)] == data[str(place_3)]:
        print('\nВЫ ПРОИГРАЛИ.')
        print('Конец игры')
        client.close()
        server.close()

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind(('127.0.0.1', 9897))
server.listen()
client, address = server.accept()
print('Вы ходите ноликом.')

while True:
    message = client.recv(1024).decode('utf-8')
    if message == 'quit':
        client.close()
        server.close()
    else:
        print('\nХод противника:')
        print(show_field())
    server_msg = input('\nВаш ход (Введите номер ячейки): ')
    save_to_json(server_msg, 'o')
    print(show_field())
    show_win_or_lose(1, 2, 3)
    show_win_or_lose(1, 4, 7)
    show_win_or_lose(1, 5, 9)
    show_win_or_lose(2, 5, 8)
    show_win_or_lose(4, 5, 6)
    show_win_or_lose(3, 5, 7)
    show_win_or_lose(3, 6, 9)
    show_win_or_lose(7, 8, 9)
    client.send(server_msg.encode('utf-8'))

