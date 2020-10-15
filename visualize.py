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
	
def plot(db, stufftoplot, plotname, from_date = datetime(2000, 1, 1), to_date = datetime.now()):
	
	statement = f"SELECT timestamp FROM {sGlobalGroup.name} WHERE timestamp BETWEEN DATETIME(:a) AND DATETIME(:b)"
	timestamps = db.query(statement, a=from_date, b=to_date)
	#timestamps = db[sGlobalGroup.name].find(timestamp={'between': [from_date, to_date]})
	x_axis = [datetime.strptime(v["timestamp"], "%Y-%m-%d %H:%M:%S.%f") for v in timestamps]
	
	y_axis = {}
	for stuff in stufftoplot:
		statement = f"SELECT {stuff.name} FROM {statusToGroup(stuff).name} WHERE timestamp BETWEEN DATETIME(:a) AND DATETIME(:b)"
		data = db.query(statement, a=from_date, b=to_date)
		y_axis[stuff] = [v[stuff.name] for v in data]
	
	plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%d.%m.%Y %H:%M'))
	plt.gca().xaxis.set_major_locator(mdates.HourLocator(byhour = list(range(0,24,24))))
	
	# plotting the lines points  
	for stuff in stufftoplot:
	#	try:
	#		y_axis[stuff] = savgol_filter(y_axis[stuff], 15, 2)
	#	except:
	#		pass
		plt.plot(x_axis, y_axis[stuff], label = f"{stuff.name} ({stuff.unit})")
		
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
	
	db_url = f"sqlite:///log/status_{datetime.now().strftime('%Y_%m')}.db"
	#db_url = f"sqlite:///log/status_{datetime.now().strftime('%Y_06')}.db"
	from_date = datetime(2020, 9, 1)
	to_date = datetime.now()
	
	with dataset.connect(db_url) as db:
		plot(db, [sOutsideTempFiltered, sInsideTemp], "Temperature over time", from_date, to_date)
		plot(db, [sDhwTemp, sCollectorTemp, sCompressor, sHcOpMode], "DHW", from_date, to_date)
		plot(db, [sInputFanSpeed, sOutputFanSpeed, sInputFanPower, sOutputFanPower, sCompressor], "Fan speed over time", from_date, to_date)
		plot(db, [sFlowTemp, sReturnTemp, sDhwTemp, sHeatingCircuitPump], "HC1", from_date, to_date)
		plot(db, [sHeatRequest], "sHeatRequest", from_date, to_date)
		

if __name__== "__main__":
	main() 

