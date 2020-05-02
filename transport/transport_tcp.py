import socket

class TransportTCP():
	
	s = None
	ip = ""
	port = 0
	
	def __init__(self, ip, port):
		self.ip = ip
		self.port = port

	def send(self, data):
		if self.s is not None:
			self.s.send(data)

	def read(self, length):
		if self.s is not None:
			response = self.s.recv(length)
			return response
		return bytes()
	
	def sendWithHello(self, data):
		self.send(b"HELLO" + data)
	
	def sendWithHelloRead(self, data):
		self.send(b"HELLOREAD" + data)
		response = self.read(2)
		response += self.read(100)
		return response
		
	def stop(self):
		if self.s is not None:
			try:
				self.send(b"CLOSE")
			except:
				pass
			self.s.close()
			self.s = None
		
	def start(self):
		self.stop()
		self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.s.settimeout(5)
		self.s.connect((self.ip, self.port))
		self.send(b"CONNECT")
