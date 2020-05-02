import socket
from transport.transport_common import *

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
	
	def sendWithFlags(self, flags, data):
		self.send(b''.join(flags) + data)
		
		if FLAG_READ in flags:
			response = self.read(2)
			response += self.read(100)
			return response
		return None
		
	def stop(self):
		if self.s is not None:
			try:
				self.send(FLAG_CLOSE)
			except:
				pass
			self.s.close()
			self.s = None
		
	def start(self):
		self.stop()
		self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.s.settimeout(5)
		self.s.connect((self.ip, self.port))
		self.send(FLAG_CONNECT)

