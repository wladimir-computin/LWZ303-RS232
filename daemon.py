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

def _default(self, obj):
    return getattr(obj.__class__, "__json__", _default.default)(obj)

_default.default = JSONEncoder().default
JSONEncoder.default = _default 

#######################################

STUFF = [sGlobalGroup, sControlGroup, sHC1Group, sDhwGroup, sSolarGroup, sFanGroup, sProgramGroup, sHistoryGroup]


def main():
	signal.signal(signal.SIGINT, handler)
	trans = TransportTCP("192.168.178.201", 7777)
	#trans = TransportSerial("/dev/ttyUSB0", 9600)
	comm = Communicator(trans)
	comm.start()
	w = Wrapper(comm)
	while True:
		try:
			time.sleep(60)
			filename = time.strftime("%Y.%m.%d_%H:%M:%S.json", time.localtime())
			with open(f"log/{filename}", "w") as f:
				groups = w.getBulkGroups(STUFF)
				for k,v in groups.items():
					print(v)
				json.dump(groups, f, indent=4)
		except Exception as e:
			print(e)
	
	comm.stop()
	
def handler(signum, frame):
	exit()

def exit():
	quit()

if __name__== "__main__":
	main() 
