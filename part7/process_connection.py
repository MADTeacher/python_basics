from multiprocessing.connection import Listener, Client
from multiprocessing import Process
from array import array

def server():
    address = ('localhost', 6000)  # family is deduced to be 'AF_INET'
    with Listener(address, authkey=b'secret password') as listener:
        with listener.accept() as conn:
            print('connection accepted from', listener.last_accepted)
            conn.send([2.25, None, 'junk', float])
            conn.send_bytes(b'hello')
            conn.send_bytes(array('i', [42, 1729]))

def client():
    address = ('localhost', 6000)
    with Client(address, authkey=b'secret password') as conn:
        print(conn.recv())  # => [2.25, None, 'junk', float]
        print(conn.recv_bytes())  # => b'hello'
        arr = array('i', [0, 0, 0, 0, 0])
        print(conn.recv_bytes_into(arr))  # => 8
        print(arr)  # => array('i', [42, 1729, 0, 0, 0])

if __name__ == "__main__":
    my_server = Process(target=server)
    my_client = Process(target=client)
    my_server.start()
    my_client.start()
