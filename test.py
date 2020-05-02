#!/usr/bin/env python3
from transport.transport_tcp import TransportTCP
from protocol.communicator import Communicator
from protocol.defs.defs2xx import *

def main():
	trans = TransportTCP("192.168.178.201", 7777)
	comm = Communicator(trans)
	comm.start()
	response = comm.readRegisterBulk([PSolarGroup.command, SSolarGroup.command])
	#response = comm.readRegister(PSolarGroup.command)
	print(PSolarGroup(response[0]))
	print(SSolarGroup(response[1]))
	comm.stop()

if __name__== "__main__":
	main() 
