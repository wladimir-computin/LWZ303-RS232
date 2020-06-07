#!/usr/bin/env python3
from transport.transport_tcp import TransportTCP
from transport.transport_serial import TransportSerial
from protocol.communicator import Communicator
from protocol.defs.defs2x6.defs2x6 import *
from protocol.wrapper import *
import time
from datetime import datetime
import signal
import json
from json import JSONEncoder
import os
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from scipy.signal import savgol_filter
import dataset

def _default(self, obj):	
    return getattr(obj.__class__, "__json__", _default.default)(obj)

_default.default = JSONEncoder().default
JSONEncoder.default = _default 

#######################################

#def getNextJson():
#	directory = "log/"
#	for entry in sorted(os.listdir(directory)):
#		if entry.endswith(".json"):
#			with open(directory + entry, "r") as f:
#				yield f
				
#def plot(jsondata, stufftoplot, plotname):
#	y_axis = {}
#	x = [datetime.datetime.strptime(d,"%Y.%m.%d_%H:%M:%S.json") for d in jsondata.keys()]
#
#	for stuff in stufftoplot:
#		y_axis[stuff] = []
#	
#	for v in jsondata.values():
#		for stuff in stufftoplot:
#			y_axis[stuff].append(v[statusToGroup(stuff).name][stuff.name])
#	
#	plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%d.%m.%Y %H:%M'))
#	plt.gca().xaxis.set_major_locator(mdates.HourLocator(byhour = list(range(0,24,3))))
#	
#	# plotting the lines points  
#	for stuff in stufftoplot:
#		try:
#			y_axis[stuff] = savgol_filter(y_axis[stuff], 15, 2)
#		except:
#			pass
#		plt.plot(x, y_axis[stuff], label = f"{stuff.name} ({stuff.unit})")
#		
#	plt.gcf().autofmt_xdate()
#	plt.ylim(bottom=0)
#
#	# naming the x axis 
#	plt.xlabel("Time") 
#	# naming the y axis 
#	plt.ylabel('y - axis') 
#	# giving a title to my graph 
#	plt.title(plotname) 
#
#	# show a legend on the plot 
#	plt.legend() 
#
#	# function to show the plot 
#	plt.show()
	
def plot(table, stufftoplot, plotname):
	db = dataset.connect(f"sqlite:///{table}")
	
	y_axis = {}
	statement = f"SELECT timestamp FROM {sGlobalGroup.name}"
	x = [datetime.strptime(v["timestamp"], '%Y-%m-%d %H:%M:%S.%f') for v in db.query(statement)]

	for stuff in stufftoplot:
		statement = f"SELECT {stuff.name} FROM {statusToGroup(stuff).name}"
		db_data = [v[stuff.name] for v in db.query(statement)]
		y_axis[stuff] = db_data
	
	plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%d.%m.%Y %H:%M'))
	plt.gca().xaxis.set_major_locator(mdates.HourLocator(byhour = list(range(0,24,3))))
	
	# plotting the lines points  
	for stuff in stufftoplot:
		#try:
			#y_axis[stuff] = savgol_filter(y_axis[stuff], 15, 2)
		#except:
			#pass
		plt.plot(x, y_axis[stuff], label = f"{stuff.name} ({stuff.unit})")
		
	plt.gcf().autofmt_xdate()
	plt.ylim(bottom=0)

	# naming the x axis 
	plt.xlabel("Time") 
	# naming the y axis 
	plt.ylabel('y - axis') 
	# giving a title to my graph 
	plt.title(plotname) 

	# show a legend on the plot 
	plt.legend() 

	# function to show the plot 
	plt.show() 

def main():
	#jsons = {}
	#for f in getNextJson():
	#	entry = json.load(f)
	#	jsons[os.path.basename(f.name)] = entry
		
	
	#plot(jsons, [sOutsideTempFiltered, sInsideTemp], "Temperature over time")
	#plot(jsons, [sDhwTemp, sCollectorTemp, sCompressor, sHcOpMode], "DHW")
	#plot(jsons, [sInputVentilatorSpeed, sOutputVentilatorSpeed, sInputVentilatorPower, sOutputVentilatorPower, sCompressor], "Fan speed over time")
	#plot(jsons, [sFlowTemp, sReturnTemp, sDhwTemp, sHeatingCircuitPump], "HC1")
	#plot(jsons, [sCollectorTemp], "TEST")
	
	plot("log/status_2020.db", [sOutsideTempFiltered, sInsideTemp], "Temperature over time")
	plot("log/status_2020.db", [sDhwTemp, sCollectorTemp, sCompressor, sHcOpMode], "DHW")
	plot("log/status_2020.db", [sInputVentilatorSpeed, sOutputVentilatorSpeed, sInputVentilatorPower, sOutputVentilatorPower, sCompressor], "Fan speed over time")
	plot("log/status_2020.db", [sFlowTemp, sReturnTemp, sDhwTemp, sHeatingCircuitPump], "HC1")
	plot("log/status_2020.db", [sCollectorTemp], "TEST")
		

if __name__== "__main__":
	main() 

