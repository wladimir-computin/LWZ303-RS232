#!/usr/bin/env python3
from transport.transport_tcp import TransportTCP
from protocol.communicator import Communicator
from protocol.defs.defs2x6.defs2x6 import *

parameter_requests = [sHistoryGroup, sSolarGroup, sProgramGroup, sFanGroup, sControlGroup, sDHWGroup, sHC1Group, sHC2Group, sSystemGroup, sGlobalGroup, pTimedateGroup, sFirmwareGroup, sSystemGroup, sLast10ErrorsGroup]
status_requests = [pSolarGroup, pP01P12Group, pHeat1Group, pHeat2Group, pDHWGroup, pRestartGroup, pDryHeatGroup, pDefrostEvaGroup, pDefrostAAGroup, sHistoryGroup, pCircPumpGroup]

def main():
	trans = TransportTCP("192.168.178.201", 7777)
	comm = Communicator(trans)
	comm.start()
	requests = parameter_requests + status_requests
	commands = [g.command for g in requests]
	response = comm.readRegisterBulk(commands)
	results = list(map(lambda x, y: x(y), requests, response))
	#response = comm.readRegister(PSolarGroup.command)
	for r in results:
		print(r)
	comm.stop()

if __name__== "__main__":
	main() 
