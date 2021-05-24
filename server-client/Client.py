from socket import *
from os import system

class Client:

    def __init__(self) -> None:
        self.__client_socket = None


    def create_socket(self):
        self.__client_socket = socket(AF_INET, SOCK_STREAM)


    def create_binded_socket(self, cli_addr, cli_port):
        self.__client_socket = socket(AF_INET, SOCK_STREAM)
        self.__client_socket.bind((cli_addr,cli_port))

    
    def connect_to(self, serverName, serverPort):
        self.__client_socket.connect((serverName, serverPort))

    
    def send_data(self, data):
        self.__client_socket.send(data.encode())


    def receive_data(self):
        return self.__client_socket.recv(1024).decode()


    def close_connection(self):
        self.__client_socket.close()

    def run(self, app):
        app()

        


def my_app():
    pass
    
    
    

if __name__ == "__main__":
    serverName = '127.0.0.1'
    serverPort = 12000
    server = serverName, serverPort

    cli1 = Client()
    cli1.create_socket()
    cli1.connect_to(*server)

    sentence = ''
    while True:
        system("clear")
        sentence = input("Input a lowercase sentence: ")
        if sentence == "quit()":
            break

        cli1.send_data(sentence)

        response = cli1.receive_data()

        system("clear")
        print(f"From Server: {response}")
        input("Press <Enter> to continue...")
    cli1.close_connection()

