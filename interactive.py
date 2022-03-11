#!/usr/bin/env python3
from transport.transport_tcp import TransportTCP
from transport.transport_serial import TransportSerial
from protocol.communicator import Communicator
from protocol.defs.defs2x6.defs2x6 import *
from protocol.wrapper import *
import time
import json
from json import JSONEncoder
from cmd import Cmd
import sys
import signal
from datetime import datetime
import dataset
from visualize import *
import re

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

class MyPrompt(Cmd):
	
	def __init__(self, wrapper):
		self.wrapper = wrapper;
		self.prompt = f"LWZ-># "
		super().__init__()
		
	def emptyline(self):
		pass
		
	def do_exit(self, inp):
		return True
	
	def do_getparam(self, arg):
		try:
			param = None
			for p in ALL_PARAMS:
				if p.name == arg:
					param = p
			print(self.wrapper.getSingleParameter(param))
		except Exception as x:
			print(x)
	
	def complete_getparam(self, text, line, begidx, endidx):
		return [i.name for i in ALL_PARAMS if i.name.lower().startswith(text.lower())]
	
	def do_getstatus(self, arg):
		try:
			status = None
			for p in ALL_STATUS:
				if p.name == arg:
					status = p
			print(self.wrapper.getSingleStatus(status))
		except Exception as x:
			print(x)
	
	def complete_getstatus(self, text, line, begidx, endidx):
		return [i.name for i in ALL_STATUS if i.name.lower().startswith(text.lower())]
	
	def do_getgroup(self, arg):
		try:
			group = None
			for p in STATUS_GROUPS + PARAM_GROUPS:
				if p.name == arg:
					group = p
			print(self.wrapper.getSingleGroup(group))
		except Exception as x:
			print(x)
	
	def complete_getgroup(self, text, line, begidx, endidx):
		return [i.name for i in STATUS_GROUPS if i.name.lower().startswith(text.lower())] + [i.name for i in PARAM_GROUPS if i.name.lower().startswith(text.lower())]
	
	def do_setparam(self, arg):
		try:
			args = arg.split(" ")
			
			param = None
			for p in ALL_PARAMS:
				if p.name == args[0]:
					param = p
			print(self.wrapper.setSingleParameter(param, float(args[1])))
		except Exception as x:
			print(x)
	
	def complete_setparam(self, text, line, begidx, endidx):
		return [i.name for i in ALL_PARAMS if i.name.lower().startswith(text.lower())]
	
	def do_params(self, arg):
		try:
			results = self.wrapper.getBulkGroups(PARAM_GROUPS)
			for k,v in results.items():
				print(v)
		except Exception as x:
			print(x)
			
	def do_status(self, arg):
		try:
			results = self.wrapper.getBulkGroups(STATUS_GROUPS)
			for k,v in results.items():
				print(v)
		except Exception as x:
			print(x)
	
	def do_plot(self, arg):
		try:
			status = []
			now = datetime.now().strftime('%Y_%m')
			for a in arg.split(" "):
				for p in ALL_STATUS:
					if p.name == a:
						status.append(p)
						break
					else:
						if re.match(r"\d\d\d\d_\d\d", a):
							now = a
			db_url = f"sqlite:///log/status_{now}.db"
			with dataset.connect(db_url) as db:
				plot(db, status, "Plot")
		except Exception as x:
			print(x)
			
	def complete_plot(self, text, line, begidx, endidx):
		return [i.name for i in ALL_STATUS if i.name.lower().startswith(text.lower())]
	
	def do_selftest(self, arg):
		selftest_write(self.wrapper.comm)

	def default(self, inp):
		pass

def exit():
	print()
	quit()

def handler(signum, frame):
	exit()

def main():
	signal.signal(signal.SIGINT, handler)
	trans = TransportTCP("192.168.178.201", 7777)
	#trans = TransportSerial("/dev/ttyUSB0", 9600)
	comm = Communicator(trans)
	comm.start()
	w = Wrapper(comm)
	#ip, port = sys.argv[1].split(":")
	#password = sys.argv[2]
	#payload = sys.argv[3]
	
	interactive = True#(payload == "i")

	#transport = Transport_TCP(ip, int(port))
	#transport = Transport_UDP(ip, int(port))
	#cc = CryptCon(transport, password)

	if interactive:
		prompt = MyPrompt(w)
		prompt.cmdloop()
		comm.stop();

	else:
		print(cc.send(payload));
		exit()

if __name__== "__main__":
	main()
