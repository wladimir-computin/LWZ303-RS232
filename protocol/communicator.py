from transport.transport_common import *

DATA_READY = b"\x10\x02"
HEADER_OK = b"\x01\x00"
HEADER_READ = b"\x01\x00"
HEADER_WRITE = b"\x01\x80"
FOOTER = b"\x10\x03"

class Communicator:
	
	transport = None
	
	def __init__(self, transport):
		self.transport = transport
		
	def start(self):
		self.transport.start()
	
	def stop(self):
		self.transport.stop()
		
	def checksum(self, data):
		checksum = 1
		for i in range(0, len(data)):
			checksum += int(data[i])
			checksum &= 0xFF
		return bytes([checksum])
	
	def verifyRequest(self, request, response):
		try:
			if request[len(HEADER_READ) + 1] == response[1]:
				print(" response matches request")
				return True
		except:
			pass
		return False
	
	def verifyChecksum(self, response):
		try:
			if self.checksum(response[1:]) == bytes([response[0]]):
				print(" checksum ok")
				return True
		except:
			pass
		return False
		
	def prepareReadRequest(self, reg):
		request = self.checksum(reg) + reg
		request = request.replace(b"\x10", b"\x10\x10")
		request = request.replace(b"\x2b", b"\x2b\x18")
		request = HEADER_READ + request + FOOTER
		return request
		
	def prepareResponse(self, response):
		response = response[len(DATA_READY + HEADER_OK):]
		response = response[:-len(FOOTER)]
		response = response.replace(b"\x10\10", b"\x10")
		response = response.replace(b"\x2b\x18", b"\x2b")
		return response
		
	def readRegister(self, reg, flags=[FLAG_HELLO, FLAG_READ]):
		
		request = self.prepareReadRequest(reg)
		print(f"Sending: {request.hex()}")
		
		if self.transport is not None:
			response = self.transport.sendWithFlags(flags, request)
			
			if response.startswith(DATA_READY + HEADER_OK) and response.endswith(FOOTER):
				
				response = self.prepareResponse(response)
				
				if(self.verifyRequest(request, response)):
					if(self.verifyChecksum(response)):
						response = response[2:]
						print(f"Response: {response.hex()}")
						return response
		return None

	
	def readRegisterBulk(self, regs):
		responses = []
		responses.append(self.readRegister(regs[0], [FLAG_HELLO, FLAG_READ, FLAG_RESET]))
		for reg in regs[1:]:
			responses.append(self.readRegister(reg, [FLAG_READ, FLAG_RESET]))
		
		return responses
			
				
	def writeRegister(self, reg, val):
		pass
