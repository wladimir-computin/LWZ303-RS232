#!/usr/bin/env python3
from transport.transport_tcp import TransportTCP
from protocol.communicator import Communicator

def main():
	trans = TransportTCP("192.168.178.201", 7777)
	comm = Communicator(trans)
	comm.start()
	response = comm.readRegister(b"\xfd")
	if response is not None:
		print(response.hex())
	comm.stop()

if __name__== "__main__":
	main() 
