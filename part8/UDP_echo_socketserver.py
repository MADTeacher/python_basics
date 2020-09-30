from socketserver import BaseRequestHandler, UDPServer
from sample_part1 import run_client

UDP_IP = 'localhost'
UDP_PORT = 8000


class EchoUDP(BaseRequestHandler):
    def handle(self):
        print(f'Сервер|| Установлено соединение с '
              f': {self.client_address}')
        msg, sock = self.request
        print(f'Сервер|| Принято сообщение: "{msg.decode("utf-8")}" '
              f'от {self.client_address}')
        print(f'Сервер|| Эхо-сообщение: "{msg.decode("utf-8")}" '
              f'отправлено {self.client_address}')
        sock.sendto(msg, self.client_address)


if __name__ == "__main__":
    from multiprocessing import Process

    server = UDPServer((UDP_IP, UDP_PORT), EchoUDP)
    client = Process(target=run_client, args=(UDP_IP, UDP_PORT,))
    client.start()
    server.serve_forever()
