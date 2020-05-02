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
				bits.append(Bits(f"{v}={self.values[k]}"))
			else:
				bits.append(Bits(bytes=self.values[k].toBytes()))
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
	
	
class p80EnableSolar(InformationObj):
	name = "p80EnableSolar"
	description = ""
	parsemap = {"val":"uint:8"}
	
class p81DiffTempSolarLoading(InformationObj):
	name = "p81DiffTempSolarLoading"
	description = ""
	parsemap = {"val":"uint:16"}
	unit = "K"
	
class p82DelayCompStartSolar(InformationObj):
	name = "p82DelayCompStartSolar"
	description = ""
	parsemap = {"val":"uint:8"}
	
class p84DHWTempSolarMode(InformationObj):
	name = "p84DHWTempSolarMode"
	description = ""
	parsemap = {"val":"uint:16"}
	
class HystDiffTempSolar(InformationObj):
	name = "HystDiffTempSolar"
	description = ""
	parsemap = {"val":"uint:16"}
	unit = "K"
	
class CollectLimitTempSolar(InformationObj):
	name = "CollectLimitTempSolar"
	description = ""
	parsemap = {"val":"uint:16"}
	unit = "°C"

class PSolarGroup(InformationGroup):
	name = "P_SolarGroup"
	description = "Solar related parameters"
	command = b"\x08"
	values = {}
	
	parsemap = [p80EnableSolar, p81DiffTempSolarLoading, p82DelayCompStartSolar, p84DHWTempSolarMode, HystDiffTempSolar, CollectLimitTempSolar]
	
class collectorTemp(InformationObj):
	name = "collectorTemp"
	description = ""
	parsemap = {"val":"int:16"}
	unit = "°C"

class dhwTemp(InformationObj):
	name = "dhwTemp"
	description = ""
	parsemap = {"val":"int:16"}
	unit = "°C"
	
class flowTemp(InformationObj):
	name = "flowTemp"
	description = ""
	parsemap = {"val":"int:16"}
	unit = "°C"
	
class edSolPump(InformationObj):
	name = "edSolPump"
	description = ""
	parsemap = {"val":"int:8"}
	unit = "°C"

class SSolarGroup(InformationGroup):
	name = "S_SolarGroup"
	description = "Solar status"
	command = b"\x16"
	parsemap = [collectorTemp, dhwTemp, flowTemp, edSolPump]
	values = {}
	

	
'''
"pDefrostEva"			=> {cmd2=>"03", type =>"03pxx206", unit =>""},
"pDefrostAA"			=> {cmd2=>"04", type =>"04pxx206", unit =>""},
"pHeat1"			    => {cmd2=>"05", type =>"05pxx206", unit =>""},
"pHeat2"			    => {cmd2=>"06", type =>"06pxx206", unit =>""},
"pDHW"			    => {cmd2=>"07", type =>"07pxx206", unit =>""},
"pSolar"			    => {cmd2=>"08", type =>"08pxx206", unit =>""},
"sHistory"			=> {cmd2=>"09", type =>"09his206", unit =>""},
"pCircPump"			=> {cmd2=>"0A", type =>"0Apxx206", unit =>""},
"pHeatProg"			=> {cmd2=>"0B", type =>"0Bpxx206", unit =>""},
"pDHWProg"			=> {cmd2=>"0C", type =>"0Cpxx206", unit =>""},
"pFanProg"   			=> {cmd2=>"0D", type =>"0Dpxx206", unit =>""},
"pRestart"			=> {cmd2=>"0E", type =>"0Epxx206", unit =>""},
"pAbsence"			=> {cmd2=>"0F", type =>"0Fpxx206", unit =>""},
"pDryHeat"			=> {cmd2=>"10", type =>"10pxx206", unit =>""},
"sSol"			    => {cmd2=>"16", type =>"16sol",    unit =>""},
"p01-p12"			    => {cmd2=>"17", type =>"17pxx206", unit =>""},
"sProgram"  			=> {cmd2=>"EE", type =>"EEprg206", unit =>""},
"sFan"  				=> {cmd2=>"E8", type =>"E8fan206", unit =>""},
"sControl"  			=> {cmd2=>"F2", type =>"F2ctrl",   unit =>""},
"sDHW"			    => {cmd2=>"F3", type =>"F3dhw",    unit =>""},
"sHC2"			    => {cmd2=>"F5", type =>"F5hc2",    unit =>""},
"sSystem"			    => {cmd2=>"F6", type =>"F6sys206", unit =>""},
"sTimedate" 			=> {cmd2=>"FC", type =>"FCtime206", unit =>""},
"inputVentilatorSpeed"=> {parent=>"sGlobal",              unit =>" %"},
"outputVentilatorSpeed"=>{parent=>"sGlobal",              unit =>" %"},
"mainVentilatorSpeed"	=> {parent=>"sGlobal",              unit =>" %"},
"inputVentilatorPower"=> {parent=>"sGlobal",              unit =>" %"},
"outputVentilatorPower"=>{parent=>"sGlobal",              unit =>" %"},
"mainVentilatorPower"	=> {parent=>"sGlobal",              unit =>" %"},  
'''
