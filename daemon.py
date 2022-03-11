#!/usr/bin/env python3
from transport.transport_tcp import TransportTCP
from transport.transport_serial import TransportSerial
from protocol.communicator import Communicator
from protocol.defs.defs2x6.defs2x6 import *
from protocol.wrapper import *
from datetime import datetime
import time
import signal
import json
from json import JSONEncoder
import os
import dataset

def _default(self, obj):
    return getattr(obj.__class__, "__json__", _default.default)(obj)

_default.default = JSONEncoder().default
JSONEncoder.default = _default 

#######################################

STUFF = [sGlobalGroup, sControlGroup, sHC1Group, sDhwGroup, sSolarGroup, sFanGroup, sProgramGroup, sHistoryGroup]

class Logger:
	
	def start(self):
		#trans = TransportTCP("192.168.178.201", 7777)
		trans = TransportSerial("/dev/ttyUSB0", 9600)
		self.comm = Communicator(trans)
		self.comm.start()
		self.w = Wrapper(self.comm)
		self.now = None
		
	def loop(self):
		#filename = time.strftime("%Y.%m.%d_%H:%M:%S.json", time.localtime())
		#with open(f"log/{filename}", "w") as f:
		groups = self.w.getBulkGroups(STUFF)
		for name,group in groups.items():
			print(group)
			
		dbdata = json.loads(json.dumps(groups))
		try:
			now = datetime.now().replace(microsecond=0)
			if self.now is None or self.now.month != now.month:
				self.db = dataset.connect(f"sqlite:///log/status_{now.strftime('%Y_%m')}.db", sqlite_wal_mode=False)
			self.now = now
			self.db.begin()
			for name,group in dbdata.items():
				ins = {}
				ins.update({"timestamp" : self.now})
				ins.update(group)
				self.db[name].insert(ins)
			self.db.commit()
		except Exception as x:
			print(x)
			self.db.rollback()
			#json.dump(groups, f, indent=4)
		
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
