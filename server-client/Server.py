from socket import *
from os import listdir

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

def list_files():
	response = listdir()
	return '\n'.join(response)

def get_file(file):
	# with open 
	pass

def get_file_metadata(file):
	pass

def close_socket(name):
	pass


if __name__ == "__main__":
	server_ip = '127.0.0.1'
	server_port = 12000

	query_dict = {
		'LIST': list_files,
		'GET': get_file,
		'METADATA': get_file_metadata,
		'CLOSE': close_socket
	}

	my_server = Server(server_ip, server_port)

	# el servidor debe enviar:
    #  -LIST lista los ficheros en el directorio donde se ejecuta el server
	#		encabezado = resultado de la operacion, tantas lineas como archivos en el dir
    #  -GET <FILE> devuelve el archivo FILE en el directorioa del server
	#		encabezado = resultado de la operacion, el archivo mismo
    #  -METADATA <FILE> devuelve metadata del FILE en el dir del server
	#		encabezado = resultado de la operacion, el archivo mismo
    #  -CLOSE cierra la conexion entre las partes
	#		encabezado = resultado de la operacion, terminar la conexion

	while True:
		sentence = my_server.receive_data().split()
		

		if len(sentence) == 1 and sentence[0] in query_dict:
			response = query_dict[sentence[0]]()
		elif len(sentence) == 2 and sentence[0] in query_dict:
			try:
				response = query_dict[sentence[0]](sentence[1])
			except:
				response = "Error, ilegal arguments"
			
		else:
			response = ' '.join(sentence).upper()
		my_server.send_data(response)
		my_server.close_socket()