#!/usr/bin/env python3
from transport.transport_tcp import TransportTCP
from transport.transport_serial import TransportSerial
from protocol.communicator import Communicator
from protocol.defs.defs2x6.defs2x6 import *

status_requests = [sHistoryGroup, sSolarGroup, sProgramGroup, sFanGroup, sControlGroup, sDhwGroup, sHC1Group, sHC2Group, sSystemGroup, sGlobalGroup, sFirmwareGroup, sSystemGroup, sLast10ErrorsGroup]
parameter_requests = []#[pSolarGroup, pP01P12Group, pHeat1Group, pHeat2Group, pDHWGroup, pFanGroup, pRestartGroup, pDryHeatGroup, pDefrostEvaGroup, pDefrostAAGroup, pCircPumpGroup, sProgramGroup, pHeatProgGroup, pDHWProgGroup, pFanProgGroup, pTimedateGroup]

def main():
	#trans = TransportTCP("192.168.178.201", 7777)
	trans = TransportSerial("/dev/ttyUSB0", 9600)
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
