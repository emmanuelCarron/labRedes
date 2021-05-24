from socket import *

class Server:
		
	def __init__(self, s_ip, s_port) -> None:
		self.ip = s_ip
		self.port = s_port


	def create_socket(self) -> None:
		self.server_socket = socket(AF_INET, SOCK_STREAM)
		self.server_socket.bind((self.ip, self.port))
		self.server_socket.listen(1)


	def receive_data(self) -> str:
		self.conn_socket = self.server_socket.accept()[0]



	def send_data(self) -> None:
		pass


	def close_soclet(self) -> None:
		pass



if __name__ == "__main__":
	pass