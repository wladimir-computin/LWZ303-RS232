from protocol.defs.defs2x6.groups import *


PARAM_GROUPS = [pP01P12Group, pExpertGroup, pHeat1Group, pHeat2Group, pDHWGroup, pFanGroup, pRestartGroup, pDryHeatGroup, pSolarGroup, pDefrostEvaGroup, pDefrostAAGroup, pCircPumpGroup, pHeatProgGroup, pDHWProgGroup, pFanProgGroup, pTimedateGroup]

STATUS_GROUPS = [sHistoryGroup, sSolarGroup, sProgramGroup, sFanGroup, sControlGroup, sDhwGroup, sHC1Group, sHC2Group, sSystemGroup, sGlobalGroup, sFirmwareGroup, sLast10ErrorsGroup]

ALL_PARAMS = [param for group in PARAM_GROUPS for param in group.parsemap if not isinstance(param,str)]
ALL_STATUS = [status for group in STATUS_GROUPS for status in group.parsemap if not isinstance(status,str)]

def paramToGroup(param):
	for group in PARAM_GROUPS:
		if param in group.parsemap:
			return group
	return None

def statusToGroup(status):
	for group in STATUS_GROUPS:
		if status in group.parsemap:
			return group
	return None

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
