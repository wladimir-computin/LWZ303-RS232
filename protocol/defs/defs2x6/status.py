from protocol.defs.defs import *

class HystDiffTempSolar(InformationObj):
	name = "HystDiffTempSolar"
	description = ""
	parsemap = {"val":FixedPOneDec16}
	unit = "K"
	
class CollectLimitTempSolar(InformationObj):
	name = "CollectLimitTempSolar"
	description = ""
	parsemap = {"val":FixedPOneDec16}
	unit = "°C"
	
class sCollectorTemp(InformationObj):
	name = "sCollectorTemp"
	description = ""
	parsemap = {"val":FixedPOneDec16}
	unit = "°C"
	
class sDhwTemp(InformationObj):
	name = "sDhwTemp"
	description = ""
	parsemap = {"val":FixedPOneDec16}
	unit = "°C"
	
class sDhwTargetTemp(InformationObj):
	name = "sDhwTargetTemp"
	description = ""
	parsemap = {"val":FixedPOneDec16}
	unit = "°C"
	
class sFlowTemp(InformationObj):
	name = "sFlowTemp"
	description = ""
	parsemap = {"val":FixedPOneDec16}
	unit = "°C"
	
class sEdSolPump(InformationObj):
	name = "sEdSolPump"
	description = ""
	parsemap = {"val":"uint:8"}
	unit = "%"
	
class sHeatBlockTime(InformationObj):
	name = "sHeatBlockTime"
	description = ""
	parsemap = {"val":"uint:16"}
	
class sDhwBoosterStage(InformationObj):
	name = "sDhwBoosterStage"
	description = ""
	parsemap = {"val":"uint:8"}
	
class sPasteurisationMode(InformationObj):
	name = "sPasteurisationMode"
	description = ""
	parsemap = {"val":"uint:8"}

class sDhwOpMode(InformationObj):
	name = "sDhwOpMode"
	description = ""
	parsemap = {"val":OperationModeHC}
	
class sAutoFanCalib(InformationObj):
	name = "sAutoFanCalib"
	description = ""
	parsemap = {"val":"uint:8"}
	unit = ""
	
class sInputFanSpeedCal(InformationObj):
	name = "sInputFanSpeedCal"
	description = ""
	parsemap = {"val":"uint:16"}
	unit = ""	

class sOutputFanSpeedCal(InformationObj):
	name = "sOutputFanSpeedCal"
	description = ""
	parsemap = {"val":"uint:16"}
	unit = ""
	
class sInputFanAirflowCal(InformationObj):
	name = "sInputFanAirflowCal"
	description = ""
	parsemap = {"val":"uint:16"}
	unit = "m3/h"	

class sOutputFanAirflowCal(InformationObj):
	name = "sOutputFanAirflowCal"
	description = ""
	parsemap = {"val":"uint:8"}
	unit = "m3/h"
	
class sInputFanSpeed(InformationObj):
	name = "sInputFanSpeed"
	description = ""
	parsemap = {"val":"uint:8"}
	unit = "rps"	

class sOutputFanSpeed(InformationObj):
	name = "sOutputFanSpeed"
	description = ""
	parsemap = {"val":"uint:8"}
	unit = "rps"
	
class sInputFanAirflowSet(InformationObj):
	name = "sInputFanAirflowSet"
	description = ""
	parsemap = {"val":"uint:16"}
	unit = "m3/h"	

class sOutputFanAirflowSet(InformationObj):
	name = "sOutputFanAirflowSet"
	description = ""
	parsemap = {"val":"uint:16"}
	unit = "m3/h"
	
class sInputFanSpeedTarget(InformationObj):
	name = "sInputFanSpeedTarget"
	description = ""
	parsemap = {"val":"uint:8"}
	unit = "%"

class sOutputFanSpeedTarget(InformationObj):
	name = "sOutputFanSpeedTarget"
	description = ""
	parsemap = {"val":"uint:8"}
	unit = "%"
	
class sInputFanSpeed0(InformationObj):
	name = "sInputFanSpeed0"
	description = ""
	parsemap = {"val":"uint:16"}
	unit = "rps"	

class sOutputFanSpeed0(InformationObj):
	name = "sOutputFanSpeed0"
	description = ""
	parsemap = {"val":"uint:16"}
	unit = "rps"
	
class sInputFanSpeed200(InformationObj):
	name = "sInputFanSpeed200"
	description = ""
	parsemap = {"val":"uint:16"}
	unit = "rps"	

class sOutputFanSpeed200(InformationObj):
	name = "sOutputFanSpeed200"
	description = ""
	parsemap = {"val":"uint:16"}
	unit = "rps"
	
class sAirflowTolerance(InformationObj):
	name = "sAirflowTolerance"
	description = ""
	parsemap = {"val":"uint:8"}
	unit = ""
	
class sAirflowCalibrationInterval(InformationObj):
	name = "sAirflowCalibrationInterval"
	description = ""
	parsemap = {"val":"uint:8"}
	unit = ""	

class sTimeToCalibration(InformationObj):
	name = "sTimeToCalibration"
	description = ""
	parsemap = {"val":"uint:8"}
	unit = ""
	
class sOutsideTemp(InformationObj):
	name = "sOutsideTemp"
	description = ""
	parsemap = {"val":FixedPOneDec16}
	unit = "°C"
	
class sCompBlockTimeTemp(InformationObj):
	name = "sCompBlockTimeTemp"
	description = ""
	parsemap = {"val":FixedPOneDec16}
	unit = ""
	
class sOperatingHours1(InformationObj):
	name = "sOperatingHours1"
	description = ""
	parsemap = {"val":"uint:16"}
	unit = ""
	
class sOperatingHours2(InformationObj):
	name = "sOperatingHours2"
	description = ""
	parsemap = {"val":"uint:16"}
	unit = ""
	
class sHeatingHours(InformationObj):
	name = "sHeatingHours"
	description = ""
	parsemap = {"val":"uint:16"}
	unit = ""
	
class sDhwHours(InformationObj):
	name = "sDhwHours"
	description = ""
	parsemap = {"val":"uint:16"}
	unit = ""
	
class sCoolingHours(InformationObj):
	name = "sCoolingHours"
	description = ""
	parsemap = {"val":"uint:16"}
	unit = ""

class sFlowTempHC1(InformationObj):
	name = "sFlowTempHC1"
	description = ""
	parsemap = {"val":FixedPOneDec16}
	unit = "°C"
	
class sReturnTemp(InformationObj):
	name = "sReturnTemp"
	description = ""
	parsemap = {"val":FixedPOneDec16}
	unit = "°C"
	
class sOHotGasTemp(InformationObj):
	name = "sOHotGasTemp"
	description = ""
	parsemap = {"val":FixedPOneDec16}
	unit = "°C"

class sFlowTempHC2(InformationObj):
	name = "sFlowTempHC2"
	description = ""
	parsemap = {"val":FixedPOneDec16}
	unit = "°C"
	
class sInsideTemp(InformationObj):
	name = "sInsideTemp"
	description = ""
	parsemap = {"val":FixedPOneDec16}
	unit = "°C"
	
class sEvaporatorTemp(InformationObj):
	name = "sEvaporatorTemp"
	description = ""
	parsemap = {"val":FixedPOneDec16}
	unit = "°C"
	
class sCondensorTemp(InformationObj):
	name = "sCondensorTemp"
	description = ""
	parsemap = {"val":FixedPOneDec16}
	unit = "°C"
	
class sBoosterStage3(InformationObj):
	name = "sBoosterStage3"
	description = ""
	parsemap = {"val":"bool"}
	
class sBoosterStage2(InformationObj):
	name = "sBoosterStage2"
	description = ""
	parsemap = {"val":"bool"}
	
class sBoosterStage1(InformationObj):
	name = "sBoosterStage1"
	description = ""
	parsemap = {"val":"bool"}
	
class sCompressor(InformationObj):
	name = "sCompressor"
	description = ""
	parsemap = {"val":"bool"}
	
class sHeatPipeValve(InformationObj):
	name = "sHeatPipeValve"
	description = ""
	parsemap = {"val":"bool"}
	
class sDiverterValve(InformationObj):
	name = "sDiverterValve"
	description = ""
	parsemap = {"val":"bool"}
	
class sDhwPump(InformationObj):
	name = "sDhwPump"
	description = ""
	parsemap = {"val":"bool"}
	
class sHeatingCircuitPump(InformationObj):
	name = "sHeatingCircuitPump"
	description = ""
	parsemap = {"val":"bool"}
	
class sMixerClosed(InformationObj):
	name = "sMixerClosed"
	description = ""
	parsemap = {"val":"bool"}
	
class sMixerOpen(InformationObj):
	name = "sMixerOpen"
	description = ""
	parsemap = {"val":"bool"}
	
class sOutputVentilatorPower(InformationObj):
	name = "sOutputVentilatorPower"
	description = ""
	parsemap = {"val":"uint:8"}
	unit = "%"

class sInputVentilatorPower(InformationObj):
	name = "sInputVentilatorPower"
	description = ""
	parsemap = {"val":"uint:8"}
	unit = "%"

class sMainVentilatorPower(InformationObj):
	name = "sMainVentilatorPower"
	description = ""
	parsemap = {"val":"uint:8"}
	unit = "%"

class sLowPressureSensor(InformationObj):
	name = "sLowPressureSensor"
	description = ""
	parsemap = {"val":"bool"}

class sHighPressureSensor(InformationObj):
	name = "sHighPressureSensor"
	description = ""
	parsemap = {"val":"bool"}

class sSignalAnode(InformationObj):
	name = "sSignalAnode"
	description = ""
	parsemap = {"val":"bool"}
	
class sOvenFireplace(InformationObj):
	name = "sOvenFireplace"
	description = ""
	parsemap = {"val":"bool"}
	
class sEvaporatorIceMonitor(InformationObj):
	name = "sEvaporatorIceMonitor"
	description = ""
	parsemap = {"val":"bool"}

class sOutputVentilatorSpeed(InformationObj):
	name = "sOutputVentilatorSpeed"
	description = ""
	parsemap = {"val":"uint:8"}
	unit = "rps"

class sInputVentilatorSpeed(InformationObj):
	name = "sInputVentilatorSpeed"
	description = ""
	parsemap = {"val":"uint:8"}
	unit = "rps"

class sMainVentilatorSpeed(InformationObj):
	name = "sMainVentilatorSpeed"
	description = ""
	parsemap = {"val":"uint:8"}
	unit = "rps"
	
class sOutsideTempFiltered(InformationObj):
	name = "sOutsideTempFiltered"
	description = ""
	parsemap = {"val":FixedPOneDec16}
	unit = "°C"
	
class sRelHumidity(InformationObj):
	name = "sRelHumidity"
	description = ""
	parsemap = {"val":FixedPOneDec16}
	unit = "%"
	
class sDewPoint(InformationObj):
	name = "sDewPoint"
	description = ""
	parsemap = {"val":FixedPOneDec16}
	unit = "°C"
	
class sUserSetFanStage(InformationObj):
	name = "sUserSetFanStage"
	description = ""
	parsemap = {"val":"uint:8"}
	
class sUserSetFanRemainingTime(InformationObj):
	name = "sUserSetFanRemainingTime"
	description = ""
	parsemap = {"val":"uint:16"}
	unit = "min"

class sIntegralHeat(InformationObj):
	name = "sIntegralHeat"
	description = ""
	parsemap = {"val":FixedPOneDec16}
	
class sHeatTemp(InformationObj):
	name = "sHeatTemp"
	description = ""
	parsemap = {"val":FixedPOneDec16}
	unit = "°C"
	
class sHeatTargetTemp(InformationObj):
	name = "sHeatTargetTemp"
	description = ""
	parsemap = {"val":FixedPOneDec16}
	unit = "°C"
	
class sSeasonMode(InformationObj):
	name = "sSeasonMode"
	description = ""
	parsemap = {"val":"uint:8"}
	val_min = 1
	val_max = 2
	
	def __init__(self, data=None, value=None):
		if data is not None:
			start = data.pos
			for k,v in self.parsemap.items():
				value = data.read(v)
				if value == 1:
					self.value = "WINTER"
				elif value == 2:
					self.value = "SUMMER"
			self.rawdata = data[start:data.pos]
		else:
			self.value = value
			self.update

	def update(self):
		bits = BitStream()
		for k,v in self.parsemap.items():
			if self.value == "WINTER":
				value = 1
			elif self.value == "SUMMER":
				value = 2
			bits.append(Bits(f"{v}={value}"))
		self.rawdata = bits
		
class sIntegralSwitch(InformationObj):
	name = "sIntegralSwitch"
	description = ""
	parsemap = {"val":"uint:16"}
	
class sHcOpMode(InformationObj):
	name = "sHcOpMode"
	description = ""
	parsemap = {"val":OperationModeHC}
	
class sRoomTargetTemp(InformationObj):
	name = "sRoomTargetTemp"
	description = ""
	parsemap = {"val":FixedPOneDec16}
	unit = "°C"
	
class sOnHysteresisNo(InformationObj):
	name = "sOnHysteresisNo"
	description = ""
	parsemap = {"val":"uint:8"}

class sOffHysteresisNo(InformationObj):
	name = "sOffHysteresisNo"
	description = ""
	parsemap = {"val":"uint:8"}

class sHcBoosterStage(InformationObj):
	name = "sHcBoosterStage"
	description = ""
	parsemap = {"val":"uint:8"}

class sHeatRequest(InformationObj):
	name = "sHeatRequest"
	description = ""
	parsemap = {"val":"uint:8"}
	val_min = 0
	val_max = 5
	
	def __init__(self, data=None, value=None):
		if data is not None:
			start = data.pos
			for k,v in self.parsemap.items():
				value = data.read(v)
				if value == 0:
					self.value = "DHW"
				elif value == 2:
					self.value = "HEAT"
				elif value == 5:
					self.value = "OFF"
				elif value == 6:
					self.value = "DEFROST"
			self.rawdata = data[start:data.pos]
		else:
			self.value = value
			self.update

	def update(self):
		bits = BitStream()
		for k,v in self.parsemap.items():
			if self.value == "DHW":
				value = 0
			elif self.value == "HEAT":
				value = 2
			elif self.value == "OFF":
				value = 5
			elif self.value == "DEFROST":
				value = 6
			bits.append(Bits(f"{v}={value}"))
		self.rawdata = bits
	
class sHcStage(InformationObj):
	name = "sHcStage"
	description = ""
	parsemap = {"val":"uint:8"}
	val_min = 0
	val_max = 5
	
	def __init__(self, data=None, value=None):
		if data is not None:
			start = data.pos
			for k,v in self.parsemap.items():
				value = data.read(v)
				if value == 0:
					self.value = "OFF"
				elif value == 1:
					self.value = "SOLAR"
				elif value == 2:
					self.value = "HEATPUMP"
				elif value == 3:
					self.value = "BOOSTER_1"
				elif value == 4:
					self.value = "BOOSTER_2"
				elif value == 5:
					self.value = "BOOSTER_3"
			self.rawdata = data[start:data.pos]
		else:
			self.value = value
			self.update

	def update(self):
		bits = BitStream()
		for k,v in self.parsemap.items():
			if self.value == "OFF":
				value = 0
			elif self.value == "SOLAR":
				value = 1
			elif self.value == "HEATPUMP":
				value = 2
			elif self.value == "BOOSTER_1":
				value = 3
			elif self.value == "BOOSTER_2":
				value = 4
			elif self.value == "BOOSTER_3":
				value = 5
			bits.append(Bits(f"{v}={value}"))
		self.rawdata = bits
	
class sDhwStage(InformationObj):
	name = "sDhwStage"
	description = ""
	parsemap = {"val":"uint:8"}
	val_min = 0
	val_max = 3
	
	def __init__(self, data=None, value=None):
		if data is not None:
			start = data.pos
			for k,v in self.parsemap.items():
				value = data.read(v)
				if value == 0:
					self.value = "OFF"
				elif value == 1:
					self.value = "SOLAR"
				elif value == 2:
					self.value = "HEATPUMP"
				elif value == 3:
					self.value = "BOOST"
			self.rawdata = data[start:data.pos]
		else:
			self.value = value
			self.update

	def update(self):
		bits = BitStream()
		for k,v in self.parsemap.items():
			if self.value == "OFF":
				value = 0
			elif self.value == "SOLAR":
				value = 1
			elif self.value == "HEATPUMP":
				value = 2
			elif self.value == "BOOST":
				value = 3
			bits.append(Bits(f"{v}={value}"))
		self.rawdata = bits
	
class sHeatStageControlModul(InformationObj):
	name = "sHeatStageControlModul"
	description = ""
	parsemap = {"val":"uint:8"}
	val_min = 0
	val_max = 2
	
	def __init__(self, data=None, value=None):
		if data is not None:
			start = data.pos
			for k,v in self.parsemap.items():
				value = data.read(v)
				if value == 0:
					self.value = "NONE"
				elif value == 1:
					self.value = "DHW"
				elif value == 2:
					self.value = "HEAT"
			self.rawdata = data[start:data.pos]
		else:
			self.value = value
			self.update

	def update(self):
		bits = BitStream()
		for k,v in self.parsemap.items():
			if self.value == "NONE":
				value = 0
			elif self.value == "DHW":
				value = 1
			elif self.value == "HEAT":
				value = 2
			bits.append(Bits(f"{v}={value}"))
		self.rawdata = bits
	
class sCompBlockTime(InformationObj):
	name = "sCompBlockTime"
	description = ""
	parsemap = {"val":FixedPOneDec16}
	
class sDefrostEvaporator(InformationObj):
	name = "sDefrostEvaporator"
	description = ""
	parsemap = {"val":"uint:8"}
	
class sSolarPump(InformationObj):
	name = "sSolarPump"
	description = ""
	parsemap = {"val":"bool"}
	
class sBoostBlockTimeAfterPumpStart(InformationObj):
	name = "sBoostBlockTimeAfterPumpStart"
	description = ""
	parsemap = {"val":"uint:16"}
	
class sBoostBlockTimeAfterHD(InformationObj):
	name = "sBoostBlockTimeAfterHD"
	description = ""
	parsemap = {"val":"uint:16"}
	
class sOperationMode(InformationObj):
	name = "sOperationMode"
	description = ""
	parsemap = {"val":"uint:8"}
	val_min = 0
	val_max = 1
	
	def __init__(self, data=None, value=None):
		if data is not None:
			start = data.pos
			for k,v in self.parsemap.items():
				value = data.read(v)
				if value == 0:
					self.value = "MANUAL"
				elif value == 1:
					self.value = "AUTOMATIC"
			self.rawdata = data[start:data.pos]
		else:
			self.value = value
			self.update

	def update(self):
		bits = BitStream()
		for k,v in self.parsemap.items():
			if self.value == "MANUAL":
				value = 0
			elif self.value == "AUTOMATIC":
				value = 1
			bits.append(Bits(f"{v}={value}"))
		self.rawdata = bits
	
class sProgStateHC(InformationObj):
	name = "sProgStateHC"
	description = ""
	parsemap = {"val":OperationModeHC}

class sProgStateDHW(InformationObj):
	name = "sProgStateDHW"
	description = ""
	parsemap = {"val":OperationModeHC}
	
class sProgStateFan(InformationObj):
	name = "sProgStateFan"
	description = ""
	parsemap = {"val":OperationModeHC}

class sBaseTimeAP0(InformationObj):
	name = "sBaseTimeAP0"
	description = ""
	parsemap = {"val":"uint:32"}
	
class sStatusAP0(InformationObj):
	name = "sStatusAP0"
	description = ""
	parsemap = {"val":"uint:8"}
	
class sStartTimeAP0(InformationObj):
	name = "sStartTimeAP0"
	description = ""
	parsemap = {"val":"uint:32"}
	
class sEndTimeAP0(InformationObj):
	name = "sEndTimeAP0"
	description = ""
	parsemap = {"val":"uint:32"}
	
class sNumberErrors(InformationObj):
	name = "sNumberErrors"
	description = ""
	parsemap = {"val":"uint:8"}

class sError(InformationObj):
	name = "sError"
	description = ""
	parsemap = {"error":Error, "time":Time16, "date":Date16}
	values = {}
	
	def __init__(self, data=None, value=None):
		self.unparsed = bytes()
		if data is not None:
			start = data.bytepos
			for k,v in self.parsemap.items():
				if isinstance(v, str):
					self.values[k] = data.read(v)
				else:
					self.values[k] = v(data)
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
				self.values[k].update_recursive()
		self.update()
		
	def toBytes(self):
		return self.rawdata

	def __str__(self):
		out = ""
		for k,v in self.values.items():
			out += f" {k}: {v}\n" 
		return f"{self.name}:\n{out}"
	
class sError1(sError):
	name = "sError1"
	values = {}
	
class sError2(sError):
	name = "sError2"
	values = {}
	
class sError3(sError):
	name = "sError3"
	values = {}
	
class sError4(sError):
	name = "sError4"
	values = {}
	
class sError5(sError):
	name = "sError5"
	values = {}
	
class sError6(sError):
	name = "sError7"
	values = {}
	
class sError7(sError):
	name = "sError7"
	values = {}
	
class sError8(sError):
	name = "sError8"
	values = {}
	
class sError9(sError):
	name = "sError9"
	values = {}
	
class sError10(sError):
	name = "sError10"
	values = {}
	
class sWeekDay(InformationObj):
	name = "sWeekDay"
	description = "Day of the Week"
	parsemap = {"val":"uint:8"}
	
class pClockHour(InformationObj):
	name = "pClockHour"
	description = "Clock (Hour)"
	parsemap = {"val":"uint:8"}
	
class pClockMinutes(InformationObj):
	name = "pClockMinutes"
	description = "Clock (Minutes)"
	parsemap = {"val":"uint:8"}
	
class pClockSeconds(InformationObj):
	name = "pClockSeconds"
	description = "Clock (Seconds)"
	parsemap = {"val":"uint:8"}
	
class pClockYear(InformationObj):
	name = "pClockYear"
	description = "Clock (Year)"
	parsemap = {"val":"uint:8"}
	
class pClockMonth(InformationObj):
	name = "pClockMonth"
	description = "Clock (Month)"
	parsemap = {"val":"uint:8"}
	
class pClockDay(InformationObj):
	name = "pClockDay"
	description = "Clock (Day)"
	parsemap = {"val":"uint:8"}
	
class sFirmVersion(InformationObj):
	name = "sFirmVersion"
	description = "Firmware Version"
	parsemap = {"val":FixedPTwoDec16}
