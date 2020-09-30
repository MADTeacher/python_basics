from socketserver import BaseRequestHandler, TCPServer
from sample_part2 import run_client

TCP_IP = 'localhost'
TCP_PORT = 8000

class EchoTCP(BaseRequestHandler):
    def handle(self):
        print(f'Сервер|| Установлено соединение с '
              f': {self.client_address}')
        while True:
            msg = self.request.recv(1024)
            if not msg:
                break
            print(f'Сервер|| Принято сообщение: "{msg.decode("utf-8")}" '
                  f'от {self.client_address}')
            print(f'Сервер|| Эхо-сообщение: "{msg.decode("utf-8")}" '
                  f'отправлено {self.client_address}')
            self.request.send(msg)



if __name__ == "__main__":
    from multiprocessing import Process

    server = TCPServer((TCP_IP, TCP_PORT), EchoTCP)
    client = Process(target=run_client, args=(TCP_IP, TCP_PORT,))
    client.start()
    server.serve_forever()
