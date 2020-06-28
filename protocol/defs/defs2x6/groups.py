from protocol.defs.defs2x6.parameters import *
from protocol.defs.defs2x6.status import *

	
class pFanGroup(InformationGroup):
	name = "P_FanGroup"
	description = "Fan Parameters"
	command = b"\x01"
	parsemap = [p37Fanstage1AirflowInlet, p38Fanstage2AirflowInlet, p39Fanstage3AirflowInlet, p40Fanstage1AirflowOutlet, p41Fanstage2AirflowOutlet, p42Fanstage3AirflowOutlet, p43UnschedVent3, p44UnschedVent2, p45UnschedVent1, p46UnschedVent0, p75PassiveCooling]
	values = {}
	
	
class pDefrostEvaGroup(InformationGroup):
	name = "P_DefrostEvaGroup"
	description = "Defrost Evaporator Parameters"
	command = b"\x03"
	parsemap = [pUpTempLimitDefrostEvaporatorEnd, pMaxTimeDefrostEvaporator, pLimitTempCondenserElectBoost, pLimitTempCondenserDefrostTerm, p47CompressorRestartDelay, p48MainFanSpeed]
	values = {}


class pDefrostAAGroup(InformationGroup):
	name = "P_DefrostAAGroup"
	description = "Defrost AA Parameters"
	command = b"\x04"
	parsemap = [pMaxDefrostDurationAAExchanger, pDefrostStartThreshold, pVolumeFlowFilterReplacement]
	values = {}
	

class pHeat1Group(InformationGroup):
	name = "P_Heat1Group"
	description = "Heat1 Parameters"
	command = b"\x05"
	parsemap = [p13GradientHC1, p14LowEndHC1, p15RoomInfluenceHC1, p16GradientHC2, p17LowEndHC2, p18RoomInfluenceHC2, p19FlowProportionHC1, p20FlowProportionHC2, pMaxSetHeatFlowTempHC1, pMinSetHeatFlowTempHC1, pMaxSetHeatFlowTempHC2, pMinSetHeatFlowTempHC2]
	values = {}


class pHeat2Group(InformationGroup):
	name = "P_Heat2Group"
	description = "Heat2 Parameters"
	command = b"\x06"
	parsemap = [p21Hyst1, p22Hyst2, p23Hyst3, p24Hyst4, p25Hyst5, p26Hyst6, p27Hyst7, p28Hyst8, p29HystAsymmetry, p30integralComponent, p31MaxBoostStages, pMaxHeatFlowTemp, p49SummerModeTemp, p50SummerModeHysteresis, p77OutTempFilterTime, p78DualModePoint, p79BoosterTimeoutHC]
	values = {}
	

class pDHWGroup(InformationGroup):
	name = "P_DHWGroup"
	description = "DHW Parameters"
	command = b"\x07"
	parsemap = [p32HystDHW, p33BoosterTimeoutDHW, p34TempLimitBoostDHW, p35PasteurisationInterval, p36MaxDurationDHWLoad, pPasteurisationTemp, pMaxBoostStagesDHW, p84EnableDHWBuffer, pMaxHeatFlowTempDHW, p89DHWMode]
	values = {}


class pSolarGroup(InformationGroup):
	name = "P_SolarGroup"
	description = "Solar Parameters"
	command = b"\x08"
	parsemap = [p80EnableSolar, p81DiffTempSolarLoading, p82DelayCompStartSolar, p83DHWTempSolarMode, HystDiffTempSolar, CollectLimitTempSolar]
	values = {}


class pCircPumpGroup(InformationGroup):
	name = "P_CircPumpGroup"
	description = "CircPump Parameters"
	command = b"\x0A"
	parsemap = [p54MinPumpCycles, p55MaxPumpCycles, p56OutTempMaxPumpCycles, p57OutTempMinPumpCycles, p58SuppressTempCaptPumpStart]
	values = {}
	
	
class pHeatProgGroup(InformationGroup):
	name = "P_HeatProgGroup"
	description = "Heat Program Parameters"
	command = b"\x0B"
	parsemap = [pProgHC1StartTime, pProgHC1EndTime, "bin:1", pProgHC1Sunday, pProgHC1Saturday, pProgHC1Friday, pProgHC1Thursday, pProgHC1Wednesday, pProgHC1Tuesday, pProgHC1Monday, pProgHC1Enable, pProgHC2StartTime, pProgHC2EndTime, "bin:1", pProgHC2Sunday, pProgHC2Saturday, pProgHC2Friday, pProgHC2Thursday, pProgHC2Wednesday, pProgHC2Tuesday, pProgHC2Monday, pProgHC2Enable]
	values = {}
	
	
class pDHWProgGroup(InformationGroup):
	name = "P_DHWProgGroup"
	description = "Hot Water Program Parameters"
	command = b"\x0C"
	parsemap = [pProgDHWStartTime, pProgDHWEndTime, "bin:1", pProgDHWSunday, pProgDHWSaturday, pProgDHWFriday, pProgDHWThursday, pProgDHWWednesday, pProgDHWTuesday, pProgDHWMonday, pProgDHWEnable]
	values = {}
	

class pFanProgGroup(InformationGroup):
	name = "P_FanProgGroup"
	description = "Fan Program Parameters"
	command = b"\x0D"
	parsemap = [pProgFan1StartTime, pProgFan1EndTime, "bin:1", pProgFan1Sunday, pProgFan1Saturday, pProgFan1Friday, pProgFan1Thursday, pProgFan1Wednesday, pProgFan1Tuesday, pProgFan1Monday, pProgFan1Enable, pProgFan2StartTime, pProgFan2EndTime, "bin:1", pProgFan2Sunday, pProgFan2Saturday, pProgFan2Friday, pProgFan2Thursday, pProgFan2Wednesday, pProgFan2Tuesday, pProgFan2Monday, pProgFan2Enable]
	values = {}
	
	
class pRestartGroup(InformationGroup):
	name = "P_RestartGroup"
	description = "Restart Parameters"
	command = b"\x0E"
	parsemap = [p59RestartBeforeSetbackEnd]
	values = {}
	

class pAbsenceGroup(InformationGroup):
	name = "P_AbsenceGroup"
	description = "Absence Parameters"
	command = b"\x0F"
	parsemap = []
	values = {}
	

class pDryHeatGroup(InformationGroup):
	name = "P_DryHeatGroup"
	description = "DryHeat Parameters"
	command = b"\x10"
	parsemap = [p70StartDryHeat, p71BaseTemp, p72PeakTemp, p73TempDuration, p74TempIncrease]
	values = {}
	
	
class pP01P12Group(InformationGroup):
	name = "P_P01-P12Group"
	description = "P01-P12 Parameters"
	command = b"\x17"
	parsemap = [p01RoomTempDay, p02RoomTempNight, p03RoomTempStandby, p04DHWsetTempDay, p05DHWsetTempNight, p06DHWsetTempStandby, p07FanStageDay, p08FanStageNight, p09FanStageStandby, p10HCTempManual, p11DHWsetTempManual, p12FanStageManual]
	values = {}
	

class sSolarGroup(InformationGroup):
	name = "S_SolarGroup"
	description = "Solar Status"
	command = b"\x16"
	parsemap = [sCollectorTemp, sDhwTemp, sFlowTemp, sEdSolPump]
	values = {}
	
	
class sProgramGroup(InformationGroup):
	name = "S_ProgramGroup"
	description = "Program Status"
	command = b"\xEE"
	parsemap = [sOperationMode, "bin:16", sProgStateHC, sProgStateDHW, sProgStateFan, sBaseTimeAP0, sStatusAP0, sStartTimeAP0, sEndTimeAP0]
	values = {}
	
	
class sFanGroup(InformationGroup):
	name = "S_FanGroup"
	description = "Fan Status"
	command = b"\xE8"
	parsemap = [sAutoFanCalib, "bin:64", sAirflowTolerance, sInputFanSpeedCal, sOutputFanSpeedCal, sInputFanAirflowCal, sOutputFanAirflowCal, sInputFanSpeed0, sOutputFanSpeed0, sInputFanSpeed200, sOutputFanSpeed200, sAirflowCalibrationInterval, sTimeToCalibration, sInputFanSpeed, sOutputFanSpeed, sInputFanAirflowSet, sOutputFanAirflowSet, sInputFanSpeedTarget, sOutputFanSpeedTarget]
	values = {}
	
	
class sHistoryGroup(InformationGroup):
	name = "S_HistoryGroup"
	description = "History Status"
	command = b"\x09"
	parsemap = [sOperatingHours1, sOperatingHours2, sHeatingHours, sDhwHours, sCoolingHours]
	values = {}
	
	
class sLast10ErrorsGroup(InformationGroup):
	name = "S_Last10ErrorsGroup"
	description = "Last 10 Errors"
	command = b"\xD1"
	parsemap = [sNumberErrors, sError1, sError2, sError3, sError4, sError5]
	values = {}
	
	
class sControlGroup(InformationGroup):
	name = "S_ControlGroup"
	description = "Control Status"
	command = b"\xF2"
	parsemap = [sHeatRequest, sHeatRequest, sHcStage, sDhwStage, sHeatStageControlModul, sCompBlockTime, sPasteurisationMode, sDefrostEvaporator, sBoosterStage2, sSolarPump, sBoosterStage1, sCompressor, sHeatPipeValve, sDiverterValve, sDhwPump, sHeatingCircuitPump, "bin:6", sMixerOpen, sMixerClosed, "bin:16", sBoostBlockTimeAfterPumpStart, sBoostBlockTimeAfterHD]
	values = {}
	
	
class sDhwGroup(InformationGroup):
	name = "S_DHW"
	description = "Hot Water Status"
	command = b"\xF3"
	parsemap = [sDhwTemp, sOutsideTemp, sDhwTargetTemp, sCompBlockTimeTemp, "bin:16", sHeatBlockTime, sDhwBoosterStage, "bin:8", sPasteurisationMode, sDhwOpMode]
	values = {}
	
	
class sHC1Group(InformationGroup):
	name = "S_HC1"
	description = "Heat Circle 1 Status"
	command = b"\xF4"
	parsemap = [sOutsideTemp,"bin:16", sReturnTemp, sIntegralHeat, sFlowTemp, sHeatTargetTemp, sHeatTemp, sOnHysteresisNo, sOffHysteresisNo, sHcBoosterStage, sSeasonMode, "bin:16", sIntegralSwitch, sHcOpMode, "bin:16", "bin:16", "bin:16", "bin:16", "bin:16", "bin:16", "bin:16", sRoomTargetTemp ]
	values = {}
	
	
class sHC2Group(InformationGroup):
	name = "S_HC2"
	description = "Heat Circle 2 Status"
	command = b"\xF5"
	parsemap = [sOutsideTemp, sReturnTemp, sFlowTemp, sHeatTargetTemp, sHeatTargetTemp, "bin:16", "bin:8", sSeasonMode, "bin:16", sHcOpMode]
	values = {}
	
	
class sSystemGroup(InformationGroup):
	name = "S_System"
	description = "System Status"
	command = b"\xF6"
	parsemap = [sUserSetFanStage, sUserSetFanRemainingTime, sError1]
	values = {}
	
	
class sGlobalGroup(InformationGroup):
	name = "S_GlobalGroup"
	description = "Global Status"
	command = b"\xFB"
	parsemap = [sCollectorTemp, sOutsideTemp, sFlowTempHC1, sReturnTemp, sOHotGasTemp, sDhwTemp, sFlowTempHC2, sInsideTemp, sEvaporatorTemp, sCondensorTemp, sBoosterStage3, sBoosterStage2, sBoosterStage1, sCompressor, sHeatPipeValve, sDiverterValve, sDhwPump, sHeatingCircuitPump, "bin:6", sMixerClosed, sMixerOpen, sOutputVentilatorPower, sInputVentilatorPower, sMainVentilatorPower, sHighPressureSensor, sLowPressureSensor, sSignalAnode, sOvenFireplace, sEvaporatorIceMonitor, "bin:3", sOutputVentilatorSpeed, sInputVentilatorSpeed, sMainVentilatorSpeed, "bin:8", sOutsideTempFiltered, "bin:8", sRelHumidity, "bin:16", ]
	values = {}	
	
	
class pTimedateGroup(InformationGroup):
	name = "P_Timedate"
	description = "Timedate Parameter"
	command = b"\xFC"
	parsemap = ["bin:8",sWeekDay, pClockHour, pClockMinutes, pClockSeconds, pClockYear, "bin:8", pClockMonth, pClockDay]
	values = {}
	
	
class sFirmwareGroup(InformationGroup):
	name = "S_FirmwareGroup"
	description = "Firmware Status"
	command = b"\xFD"
	parsemap = [sFirmVersion]
	values = {}
