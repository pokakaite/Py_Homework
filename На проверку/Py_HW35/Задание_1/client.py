import socket
import json

with open('file.json', 'w') as f:
    data = {"1": " ",
            "2": " ",
            "3": " ",
            "4": " ",
            "5": " ",
            "6": " ",
            "7": " ",
            "8": " ",
            "9": " "}
    json.dump(data, f)


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
    if data[str(place_1)] == 'x' and data[str(place_1)] == data[str(place_2)] and data[str(place_1)] == data[
        str(place_3)]:
        print('\nВЫ ПОБЕДИЛИ.')
        print('Конец игры')
        client.close()
    elif data[str(place_1)] == 'o' and data[str(place_1)] == data[str(place_2)] and data[str(place_1)] == data[
        str(place_3)]:
        print('\nВЫ ПРОИГРАЛИ.')
        print('Конец игры')
        client.close()


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 9897))
print('Вы ходите крестиком.')
print(show_field())

while True:
    client_msg = input('\nВаш ход (Введите номер ячейки): ')
    save_to_json(client_msg, 'x')
    print(show_field())
    show_win_or_lose(1, 2, 3)
    show_win_or_lose(1, 4, 7)
    show_win_or_lose(1, 5, 9)
    show_win_or_lose(2, 5, 8)
    show_win_or_lose(4, 5, 6)
    show_win_or_lose(3, 5, 7)
    show_win_or_lose(3, 6, 9)
    show_win_or_lose(7, 8, 9)
    client.send(client_msg.encode('utf-8'))
    message = client.recv(1024).decode('utf-8')
    if message == 'quit':
        client.close()
    else:
        print('\nХод противника:')
        print(show_field())
