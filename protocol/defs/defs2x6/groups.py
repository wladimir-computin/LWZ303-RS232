from protocol.defs.defs import InformationGroup
from protocol.defs.defs2x6.parameters import *

	
class PFanGroup(InformationGroup):
	name = "P_FanGroup"
	description = "Fan Parameters"
	command = b"\x01"
	parsemap = [p37Fanstage1AirflowInlet, p38Fanstage2AirflowInlet, p39Fanstage3AirflowInlet, p40Fanstage1AirflowOutlet, p41Fanstage2AirflowOutlet, p42Fanstage3AirflowOutlet, p43UnschedVent3, p44UnschedVent2, p45UnschedVent1, p46UnschedVent0, p75PassiveCooling]
	values = {}
	
	
class PDefrostEvaGroup(InformationGroup):
	name = "P_DefrostEvaGroup"
	description = "Defrost Evaporator Parameters"
	command = b"\x03"
	parsemap = []
	values = {}


class PDefrostAAGroup(InformationGroup):
	name = "P_DefrostAAGroup"
	description = "Defrost AA Parameters"
	command = b"\x04"
	parsemap = []
	values = {}
	

class PHeat1Group(InformationGroup):
	name = "P_Heat1Group"
	description = "Heat1 Parameters"
	command = b"\x05"
	parsemap = []
	values = {}


class PHeat2Group(InformationGroup):
	name = "P_Heat2Group"
	description = "Heat2 Parameters"
	command = b"\x06"
	parsemap = []
	values = {}
	

class PDHWGroup(InformationGroup):
	name = "P_DHWGroup"
	description = "DHW Parameters"
	command = b"\x07"
	parsemap = []
	values = {}

class PSolarGroup(InformationGroup):
	name = "P_SolarGroup"
	description = "Solar Parameters"
	command = b"\x08"
	parsemap = [p80EnableSolar, p81DiffTempSolarLoading, p82DelayCompStartSolar, p84DHWTempSolarMode, HystDiffTempSolar, CollectLimitTempSolar]
	values = {}
	

class SHistoryGroup(InformationGroup):
	name = "S_HistoryGroup"
	description = "History Status"
	command = b"\x09"
	parsemap = []
	values = {}


class PCircPumpGroup(InformationGroup):
	name = "P_CircPumpGroup"
	description = "CircPump Parameters"
	command = b"\x0A"
	parsemap = []
	values = {}
	
	
class PHeatProgGroup(InformationGroup):
	name = "P_HeatProgGroup"
	description = "Heat Program Parameters"
	command = b"\x0B"
	parsemap = []
	values = {}
	
	
class PDHWProgGroup(InformationGroup):
	name = "P_DHWProgGroup"
	description = "Hot Water Program Parameters"
	command = b"\x0C"
	parsemap = []
	values = {}
	

class PFanProgGroup(InformationGroup):
	name = "P_FanProgGroup"
	description = "Fan Program Parameters"
	command = b"\x0D"
	parsemap = []
	values = {}
	
	
class PRestartGroup(InformationGroup):
	name = "P_RestartGroup"
	description = "Restart Parameters"
	command = b"\x0E"
	parsemap = []
	values = {}
	

class PAbsenceGroup(InformationGroup):
	name = "P_AbsenceGroup"
	description = "Absence Parameters"
	command = b"\x0F"
	parsemap = []
	values = {}
	

class PDryHeatGroup(InformationGroup):
	name = "P_DryHeatGroup"
	description = "DryHeat Parameters"
	command = b"\x10"
	parsemap = []
	values = {}
	

class SSolarGroup(InformationGroup):
	name = "S_SolarGroup"
	description = "Solar Status"
	command = b"\x16"
	parsemap = [SCollectorTemp, SDHWTemp, SFlowTemp, SedSolPump]
	values = {}
	
	
class PP01P12Group(InformationGroup):
	name = "P_P01-P12Group"
	description = "P01-P12 Parameters"
	command = b"\x17"
	parsemap = []
	values = {}
	
	
class SProgramGroup(InformationGroup):
	name = "S_ProgramGroup"
	description = "Program Status"
	command = b"\xEE"
	parsemap = []
	values = {}
	
	
class SFanGroup(InformationGroup):
	name = "S_FanGroup"
	description = "Fan Status"
	command = b"\xE8"
	parsemap = [SAutoFanCalib, "pad:64", SAirflowTolerance, SInputFanSpeedCal, SOutputFanSpeedCal, SInputFanAirflowCal, SOutputFanAirflowCal, SInputFanSpeed0, SOutputFanSpeed0, SInputFanSpeed200, SOutputFanSpeed200, SAirflowCalibrationInterval, STimeToCalibration, SInputFanSpeed, SOutputFanSpeed, SInputFanAirflowSet, SOutputFanAirflowSet, SInputFanSpeedTarget, SOutputFanSpeedTarget]
	values = {}
	
	
class SLast10errorsGroup(InformationGroup):
	name = "S_Last10errorsGroup"
	description = "Last 10 Errors"
	command = b"\xD1"
	parsemap = []
	values = {}
	
	
class SControlGroup(InformationGroup):
	name = "S_ControlGroup"
	description = "Control Status"
	command = b"\xF2"
	parsemap = []
	values = {}
	
	
class SDHWGroup(InformationGroup):
	name = "S_DHW"
	description = "Hot Water Status"
	command = b"\xF3"
	parsemap = [SDHWTemp, SOutsideTemp, PDHWTemp, SCompBlockTimeTemp]
	values = {}
	
	
class SHC1Group(InformationGroup):
	name = "S_HC1"
	description = "Heat Circle 1 Status"
	command = b"\xF4"
	parsemap = []
	values = {}
	
	
class SHC2Group(InformationGroup):
	name = "S_HC2"
	description = "Heat Circle 2 Status"
	command = b"\xF5"
	parsemap = []
	values = {}
	
	
class SSystemGroup(InformationGroup):
	name = "S_System"
	description = "System Status"
	command = b"\xF6"
	parsemap = []
	values = {}
	
	
class SGlobalGroup(InformationGroup):
	name = "S_GlobalGroup"
	description = "Global Status"
	command = b"\xFB"
	parsemap = [SCollectorTemp, SOutsideTemp, SFlowTempHC1, SReturnTemp, SOHotGasTemp, SDHWTemp, SFlowTempHC2, SInsideTemp, SEvaporatorTemp, SCondensorTemp, "pad:16", SOutputVentilatorPower, SInputVentilatorPower, SMainVentilatorPower, "pad:8", SOutputVentilatorSpeed, SInputVentilatorSpeed, SMainVentilatorSpeed, SOutsideTempFiltered, SRelHumidity, SDewPoint, "pad:16", ]
	values = {}	
	
	
class PTimedateGroup(InformationGroup):
	name = "P_Timedate"
	description = "Timedate Parameter"
	command = b"\xFC"
	parsemap = ["pad:8", SWeekDay, PClockHour, PClockMinutes, SClockSeconds, PClockYear, "pad:8", PClockMonth, PClockDay]
	values = {}
	
	
class SFirmwareGroup(InformationGroup):
	name = "S_FirmwareGroup"
	description = "Firmware Status"
	command = b"\xFD"
	parsemap = [SFirmVersion]
	values = {}
