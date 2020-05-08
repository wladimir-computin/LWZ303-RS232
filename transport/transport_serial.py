import serial
from transport.transport_common import *

class TransportSerial():
	
	s = None
	device = ""
	baud = 0
			
	MAX_RETRIES = 5
	
	def __init__(self, device, baud):
		self.device = device
		self.baud = baud

	def connect_serial(self):
		if self.s is None:
			print("SERIAL OPEN!")
			self.s = serial.Serial(self.device, baudrate=self.baud, timeout=1)

	def hello_serial(self):
		print("SERIAL HELLO!")
		print("WRITE: 02")
		self.s.write(b"\x02")
		response = self.s.read(1)
		print(f"READ: {response.hex()}\n")
		if response != b"\x10":
			 raise IOError("Error: heat pump does not respond - is it connected?")
		 
	def reset_serial(self):
		print("SERIAL RESET!")
		print("WRITE: 1002")
		self.s.write(DATA_READY)
		response = self.s.read(1)
		print(f"READ: {response.hex()}\n")
		 
	def connected(self):
		if self.s is not None:
			try:
				self.hello_serial()
				return True
			except:
				pass
		return False

	def send(self, data):
		if self.s is not None:
			self.s.write(data)

	def read(self, length):
		if self.s is not None:
			response = self.s.read(length)
			return response
		return bytes()
	
	def sendWithFlags(self, flags, data):
		try:
			flag_open = False
			flag_read = False
			flag_reset = False
			if FLAG_CLOSE in flags:
				self.close_serial()
				return
			if FLAG_CONNECT in flags:
				flag_open = True
				self.close_serial()
				self.connect_serial()
			if FLAG_HELLO in flags:
				self.hello_serial()
			if FLAG_READ in flags:
				flag_read = True
			if FLAG_RESET in flags:
				flag_reset = True

			self.s.write(data)
			response = bytes()
			if if FLAG_READ in flags::
				response = self.s.read(2)
			else:
				response = self.s.read(100)

			if flag_read and response == DATA_READY:
				print("\nWRITE: 10\n")
				self.s.write(b"\x10")
				response += self.s.read_until(FOOTER)
			if flag_reset:
				self.reset_serial()
			print()
			print("----------------------------------------------")
			print()
			return response
		except Exception as x:
			print(x)
		return bytes()
		
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
		self.connect_serial()
