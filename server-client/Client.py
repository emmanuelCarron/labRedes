from socket import *

class Client:

    def __init__(self, server_name, server_port):
        self.create_socket(server_name, server_port)


    def create_socket(self, server_name, server_port):
        self.__client_socket = socket(AF_INET, SOCK_STREAM)
        self.__client_socket.connect((server_name, server_port))

       
    def send_data(self, data):
        self.__client_socket.send(data.encode())


    def receive_data(self):
        return self.__client_socket.recv(1024).decode()


    def close_connection(self):
        self.__client_socket.close()

#     def run(self, app):
#         app()

        


# def my_app():
#     pass
    
    
    

if __name__ == "__main__":
    serverName = '127.0.0.1'
    serverPort = 12000

    my_cli = Client(serverName, serverPort)

    sentence = input("Input a lowercase sentence:\n>>> ")

    my_cli.send_data(sentence)
    response = my_cli.receive_data()

    print(f"From Server: {response}")

    my_cli.close_connection()




