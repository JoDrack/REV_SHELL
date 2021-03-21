import socket
from rich import print

HOST = socket.gethostbyname(socket.gethostname())
PORT = 1234
ADDRESS = (HOST, PORT)
HOST_NAME = socket.gethostname()

try:
    client = socket.socket()
    client.connect(ADDRESS)
    print('Connected')

    while True:
        # sending the HOST_NAME to the server
        client.send(HOST_NAME.encode("utf-8"))
    # print('[bold green]HostName sent successfully')
        data = client.recv(1024).decode()
        print(data)

except ConnectionResetError as cnct_err:
    print(f'Connection error -> {cnct_err}')
    raise SystemExit