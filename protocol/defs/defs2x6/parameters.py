from protocol.defs.defs import *

class p37Fanstage1AirflowInlet(InformationObj):
	name = "p37Fanstage1AirflowInlet"
	description = ""
	parsemap = {"val":"uint:16"}
	
class p38Fanstage2AirflowInlet(InformationObj):
	name = "p38Fanstage2AirflowInlet"
	description = ""
	parsemap = {"val":"uint:16"}

class p39Fanstage3AirflowInlet(InformationObj):
	name = "p39Fanstage3AirflowInlet"
	description = ""
	parsemap = {"val":"uint:16"}
	
class p40Fanstage1AirflowOutlet(InformationObj):
	name = "p40Fanstage1AirflowOutlet"
	description = ""
	parsemap = {"val":"uint:16"}
	
class p41Fanstage2AirflowOutlet(InformationObj):
	name = "p41Fanstage2AirflowOutlet"
	description = ""
	parsemap = {"val":"uint:16"}
	
class p42Fanstage3AirflowOutlet(InformationObj):
	name = "p42Fanstage3AirflowOutlet"
	description = ""
	parsemap = {"val":"uint:16"}

class p43UnschedVent3(InformationObj):
	name = "p43UnschedVent3"
	description = ""
	parsemap = {"val":"uint:16"}
	
class p44UnschedVent2(InformationObj):
	name = "p44UnschedVent2"
	description = ""
	parsemap = {"val":"uint:16"}
	
class p45UnschedVent1(InformationObj):
	name = "p45UnschedVent1"
	description = ""
	parsemap = {"val":"uint:16"}
	
class p46UnschedVent0(InformationObj):
	name = "p46UnschedVent0"
	description = ""
	parsemap = {"val":"uint:16"}
	
class p75PassiveCooling(InformationObj):
	name = "p75PassiveCooling"
	description = ""
	parsemap = {"val":"uint:16"}
	
class p80EnableSolar(InformationObj):
	name = "p80EnableSolar"
	description = ""
	parsemap = {"val":"uint:8"}
	
class p81DiffTempSolarLoading(InformationObj):
	name = "p81DiffTempSolarLoading"
	description = ""
	parsemap = {"val":FixedPOneDec16}
	unit = "K"
	
class p82DelayCompStartSolar(InformationObj):
	name = "p82DelayCompStartSolar"
	description = ""
	parsemap = {"val":"uint:8"}
	
class p84DHWTempSolarMode(InformationObj):
	name = "p84DHWTempSolarMode"
	description = ""
	parsemap = {"val":FixedPOneDec16}
	
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
	
class SCollectorTemp(InformationObj):
	name = "S_CollectorTemp"
	description = ""
	parsemap = {"val":FixedPOneDec16}
	unit = "°C"
	
class SDHWTemp(InformationObj):
	name = "S_DHWTemp"
	description = ""
	parsemap = {"val":FixedPOneDec16}
	unit = "°C"
	
class SFlowTemp(InformationObj):
	name = "S_FlowTemp"
	description = ""
	parsemap = {"val":FixedPOneDec16}
	unit = "°C"
	
class SedSolPump(InformationObj):
	name = "S_edSolPump"
	description = ""
	parsemap = {"val":"int:8"}
	unit = "%"
	
class SAutoFanCalib(InformationObj):
	name = "S_AutoFanCalib"
	description = ""
	parsemap = {"val":"uint:8"}
	unit = ""
	
class SInputFanSpeedCal(InformationObj):
	name = "S_InputFanSpeedCal"
	description = ""
	parsemap = {"val":"uint:16"}
	unit = ""	

class SOutputFanSpeedCal(InformationObj):
	name = "S_OutputFanSpeedCal"
	description = ""
	parsemap = {"val":"uint:16"}
	unit = ""
	
class SInputFanAirflowCal(InformationObj):
	name = "S_InputFanAirflowCal"
	description = ""
	parsemap = {"val":"uint:16"}
	unit = "m3/h"	

class SOutputFanAirflowCal(InformationObj):
	name = "S_OutputFanAirflowCal"
	description = ""
	parsemap = {"val":"uint:8"}
	unit = "m3/h"
	
class SInputFanSpeed(InformationObj):
	name = "S_InputFanSpeed"
	description = ""
	parsemap = {"val":"uint:8"}
	unit = "rps"	

class SOutputFanSpeed(InformationObj):
	name = "S_OutputFanSpeed"
	description = ""
	parsemap = {"val":"uint:8"}
	unit = "rps"
	
class SInputFanAirflowSet(InformationObj):
	name = "S_InputFanAirflowSet"
	description = ""
	parsemap = {"val":"uint:16"}
	unit = "m3/h"	

class SOutputFanAirflowSet(InformationObj):
	name = "S_OutputFanAirflowSet"
	description = ""
	parsemap = {"val":"uint:16"}
	unit = "m3/h"
	
class SInputFanSpeedTarget(InformationObj):
	name = "S_InputFanSpeedTarget"
	description = ""
	parsemap = {"val":"uint:8"}
	unit = "%"

class SOutputFanSpeedTarget(InformationObj):
	name = "S_OutputFanSpeedTarget"
	description = ""
	parsemap = {"val":"uint:8"}
	unit = "%"
	
class SInputFanSpeed0(InformationObj):
	name = "S_InputFanSpeed0"
	description = ""
	parsemap = {"val":"uint:16"}
	unit = "rps"	

class SOutputFanSpeed0(InformationObj):
	name = "S_OutputFanSpeed0"
	description = ""
	parsemap = {"val":"uint:16"}
	unit = "rps"
	
class SInputFanSpeed200(InformationObj):
	name = "S_InputFanSpeed200"
	description = ""
	parsemap = {"val":"uint:16"}
	unit = "rps"	

class SOutputFanSpeed200(InformationObj):
	name = "S_OutputFanSpeed200"
	description = ""
	parsemap = {"val":"uint:16"}
	unit = "rps"
	
class SAirflowTolerance(InformationObj):
	name = "S_AirflowTolerance"
	description = ""
	parsemap = {"val":"uint:8"}
	unit = ""
	
class SAirflowCalibrationInterval(InformationObj):
	name = "S_AirflowCalibrationInterval"
	description = ""
	parsemap = {"val":"uint:8"}
	unit = ""	

class STimeToCalibration(InformationObj):
	name = "S_TimeToCalibration"
	description = ""
	parsemap = {"val":"uint:8"}
	unit = ""
	
class SOutsideTemp(InformationObj):
	name = "S_OutsideTemp"
	description = ""
	parsemap = {"val":FixedPOneDec16}
	unit = "°C"
	
class PDHWTemp(InformationObj):
	name = "P_DHWTemp"
	description = ""
	parsemap = {"val":FixedPOneDec16}
	unit = "°C"
	
class SCompBlockTimeTemp(InformationObj):
	name = "S_CompBlockTimeTemp"
	description = ""
	parsemap = {"val":FixedPOneDec16}
	unit = ""
	
class PDHWHysteresis(InformationObj):
	name = "P_DHWHysteresis"
	description = ""
	parsemap = {"val":"uint:8"}
	unit = "K"
	
'''
"FBglob206" => [["outsideTemp: ", 8, 4, "hex2int", 10],	[" flowTemp: ",		        12, 4, "hex2int", 10],
	      [" returnTemp: ",		    16, 4, "hex2int", 10],  [" hotGasTemp: ", 	        20, 4, "hex2int", 10],
	      [" dhwTemp: ",		    24, 4, "hex2int", 10],  [" flowTempHC2: ",	        28, 4, "hex2int", 10],
	      [" evaporatorTemp: ",	    36, 4, "hex2int", 10],  [" condenserTemp: ",	    40, 4, "hex2int", 10],
	      [" mixerOpen: ",		    47, 1, "bit1", 1],      [" mixerClosed: ",		    47, 1, "bit0", 1],
	      [" heatPipeValve: ",	    45, 1, "bit3", 1],      [" diverterValve: ",		45, 1, "bit2", 1],
	      [" dhwPump: ",		    45, 1, "bit1", 1],      [" heatingCircuitPump: ",	45, 1, "bit0", 1],
	      [" solarPump: ",		    44, 1, "n.a", 1],      	[" compressor: ",		    44, 1, "bit0", 1],
	      [" boosterStage3: ",	    44, 1, "bit3", 1],      [" boosterStage2: ",		44, 1, "bit2", 1], 	      
          [" boosterStage1: ",	    44, 1, "bit1", 1],      [" highPressureSensor: ",	54, 1, "bit3", 1],
	      [" lowPressureSensor: ",	54, 1, "bit2", 1],      [" evaporatorIceMonitor: ",	55, 1, "bit3", 1],
	      [" signalAnode: ",	    54, 1, "bit1", 1],      [" evuRelease: ",		    48, 1, "n.a.", 1],
	      [" ovenFireplace: ",	    54, 1, "bit0", 1],      [" STB: ",			        48, 1, "n.a.", 1],
	      [" outputVentilatorPower: ",48, 2, "hex", 1],  	[" inputVentilatorPower: ",	50, 2, "hex", 1],	[" mainVentilatorPower: ",	52, 2, "hex", 255/100],          
          [" outputVentilatorSpeed: ",56, 2, "hex", 1],	    [" inputVentilatorSpeed: ",	58, 2, "hex", 1],  	[" mainVentilatorSpeed: ",	60, 2, "hex", 1],
          [" outsideTempFiltered: ",64, 4, "hex2int", 10],	[" relHumidity: ",		    70, 4, "n.a.", 1],
          [" dewPoint: ",		    5, 4, "n.a.", 1],
	      [" P_Nd: ",		        5, 4, "n.a.", 1],	    [" P_Hd: ",			        5, 4, "n.a.", 1],
	      [" actualPower_Qc: ",	    5, 8, "n.a.", 1],	    [" actualPower_Pel: ",		5, 8, "n.a.", 1],
	      [" collectorTemp: ",	    4,  4, "hex2int", 10],	[" insideTemp: ",		    32, 4, "hex2int", 10] 
'''
	
class SFlowTempHC1(InformationObj):
	name = "S_FlowTempHC1"
	description = ""
	parsemap = {"val":FixedPOneDec16}
	unit = "°C"
	
class SReturnTemp(InformationObj):
	name = "S_ReturnTemp"
	description = ""
	parsemap = {"val":FixedPOneDec16}
	unit = "°C"
	
class SOHotGasTemp(InformationObj):
	name = "S_HotGasTemp"
	description = ""
	parsemap = {"val":FixedPOneDec16}
	unit = "°C"
	
class SDHWTemp(InformationObj):
	name = "S_DHWTemp"
	description = ""
	parsemap = {"val":FixedPOneDec16}
	unit = "°C"
	
class SFlowTempHC2(InformationObj):
	name = "S_FlowTempHC2"
	description = ""
	parsemap = {"val":FixedPOneDec16}
	unit = "°C"
	
class SInsideTemp(InformationObj):
	name = "S_InsideTemp"
	description = ""
	parsemap = {"val":FixedPOneDec16}
	unit = "°C"
	
class SEvaporatorTemp(InformationObj):
	name = "S_EvaporatorTemp"
	description = ""
	parsemap = {"val":FixedPOneDec16}
	unit = "°C"
	
class SCondensorTemp(InformationObj):
	name = "S_CondesorTemp"
	description = ""
	parsemap = {"val":FixedPOneDec16}
	unit = "°C"
	
class SMixerOpen(InformationObj):
	name = "S_MixerOpen"
	description = ""
	parsemap = {"val":"bool"}
	
class SOutputVentilatorPower(InformationObj):
	name = "S_OutputVentilatorPower"
	description = ""
	parsemap = {"val":"uint:8"}
	unit = "%"

class SInputVentilatorPower(InformationObj):
	name = "S_InputVentilatorPower"
	description = ""
	parsemap = {"val":"uint:8"}
	unit = "%"

class SMainVentilatorPower(InformationObj):
	name = "S_MainVentilatorPower"
	description = ""
	parsemap = {"val":"uint:8"}
	unit = "%"

class SOutputVentilatorSpeed(InformationObj):
	name = "S_OutputVentilatorSpeed"
	description = ""
	parsemap = {"val":"uint:8"}
	unit = "rps"

class SInputVentilatorSpeed(InformationObj):
	name = "S_InputVentilatorSpeed"
	description = ""
	parsemap = {"val":"uint:8"}
	unit = "rps"

class SMainVentilatorSpeed(InformationObj):
	name = "S_MainVentilatorSpeed"
	description = ""
	parsemap = {"val":"uint:8"}
	unit = "rps"
	
class SOutsideTempFiltered(InformationObj):
	name = "S_OutsideTempFiltered"
	description = ""
	parsemap = {"val":FixedPOneDec16}
	unit = "°C"
	
class SRelHumidity(InformationObj):
	name = "S_RelHumidity"
	description = ""
	parsemap = {"val":FixedPOneDec16}
	unit = "%"
	
class SDewPoint(InformationObj):
	name = "S_DewPoint"
	description = ""
	parsemap = {"val":FixedPOneDec16}
	unit = "°C"
	
class SWeekDay(InformationObj):
	name = "S_WeekDay"
	description = "Day of the Week"
	parsemap = {"val":"uint:8"}
	
class PClockHour(InformationObj):
	name = "P_ClockHour"
	description = "Clock (Hour)"
	parsemap = {"val":"uint:8"}
	
class PClockMinutes(InformationObj):
	name = "P_ClockMinutes"
	description = "Clock (Minutes)"
	parsemap = {"val":"uint:8"}
	
class SClockSeconds(InformationObj):
	name = "S_ClockSeconds"
	description = "Clock (Seconds)"
	parsemap = {"val":"uint:8"}
	
class PClockYear(InformationObj):
	name = "P_ClockYear"
	description = "Clock (Year)"
	parsemap = {"val":"uint:8"}
	
class PClockMonth(InformationObj):
	name = "P_ClockMonth"
	description = "Clock (Month)"
	parsemap = {"val":"uint:8"}
	
class PClockDay(InformationObj):
	name = "P_ClockDay"
	description = "Clock (Day)"
	parsemap = {"val":"uint:8"}
	
class SFirmVersion(InformationObj):
	name = "S_FirmVersion"
	description = "Firmware Version"
	parsemap = {"val":FixedPTwoDec16}
