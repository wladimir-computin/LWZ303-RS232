#!/usr/bin/env python3
from transport.transport_tcp import TransportTCP
from transport.transport_serial import TransportSerial
from protocol.communicator import Communicator
from protocol.defs.defs2x6.defs2x6 import *
from protocol.wrapper import *
import time
import signal
import json
from json import JSONEncoder
import os

def _default(self, obj):
    return getattr(obj.__class__, "__json__", _default.default)(obj)

_default.default = JSONEncoder().default
JSONEncoder.default = _default 

#######################################

STUFF = [sGlobalGroup, sControlGroup, sHC1Group, sDhwGroup, sSolarGroup, sFanGroup, sProgramGroup, sHistoryGroup]

class Logger:
	
	def start(self):
		trans = TransportTCP("192.168.178.201", 7777)
		#self.trans = TransportSerial("/dev/ttyUSB0", 9600)
		self.comm = Communicator(trans)
		self.comm.start()
		self.w = Wrapper(self.comm)
		
	def loop(self):
		filename = time.strftime("%Y.%m.%d_%H:%M:%S.json", time.localtime())
		with open(f"log/{filename}", "w") as f:
			groups = self.w.getBulkGroups(STUFF)
			for k,v in groups.items():
				print(v)
			json.dump(groups, f, indent=4)
		
	def end(self):
		self.comm.stop()

logger = None

def main():
	signal.signal(signal.SIGINT, handler)
	global logger
	logger = Logger()
	logger.start()
	while True:
		try:
			logger.loop()
			time.sleep(60 - time.localtime().tm_sec)
		except Exception as e:
			print(e)
			time.sleep(5)
			os.system("find ./log/ -type f -empty -delete")
	

	
def handler(signum, frame):
	exit()

def exit():
	global logger
	logger.end()
	quit()

if __name__== "__main__":
	main() 
