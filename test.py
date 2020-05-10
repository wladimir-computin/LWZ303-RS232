#!/usr/bin/env python3
from transport.transport_tcp import TransportTCP
from transport.transport_serial import TransportSerial
from protocol.communicator import Communicator
from protocol.defs.defs2x6.defs2x6 import *
import json
import time

status_requests = []#[sHistoryGroup, sSolarGroup, sProgramGroup, sFanGroup, sControlGroup, sDhwGroup, sHC1Group, sHC2Group, sSystemGroup, sGlobalGroup, sFirmwareGroup, sSystemGroup, sLast10ErrorsGroup]
parameter_requests = [pSolarGroup, pP01P12Group, pHeat1Group, pHeat2Group, pDHWGroup, pFanGroup, pRestartGroup, pDryHeatGroup, pDefrostEvaGroup, pDefrostAAGroup, pCircPumpGroup, sProgramGroup, pHeatProgGroup, pDHWProgGroup, pFanProgGroup, pTimedateGroup]

def selftest_update(comm):
	requests = parameter_requests
	commands = [g.command for g in requests]
	response = comm.readRegisterBulk(commands)
	results = list(map(lambda x, y: x(y), requests, response))
	for r in results:
		orig = r.toBytes()
		r.update_recursive()
		new = r.toBytes()
		if(orig != new):
			print(f"\nERROR: Following class is defective:\n {r}")
			print(f"BEFORE: {orig.hex()}")
			print(f" AFTER: {new.hex()}")
			return False
	return True

def backup_all_paramters(comm):
	requests = parameter_requests
	commands = [g.command for g in requests]
	response = comm.readRegisterBulk(commands)
	results = list(map(lambda x, y: x(y), requests, response))
	backup = []
	for r in results:
		values = {}
		for k,v in r.values.items():
			try:
				values[k] = str(v.value)
			except:
				values[k] = str(v)
		backup.append({"raw":r.toBytes().hex(), "values": values})
	with open("backup.json", 'w') as outfile:
		print(json.dump(backup, outfile, indent=4, sort_keys=True))
			

def main():
	trans = TransportTCP("192.168.178.201", 7777)
	#trans = TransportSerial("/dev/ttyUSB0", 9600)
	comm = Communicator(trans)
	comm.start()

	#selftest_write(comm)
	#backup_all_paramters(comm)
	p01p12 = pP01P12Group(comm.readRegister(pP01P12Group.command))
	print(p01p12)
	p01 = p01p12.values["p01RoomTempDay"]
	p01.value.value = 22
	p01p12.update_recursive()
	time.sleep(5)
	#comm.writeRegister(pP01P12Group.command, p01p12.toBytes())
	
	
		
	comm.stop()

if __name__== "__main__":
	main() 
