from transport.transport_common import *

DATA_READY = b"\x10\x02"
HEADER_OK = b"\x01\x00"
HEADER_READ = b"\x01\x00"
HEADER_WRITE = b"\x01\x80"
FOOTER = b"\x10\x03"

class Communicator:
	
	transport = None
	MAX_RETRYS = 2
	
	def __init__(self, transport):
		self.transport = transport
		
	def start(self):
		self.transport.start()
	
	def stop(self):
		self.transport.stop()
		
	def checksum(self, data):
		checksum = 1
		for b in data:
			checksum += b
			checksum &= 0xFF
		return bytes([checksum])
	
	def verifyRequest(self, request, response):
		try:
			id_request = request[len(HEADER_READ) + 1]
			id_response = response[1]
			if id_request == id_response:
				return True
			else:
				print(f" request error: {id_request.hex()}!={id_response.hex()}")
				return False
		except:
			pass
		print(f" request error!")
		return False
	
	def verifyChecksum(self, response):
		try:
			chk_calc = self.checksum(response[1:])
			chk_response = bytes([response[0]])
			if chk_calc == chk_response:
				return True
			else:
				print(f" checksum error: {chk_calc.hex()}!={chk_response.hex()}")
				return False
		except:
			pass
		print(f" checksum error!")
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
		response = response.replace(b"\x10\x10", b"\x10")
		response = response.replace(b"\x2b\x18", b"\x2b")
		return response
		
	def readRegister(self, reg, flags=[FLAG_HELLO, FLAG_READ]):
		try:
			request = self.prepareReadRequest(reg)
			print(f"Sending: {request.hex()}")
			
			if self.transport is not None:
				tried = 0
				while tried < self.MAX_RETRYS:
					tried += 1
					response = self.transport.sendWithFlags(flags, request)
					
					if response.startswith(DATA_READY + HEADER_OK) and response.endswith(FOOTER):
						
						response = self.prepareResponse(response)
						print(f"Response: {response.hex()}")
						if(self.verifyRequest(request, response)):
							if(self.verifyChecksum(response)):
								response = response[2:]
								return response
				return b""
		except Exception as x:
			print(x)
		return None

	
	def readRegisterBulk(self, regs):
		responses = []
		responses.append(self.readRegister(regs[0], [FLAG_HELLO, FLAG_READ, FLAG_RESET]))
		for reg in regs[1:]:
			success = False
			resp = self.readRegister(reg, [FLAG_READ, FLAG_RESET])
			if resp is None:
				self.transport.sendWithFlags([FLAG_CONNECT], b"")
				resp = self.readRegister(reg, [FLAG_HELLO, FLAG_READ, FLAG_RESET])
			responses.append(resp)
		return responses
			
				
	def writeRegister(self, reg, val):
		pass
