#!/usr/bin/env python3
from transport.transport_tcp import TransportTCP
from protocol.communicator import Communicator
from protocol.defs.defs2xx.defs2xx import *

def main():
	trans = TransportTCP("192.168.178.201", 7777)
	comm = Communicator(trans)
	comm.start()
	requests = [SHistoryGroup, SSolarGroup, SProgramGroup, SFanGroup, SLast10errorsGroup, SControlGroup, SDHWGroup, SHC1Group, SHC2Group, SSystemGroup, SGlobalGroup, PTimedateGroup, SFirmwareGroup]
	commands = [g.command for g in requests]
	response = comm.readRegisterBulk(commands)
	results = list(map(lambda x, y: x(y), requests, response))
	#response = comm.readRegister(PSolarGroup.command)
	for r in results:
		print(r)
	comm.stop()

if __name__== "__main__":
	main() 
