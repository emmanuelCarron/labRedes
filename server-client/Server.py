from socket import *

class Server:	
		
	def __init__(self, server_name, server_port):
		self.create_socket(server_name, server_port)


	def create_socket(self, server_name, server_port):
		self.__server_socket = socket(AF_INET, SOCK_STREAM)
		self.__server_socket.bind((server_name, server_port))
		self.__server_socket.listen(1)
		print("The server is ready to receive")


	def receive_data(self):
		self.__conn_socket = self.__server_socket.accept()[0]#tiene que ir aparte?
		return self.__conn_socket.recv(1024).decode()
		
		
	def send_data(self, data):
		self.__conn_socket.send(data.encode())


	def close_socket(self):
		self.__conn_socket.close()


if __name__ == "__main__":
	server_ip = '127.0.0.1'
	server_port = 12000

	my_server = Server(server_ip, server_port)
	while True:
		sentence = my_server.receive_data()
		response = sentence.upper()
		my_server.send_data(response)
		my_server.close_socket()