#!/usr/bin/env python3
from transport.transport_tcp import TransportTCP
from transport.transport_serial import TransportSerial
from protocol.communicator import Communicator
from protocol.defs.defs2x6.defs2x6 import *
from protocol.wrapper import *
import time
import json
from json import JSONEncoder

def _default(self, obj):
    return getattr(obj.__class__, "__json__", _default.default)(obj)

_default.default = JSONEncoder().default
JSONEncoder.default = _default

#######################################

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
	#status = w.getBulkStatus([sDhwTemp, sFlowTempHC1, sReturnTemp, sHeatingCircuitPump, sHeatRequest, sHcStage, sDhwStage])
	#for k,v in status.items():
		#print(v)

	#print(w.setSingleParameter(p42Fanstage3AirflowOutlet, 170))
	#time.sleep(1)
	groups = w.getBulkGroups(PARAM_GROUPS)
	#groups = w.getBulkGroups(STATUS_GROUPS)
	for k,v in groups.items():
		print(v)
	
	#w.setSingleParameter(p01RoomTempDay, 22.0)
		
	#print(json.dumps(groups, indent=4))
	#print(w.getSingleGroup(sControlGroup))
	
	
	
	comm.stop()

if __name__== "__main__":
	main() 
