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
	
	
class collectorTemp(InformationObj):
	name = "collectorTemp"
	description = ""
	parsemap = {"val":FixedPOneDec16}
	unit = "°C"

class dhwTemp(InformationObj):
	name = "dhwTemp"
	description = ""
	parsemap = {"val":FixedPOneDec16}
	unit = "°C"
	
class flowTemp(InformationObj):
	name = "flowTemp"
	description = ""
	parsemap = {"val":FixedPOneDec16}
	unit = "°C"
	
class edSolPump(InformationObj):
	name = "edSolPump"
	description = ""
	parsemap = {"val":"int:8"}
	unit = "°C"

class SSolarGroup(InformationGroup):
	name = "S_SolarGroup"
	description = "Solar Status"
	command = b"\x16"
	parsemap = [collectorTemp, dhwTemp, flowTemp, edSolPump]
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
	parsemap = []
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
	parsemap = []
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
	parsemap = []
	values = {}
	
	
class STimedateGroup(InformationGroup):
	name = "P_Timedate"
	description = "Timedate Parameter"
	command = b"\xFC"
	parsemap = []
	values = {}
	
	
class SFirmwareGroup(InformationGroup):
	name = "S_FirmwareGroup"
	description = "Firmware Status"
	command = b"\xFD"
	parsemap = []
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
