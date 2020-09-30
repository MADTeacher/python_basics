import socket
import time

UDP_IP = '127.0.0.1'
UDP_PORT = 8883


def run_client(ip, port):
    time.sleep(2)
    MESSAGE = u"""Эхо-служба (€) «Hello World!»"""
    sock = socket.socket(socket.AF_INET,  # IPv4
                         socket.SOCK_DGRAM)  # UDP
    server = (ip, port)
    for line in MESSAGE.split(' '):
        data = line.encode('utf-8')
        sock.sendto(data, server)
        print(f'Клиент|| На сервер {server} отправлено: {repr(data)}')
        response, address = sock.recvfrom(1024)  # размер буфера: 1024
        print(f"Клиент|| Получены данные: {repr(response.decode('utf-8'))}, "
              f"от {address}")
    print("Завершение работы клиента")


def run_server(ip, port):
    sock = socket.socket(socket.AF_INET,  # IPv4
                         socket.SOCK_DGRAM)  # UDP
    server = (ip, port)
    sock.bind(server)
    print(f'Запуск эхо-сервера: {server}')

    while True:
        data, address = sock.recvfrom(1024)  # размер буфера: 1024
        print(f"Сервер|| Получены данные: {repr(data.decode('utf-8'))}, "
              f"от {address}")
        sock.sendto(data, address)
        print(f'Сервер|| Отправлены данные: {repr(data)}, '
              f'по адресу: {address}')


if __name__ == "__main__":
    from multiprocessing import Process

    client = Process(target=run_client, args=(UDP_IP, UDP_PORT,))
    server = Process(target=run_server, args=(UDP_IP, UDP_PORT,))
    server.start()
    client.start()
    client.join()
    server.terminate()
