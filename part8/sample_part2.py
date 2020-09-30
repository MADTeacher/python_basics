import socket
from concurrent import futures as cf
import time

TCP_IP = 'localhost'
TCP_PORT = 8883


def run_client(ip, port):
    time.sleep(4)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((ip, port))
        print('Клиент|| Соединение с сервером установлено')
        data = u"""Эхо-служба (€) «Hello World!»"""
        for line in data.split(' '):
            sock.sendall(line.encode('utf-8'))
            print(f'Клиент|| Отправлено: "{line}"')
            response = sock.recv(1024)
            print(f"Клиент|| Ответ сервера: ''{response.decode('utf-8')}''")
    print('Клиент|| Соединение с сервером закрыто')


def run_server(ip, port):
    def handle(new_sock, address):
        print(f'Сервер|| Установлено соединение с : {address} ')
        while True:
            received = new_sock.recv(1024)
            if not received: break
            s = received.decode('utf-8', errors='replace')
            print(f'Сервер|| Принято сообщение: "{s}" от {address}')
            new_sock.sendall(received)
            print(f'Сервер|| Эхо-сообщение: "{s}" отправлено {address}')
        new_sock.close()
        print(f'Сервер|| Закрыто соединение с : {address}')

    servsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servsock.bind((ip, port))
    servsock.listen(5)
    print(f'Запуск эхо-сервера: {servsock.getsockname()}')
    with cf.ThreadPoolExecutor(20) as client_pool:
        try:
            while True:
                new_sock, address = servsock.accept()
                client_pool.submit(handle, new_sock, address)
        except KeyboardInterrupt:
            pass
        finally:
            servsock.close()



if __name__ == "__main__":
    from multiprocessing import Process

    client = Process(target=run_client, args=(TCP_IP, TCP_PORT,))
    server = Process(target=run_server, args=(TCP_IP, TCP_PORT,))
    server.start()
    client.start()
    client.join()
    server.terminate()
