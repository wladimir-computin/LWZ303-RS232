#!/usr/bin/env python3
from transport.transport_tcp import TransportTCP
from transport.transport_serial import TransportSerial
from protocol.communicator import Communicator
from protocol.defs.defs2x6.defs2x6 import *
from protocol.wrapper import *
import json
import time

status_requests = [sHistoryGroup, sSolarGroup, sProgramGroup, sFanGroup, sControlGroup, sDhwGroup, sHC1Group, sHC2Group, sSystemGroup, sGlobalGroup, sFirmwareGroup, sSystemGroup, sLast10ErrorsGroup]
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
		
def selftest_write(comm):
	p01p12 = pP01P12Group(comm.readRegister(pP01P12Group.command))
	print("\nRead Values:\n")
	print(p01p12)
	p01 = p01p12.values["p01RoomTempDay"]
	p01_backup = p01.value.value
	p01.value.value = 19
	p01p12.update_recursive()
	time.sleep(5)
	new = comm.writeRegister(pP01P12Group.command, p01p12.toBytes())
	if new is not None:
		p01p12 = pP01P12Group(new)
		print("\nNew Values:\n")
		print(p01p12)
		p01 = p01p12.values["p01RoomTempDay"]
		if p01.value.value == 19:
			p01 = p01p12.values["p01RoomTempDay"]
			p01.value.value = p01_backup
			p01p12.update_recursive()
			print(f"\nWrite successful, restoring old value: {p01_backup}\n")
			time.sleep(5)
			new2 = comm.writeRegister(pP01P12Group.command, p01p12.toBytes())
			if new2 is not None:
				p01p12 = pP01P12Group(new2)
				print("\nRestored Values:\n")
				print(p01p12)
				p01 = p01p12.values["p01RoomTempDay"]
				if p01.value.value == p01_backup:
					print("\nOld Value restored, write works as expected!\n")
					return True
	return False
				
			
			
		
def printRequests(comm, requests):
	requests = requests
	commands = [g.command for g in requests]
	response = comm.readRegisterBulk(commands)
	results = list(map(lambda x, y: x(y), requests, response))
	for r in results:
		print(r)
		
def printStatus(comm):
	printRequests(comm, status_requests)
		
def printParameters(comm):
	printRequests(comm, parameter_requests)
	
def printSingleParameter(comm, param):
	group = paramToGroup(param)
	value = group(comm.readRegister(group.command)).values[param.name]
	print(value)
			

def main():
	trans = TransportTCP("192.168.178.201", 7777)
	#trans = TransportSerial("/dev/ttyUSB0", 9600)
	comm = Communicator(trans)
	comm.start()
	w = Wrapper(comm)
	#printStatus(comm)
	#printRequests(comm, status_requests + parameter_requests)
	#backup_all_paramters(comm)
	#selftest_write(comm)
	#print(w.getSingleParameter(p01RoomTempDay))
	status = w.getBulkStatus([sDhwTemp, sFlowTempHC1, sReturnTemp, sHeatingCircuitPump, sHeatRequest, sHcStage, sDhwStage])
	for s in status:
		print(s)
	
	
		
	comm.stop()

if __name__== "__main__":
	main() 
