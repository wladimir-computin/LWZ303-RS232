from bitstring import ConstBitStream, BitStream, Bits

class InformationObj(object):
	name = ""
	description = ""

	parsemap = {}
	parent = None
	unit = ""
	value = None
	val_min = 0
	val_max = 0
	val_default = 0

	def __init__(self, data=None, value=None):
		self.unparsed = bytes()
		if data is not None:
			start = data.bytepos
			for k,v in self.parsemap.items():
				if isinstance(v, str):
					self.value = data.read(v)
				else:
					self.value = v(data)
			self.rawdata = data.bytes[start:data.bytepos]
		else:
			if value >= self.val_min and value <= self.val_max:
				self.value = value
				self.update()

	def update(self):
		bits = BitStream()
		for k,v in self.parsemap.items():
			if isinstance(v, str):
				bits.append(Bits(f"{v}={self.value}"))
			else:
				bits.append(Bits(bytes=self.value.toBytes()))
		self.rawdata = bits.bytes

	def update_recursive(self):
		for k,v in self.parsemap.items():
			if not isinstance(v, str):
				self.value.update_recursive()
		self.update()
		
	def toBytes(self):
		return self.rawdata

	def __str__(self):
		return f"{self.name}: {self.value}{self.unit}"


class InformationGroup(object):
	name = ""
	description = ""

	parsemap = []
	values = {}

	def __init__(self, rawbytes=None):
		data = ConstBitStream(rawbytes)
		self.unparsed = bytes()
		if data is not None:
			start = data.bytepos
			for p in self.parsemap:
				if isinstance(p, str):
					data.read(p)
				else:
					self.values[p.name] = p(data)
			self.rawdata = data.bytes[start:data.bytepos]

	def update(self):
		bits = BitStream()
		for p in self.parsemap:
			if isinstance(p, str):
				bits.append(Bits(p))
			else:
				bits.append(Bits(bytes=self.values[p.name].toBytes()))
		self.rawdata = bits.bytes
		
	def update_recursive(self):
		for p in self.parsemap:
			if not isinstance(p, str):
				self.values[p.name].update_recursive()
		self.update()
		
	def toBytes(self):
		return self.rawdata
		
	def __str__(self):
		out = ""
		for k,v in self.values.items():
			out += f" {v}\n"
		return f"Name: {self.name}\n{self.description}\n{out}" 


class FixedPOneDec8():
	value = 0

	def __init__(self, data=None, value=None):
		if data is not None:
			start = data.bytepos
			self.value = data.read("int:8") / 10
			self.rawdata = data.bytes[start:data.bytepos]
		else:
			self.value = value
			self.update()
			
	def update(self):
		bits = BitStream()
		bits.append(Bits(f"int:8={self.value*10:d}"))
		self.rawdata = bits.bytes
		
	def update_recursive(self):
		self.update()
		
	def toBytes(self):
		return self.rawdata
		
	def __str__(self):
		return f"{self.value}"
	
	def __float__(self):
		return self.value
	

class FixedPOneDec16():
	value = 0

	def __init__(self, data=None, value=None):
		if data is not None:
			start = data.bytepos
			self.value = data.read("int:16") / 10
			self.rawdata = data.bytes[start:data.bytepos]
		else:
			self.value = value
			self.update()
			
	def update(self):
		bits = BitStream()
		bits.append(Bits(f"int:16={self.value*10:d}"))
		self.rawdata = bits.bytes
		
	def update_recursive(self):
		self.update()
		
	def toBytes(self):
		return self.rawdata
		
	def __str__(self):
		return f"{self.value}"
	
	def __float__(self):
		return self.value
	
	
class FixedPTwoDec16():
	value = 0

	def __init__(self, data=None, value=None):
		if data is not None:
			start = data.bytepos
			self.value = data.read("int:16") / 100
			self.rawdata = data.bytes[start:data.bytepos]
		else:
			self.value = value
			self.update()
			
	def update(self):
		bits = BitStream()
		bits.append(Bits(f"int:16={self.value*100:d}"))
		self.rawdata = bits.bytes
		
	def update_recursive(self):
		self.update()
		
	def toBytes(self):
		return self.rawdata
		
	def __str__(self):
		return f"{self.value}"
	
	def __float__(self):
		return self.value
	
	
class Time16():
	value = 0

	def __init__(self, data=None, value=None):
		if data is not None:
			start = data.bytepos
			val = data.read("uint:16")
			val_s = f"{val:04d}"
			self.value = f"{val_s[0:2]}:{val_s[2:]}"
			self.rawdata = data.bytes[start:data.bytepos]
		else:
			self.value = value
			self.update()
			
	def update(self):
		bits = BitStream()
		vals = self.value.split(":")
		val = vals[0]*100 + vals[1]
		bits.append(Bits(f"uint:16={val:d}"))
		self.rawdata = bits.bytes
		
	def update_recursive(self):
		self.update()
		
	def toBytes(self):
		return self.rawdata
		
	def __str__(self):
		return f"{self.value}"
	
	def __float__(self):
		return self.value
	
	
class Date16():
	value = 0

	def __init__(self, data=None, value=None):
		if data is not None:
			start = data.bytepos
			val = data.read("uint:16")
			val_s = f"{val:04d}"
			self.value = f"{val_s[0:2]}.{val_s[2:]}"
			self.rawdata = data.bytes[start:data.bytepos]
		else:
			self.value = value
			self.update()
			
	def update(self):
		bits = BitStream()
		vals = self.value.split(".")
		val = vals[0]*100 + vals[1]
		bits.append(Bits(f"uint:16={val:d}"))
		self.rawdata = bits.bytes
		
	def update_recursive(self):
		self.update()
		
	def toBytes(self):
		return self.rawdata
		
	def __str__(self):
		return f"{self.value}"
	
	def __float__(self):
		return self.value
	
	
class Error():
	value = 0
	faultmap = { 0 : "n.a.",
			 1 : "F01_AnodeFault",
			 2 : "F02_SafetyTempDelimiterEngaged",
			 3 : "F03_HighPreasureGuardFault",
			 4 : "F04_LowPreasureGuardFault",
			 5 : "F05_OutletFanFault",
			 6 : "F06_InletFanFault",
			 7 : "F07_MainOutputFanFault",
			 11 : "F11_LowPreasureSensorFault",
			 12 : "F12_HighPreasureSensorFault",
			 15 : "F15_DHW_TemperatureFault",
			 17 : "F17_DefrostingDurationExceeded",
			 20 : "F20_SolarSensorFault",
			 21 : "F21_OutsideTemperatureSensorFault",
			 22 : "F22_HotGasTemperatureFault",
			 23 : "F23_CondenserTemperatureSensorFault",
			 24 : "F24_EvaporatorTemperatureSensorFault",
			 26 : "F26_ReturnTemperatureSensorFault",
			 28 : "F28_FlowTemperatureSensorFault",
			 29 : "F29_DHW_TemperatureSensorFault",
			 30 : "F30_SoftwareVersionFault",
			 31 : "F31_RAMfault",
			 32 : "F32_EEPromFault",
			 33 : "F33_ExtractAirHumiditySensor",
			 34 : "F34_FlowSensor",
			 35 : "F35_minFlowCooling",
			 36 : "F36_MinFlowRate",
			 37 : "F37_MinWaterPressure",
			 40 : "F40_FloatSwitch",
			 50 : "F50_SensorHeatPumpReturn",
			 51 : "F51_SensorHeatPumpFlow",
			 52 : "F52_SensorCondenserOutlet",
			 86 : "F86_Unknown"}


	def __init__(self, data=None, value=None):
		if data is not None:
			start = data.bytepos
			val = data.read("uint:8")
			self.value = self.faultmap[val]
			self.rawdata = data.bytes[start:data.bytepos]
		else:
			self.value = value
			self.update()
			
	def update(self):
		bits = BitStream()
		val = self.faultmap.items()[self.value]
		bits.append(Bits(f"uint:16={val:d}"))
		self.rawdata = bits.bytes
		
	def update_recursive(self):
		self.update()
		
	def toBytes(self):
		return self.rawdata
		
	def __str__(self):
		return f"{self.value}"
	
	def __float__(self):
		return self.value
