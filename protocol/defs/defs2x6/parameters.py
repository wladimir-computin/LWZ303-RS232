from protocol.defs.defs import *

class p01RoomTempDay(InformationObj):
	name = "p01RoomTempDay"
	description = ""
	parsemap = {"val":FixedPOneDec16}
	unit = "°C"
	
class p02RoomTempNight(InformationObj):
	name = "p02RoomTempNight"
	description = ""
	parsemap = {"val":FixedPOneDec16}
	unit = "°C"
	
class p03RoomTempStandby(InformationObj):
	name = "p03RoomTempStandby"
	description = ""
	parsemap = {"val":FixedPOneDec16}
	unit = "°C"
	
class p04DHWsetTempDay(InformationObj):
	name = "p04DHWsetTempDay"
	description = ""
	parsemap = {"val":FixedPOneDec16}
	unit = "°C"
	
class p05DHWsetTempNight(InformationObj):
	name = "p05DHWsetTempNight"
	description = ""
	parsemap = {"val":FixedPOneDec16}
	unit = "°C"
	
class p06DHWsetTempStandby(InformationObj):
	name = "p06DHWsetTempStandby"
	description = ""
	parsemap = {"val":FixedPOneDec16}
	unit = "°C"
	
class p07FanStageDay(InformationObj):
	name = "p07FanStageDay"
	description = ""
	parsemap = {"val":"uint:8"}
	
class p08FanStageNight(InformationObj):
	name = "p08FanStageNight"
	description = ""
	parsemap = {"val":"uint:8"}
	
class p09FanStageStandby(InformationObj):
	name = "p09FanStageStandby"
	description = ""
	parsemap = {"val":"uint:8"}
	
class p10HCTempManual(InformationObj):
	name = "p10HCTempManual"
	description = ""
	parsemap = {"val":FixedPOneDec16}
	unit = "°C"
	
class p11DHWsetTempManual(InformationObj):
	name = "p11DHWsetTempManual"
	description = ""
	parsemap = {"val":FixedPOneDec16}
	unit = "°C"
	
class p12FanStageManual(InformationObj):
	name = "p12FanStageManual"
	description = ""
	parsemap = {"val":"uint:8"}
	
class p13GradientHC1(InformationObj):
	name = "p13GradientHC1"
	description = ""
	parsemap = {"val":FixedPOneDec16}
	
class p14LowEndHC1(InformationObj):
	name = "p14LowEndHC1"
	description = ""
	parsemap = {"val":FixedPOneDec16}
	unit = "K"
	
class p15RoomInfluenceHC1(InformationObj):
	name = "p15RoomInfluenceHC1"
	description = ""
	parsemap = {"val":"uint:8"}
	unit = "%"
	
class p16GradientHC2(InformationObj):
	name = "p16GradientHC2"
	description = ""
	parsemap = {"val":FixedPOneDec16}
	
class p17LowEndHC2(InformationObj):
	name = "p17LowEndHC2"
	description = ""
	parsemap = {"val":FixedPOneDec16}
	unit = "K"
	
class p18RoomInfluenceHC2(InformationObj):
	name = "p18RoomInfluenceHC2"
	description = ""
	parsemap = {"val":"uint:8"}
	unit = "%"
	
class p19LowEndHC2(InformationObj):
	name = "p19LowEndHC2"
	description = ""
	parsemap = {"val":FixedPOneDec16}
	unit = "K"
	
class p20LowEndHC2(InformationObj):
	name = "p20LowEndHC2"
	description = ""
	parsemap = {"val":FixedPOneDec16}
	unit = "K"
	
class pMaxSetHeatFlowTempHC1(InformationObj):
	name = "pMaxSetHeatFlowTempHC1"
	description = ""
	parsemap = {"val":FixedPOneDec16}
	unit = "°C"
	
class pMinSetHeatFlowTempHC1(InformationObj):
	name = "pMinSetHeatFlowTempHC1"
	description = ""
	parsemap = {"val":FixedPOneDec16}
	unit = "°C"
	
class pMaxSetHeatFlowTempHC2(InformationObj):
	name = "pMaxSetHeatFlowTempHC2"
	description = ""
	parsemap = {"val":FixedPOneDec16}
	unit = "°C"
	
class pMinSetHeatFlowTempHC2(InformationObj):
	name = "pMinSetHeatFlowTempHC2"
	description = ""
	parsemap = {"val":FixedPOneDec16}
	unit = "°C"
	
class pMaxHeatFlowTemp(InformationObj):
	name = "pMaxHeatFlowTemp"
	description = ""
	parsemap = {"val":FixedPOneDec16}
	unit = "°C"
	
class p21Hyst1(InformationObj):
	name = "p21Hyst1"
	description = ""
	parsemap = {"val":FixedPOneDec8}
	unit = "K"
	
class p22Hyst2(InformationObj):
	name = "p22Hyst2"
	description = ""
	parsemap = {"val":FixedPOneDec8}
	unit = "K"
	
class p23Hyst3(InformationObj):
	name = "p23Hyst3"
	description = ""
	parsemap = {"val":FixedPOneDec8}
	unit = "K"
	
class p24Hyst4(InformationObj):
	name = "p21Hyst4"
	description = ""
	parsemap = {"val":FixedPOneDec8}
	unit = "K"
	
class p25Hyst5(InformationObj):
	name = "p22Hyst5"
	description = ""
	parsemap = {"val":FixedPOneDec8}
	unit = "K"
	
class p26Hyst6(InformationObj):
	name = "p23Hyst6"
	description = ""
	parsemap = {"val":FixedPOneDec8}
	unit = "K"
	
class p27Hyst7(InformationObj):
	name = "p23Hyst7"
	description = ""
	parsemap = {"val":FixedPOneDec8}
	unit = "K"

class p28Hyst8(InformationObj):
	name = "p23Hyst8"
	description = ""
	parsemap = {"val":FixedPOneDec8}
	unit = "K"
	
class p29HystAsymmetry(InformationObj):
	name = "p29HystAsymmetry"
	description = ""
	parsemap = {"val":"uint:8"}
	unit = "K"
	
class p30integralComponent(InformationObj):
	name = "p30integralComponent"
	description = ""
	parsemap = {"val":FixedPOneDec16}
	
class p31MaxBoostStages(InformationObj):
	name = "p31MaxBoostStages"
	description = ""
	parsemap = {"val":"uint:8"}

class p32HystDHW(InformationObj):
	name = "p32HystDHW"
	description = ""
	parsemap = {"val":FixedPOneDec8}
	unit = "K"
	
class p33BoosterTimeoutDHW(InformationObj):
	name = "p33BoosterTimeoutDHW"
	description = ""
	parsemap = {"val":"uint:8"}
	unit = "min"
	
class p34TempLimitBoostDHW(InformationObj):
	name = "p34TempLimitBoostDHW"
	description = ""
	parsemap = {"val":FixedPOneDec16}
	unit = ""
	
class p35PasteurisationInterval(InformationObj):
	name = "p35PasteurisationInterval"
	description = ""
	parsemap = {"val":"uint:8"}
	unit = ""
	
class p36MaxDurationDHWLoad(InformationObj):
	name = "p36MaxDurationDHWLoad"
	description = ""
	parsemap = {"val":"uint:8"}
	unit = ""
	
class pPasteurisationTemp(InformationObj):
	name = "pPasteurisationTemp"
	description = ""
	parsemap = {"val":"uint:16"}
	unit = "°C"
	
class pMaxBoostStagesDHW(InformationObj):
	name = "pMaxBoostStagesDHW"
	description = ""
	parsemap = {"val":"uint:8"}

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
	
class pUpTempLimitDefrostEvaporatorEnd(InformationObj):
	name = "pUpTempLimitDefrostEvaporatorEnd"
	description = ""
	parsemap = {"val":"uint:16"}
	
class pMaxTimeDefrostEvaporator(InformationObj):
	name = "pMaxTimeDefrostEvaporator"
	description = ""
	parsemap = {"val":"uint:16"}
	
class pLimitTempCondenserElectBoost(InformationObj):
	name = "pLimitTempCondenserElectBoost"
	description = ""
	parsemap = {"val":"uint:16"}
	
class pLimitTempCondenserDefrostTerm(InformationObj):
	name = "pLimitTempCondenserDefrostTerm"
	description = ""
	parsemap = {"val":"uint:16"}
	
class p47CompressorRestartDelay(InformationObj):
	name = "p47CompressorRestartDelay"
	description = ""
	parsemap = {"val":"uint:8"}
	unit = "min"
	
class p48MainFanSpeed(InformationObj):
	name = "p48MainFanSpeed"
	description = ""
	parsemap = {"val":"uint:8"}
	unit = "%"
	
class pMaxDefrostDurationAAExchanger(InformationObj):
	name = "pMaxDefrostDurationAAExchanger"
	description = ""
	parsemap = {"val":"uint:8"}
	
class pDefrostStartThreshold(InformationObj):
	name = "pDefrostStartThreshold"
	description = ""
	parsemap = {"val":"uint:16"}
	
class pVolumeFlowFilterReplacement(InformationObj):
	name = "pVolumeFlowFilterReplacement"
	description = ""
	parsemap = {"val":"uint:16"}
	
class p49SummerModeTemp(InformationObj):
	name = "p49SummerModeTemp"
	description = ""
	parsemap = {"val":FixedPOneDec16}
	unit = "°C"
	
class p50SummerModeHysteresis(InformationObj):
	name = "p50SummerModeHysteresis"
	description = ""
	parsemap = {"val":FixedPOneDec16}
	unit = "K"
	
class p54MinPumpCycles(InformationObj):
	name = "p54MinPumpCycles"
	description = ""
	parsemap = {"val":"uint:8"}
	
class p55MaxPumpCycles(InformationObj):
	name = "p55MaxPumpCycles"
	description = ""
	parsemap = {"val":"uint:16"}
	
class p56OutTempMaxPumpCycles(InformationObj):
	name = "p56OutTempMaxPumpCycles"
	description = ""
	parsemap = {"val":"uint:16"}
	
class p57OutTempMinPumpCycles(InformationObj):
	name = "p57OutTempMinPumpCycles"
	description = ""
	parsemap = {"val":"uint:16"}
	
class p58SuppressTempCaptPumpStart(InformationObj):
	name = "p58SuppressTempCaptPumpStart"
	description = ""
	parsemap = {"val":"uint:16"}
	
class p59RestartBeforeSetbackEnd(InformationObj):
	name = "p59RestartBeforeSetbackEnd"
	description = ""
	parsemap = {"val":FixedPOneDec16}
	
class p70StartDryHeat(InformationObj):
	name = "p70StartDryHeat"
	description = ""
	parsemap = {"val":"uint:8"}
	
class p71BaseTemp(InformationObj):
	name = "p71BaseTemp"
	description = ""
	parsemap = {"val":FixedPOneDec16}
	unit = "°C"
	
class p72PeakTemp(InformationObj):
	name = "p72PeakTemp"
	description = ""
	parsemap = {"val":FixedPOneDec16}
	unit = "°C"
	
class p73TempDuration(InformationObj):
	name = "p73TempDuration"
	description = ""
	parsemap = {"val":"uint:16"}
	
class p74TempIncrease(InformationObj):
	name = "p74TempIncrease"
	description = ""
	parsemap = {"val":FixedPOneDec16}
	
class p75PassiveCooling(InformationObj):
	name = "p75PassiveCooling"
	description = ""
	parsemap = {"val":"uint:16"}
	
class p77OutTempFilterTime(InformationObj):
	name = "p77OutTempFilterTime"
	description = ""
	parsemap = {"val":FixedPOneDec16}
	
class p78DualModePoint(InformationObj):
	name = "p78DualModePoint"
	description = ""
	parsemap = {"val":FixedPOneDec16}
	
class p79BoosterTimeoutHC(InformationObj):
	name = "p79BoosterTimeoutHC"
	description = ""
	parsemap = {"val":"uint:8"}	 
	
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

class pProgHC1StartTime(InformationObj):
	name = "pProgHC1StartTime"
	description = ""
	parsemap = {"val":Time16}
	
class pProgHC1EndTime(InformationObj):
	name = "pProgHC1EndTime"
	description = ""
	parsemap = {"val":Time16}
	
class pProgHC1Sunday(InformationObj):
	name = "pProgHC1Sunday"
	description = ""
	parsemap = {"val":"bool"}
	
class pProgHC1Saturday(InformationObj):
	name = "pProgHC1Saturday"
	description = ""
	parsemap = {"val":"bool"}
	
class pProgHC1Friday(InformationObj):
	name = "pProgHC1Friday"
	description = ""
	parsemap = {"val":"bool"}
	
class pProgHC1Thursday(InformationObj):
	name = "pProgHC1Thursday"
	description = ""
	parsemap = {"val":"bool"}
	
class pProgHC1Wednesday(InformationObj):
	name = "pProgHC1Wednesday"
	description = ""
	parsemap = {"val":"bool"}
	
class pProgHC1Tuesday(InformationObj):
	name = "pProgHC1Tuesday"
	description = ""
	parsemap = {"val":"bool"}
	
class pProgHC1Monday(InformationObj):
	name = "pProgHC1Monday"
	description = ""
	parsemap = {"val":"bool"}
	
class pProgHC1Enable(InformationObj):
	name = "pProgHC1Enable"
	description = ""
	parsemap = {"val":"uint:8"}
	
class pProgHC2StartTime(InformationObj):
	name = "pProgHC2StartTime"
	description = ""
	parsemap = {"val":Time16}
	
class pProgHC2EndTime(InformationObj):
	name = "pProgHC2EndTime"
	description = ""
	parsemap = {"val":Time16}
	
class pProgHC2Sunday(InformationObj):
	name = "pProgHC2Sunday"
	description = ""
	parsemap = {"val":"bool"}
	
class pProgHC2Saturday(InformationObj):
	name = "pProgHC2Saturday"
	description = ""
	parsemap = {"val":"bool"}
	
class pProgHC2Friday(InformationObj):
	name = "pProgHC2Friday"
	description = ""
	parsemap = {"val":"bool"}
	
class pProgHC2Thursday(InformationObj):
	name = "pProgHC2Thursday"
	description = ""
	parsemap = {"val":"bool"}
	
class pProgHC2Wednesday(InformationObj):
	name = "pProgHC2Wednesday"
	description = ""
	parsemap = {"val":"bool"}
	
class pProgHC2Tuesday(InformationObj):
	name = "pProgHC2Tuesday"
	description = ""
	parsemap = {"val":"bool"}
	
class pProgHC2Monday(InformationObj):
	name = "pProgHC2Monday"
	description = ""
	parsemap = {"val":"bool"}
	
class pProgHC2Enable(InformationObj):
	name = "pProgHC2Enable"
	description = ""
	parsemap = {"val":"uint:8"}
	
class pProgDHWStartTime(InformationObj):
	name = "pProgDHWStartTime"
	description = ""
	parsemap = {"val":Time16}
	
class pProgDHWEndTime(InformationObj):
	name = "pProgDHWEndTime"
	description = ""
	parsemap = {"val":Time16}
	
class pProgDHWSunday(InformationObj):
	name = "pProgDHWSunday"
	description = ""
	parsemap = {"val":"bool"}
	
class pProgDHWSaturday(InformationObj):
	name = "pProgDHWSaturday"
	description = ""
	parsemap = {"val":"bool"}
	
class pProgDHWFriday(InformationObj):
	name = "pProgDHWFriday"
	description = ""
	parsemap = {"val":"bool"}
	
class pProgDHWThursday(InformationObj):
	name = "pProgDHWThursday"
	description = ""
	parsemap = {"val":"bool"}
	
class pProgDHWWednesday(InformationObj):
	name = "pProgDHWWednesday"
	description = ""
	parsemap = {"val":"bool"}
	
class pProgDHWTuesday(InformationObj):
	name = "pProgDHWTuesday"
	description = ""
	parsemap = {"val":"bool"}
	
class pProgDHWMonday(InformationObj):
	name = "pProgDHWMonday"
	description = ""
	parsemap = {"val":"bool"}
	
class pProgDHWEnable(InformationObj):
	name = "pProgDHWEnable"
	description = ""
	parsemap = {"val":"uint:8"}
	
class pProgFan1StartTime(InformationObj):
	name = "pProgFan1StartTime"
	description = ""
	parsemap = {"val":Time16}
	
class pProgFan1EndTime(InformationObj):
	name = "pProgFan1EndTime"
	description = ""
	parsemap = {"val":Time16}
	
class pProgFan1Sunday(InformationObj):
	name = "pProgFan1Sunday"
	description = ""
	parsemap = {"val":"bool"}
	
class pProgFan1Saturday(InformationObj):
	name = "pProgFan1Saturday"
	description = ""
	parsemap = {"val":"bool"}
	
class pProgFan1Friday(InformationObj):
	name = "pProgFan1Friday"
	description = ""
	parsemap = {"val":"bool"}
	
class pProgFan1Thursday(InformationObj):
	name = "pProgFan1Thursday"
	description = ""
	parsemap = {"val":"bool"}
	
class pProgFan1Wednesday(InformationObj):
	name = "pProgFan1Wednesday"
	description = ""
	parsemap = {"val":"bool"}
	
class pProgFan1Tuesday(InformationObj):
	name = "pProgFan1Tuesday"
	description = ""
	parsemap = {"val":"bool"}
	
class pProgFan1Monday(InformationObj):
	name = "pProgFan1Monday"
	description = ""
	parsemap = {"val":"bool"}
	
class pProgFan1Enable(InformationObj):
	name = "pProgFan1Enable"
	description = ""
	parsemap = {"val":"uint:8"}
	
class pProgFan2StartTime(InformationObj):
	name = "pProgFan2StartTime"
	description = ""
	parsemap = {"val":Time16}
	
class pProgFan2EndTime(InformationObj):
	name = "pProgFan2EndTime"
	description = ""
	parsemap = {"val":Time16}
	
class pProgFan2Sunday(InformationObj):
	name = "pProgFan2Sunday"
	description = ""
	parsemap = {"val":"bool"}
	
class pProgFan2Saturday(InformationObj):
	name = "pProgFan2Saturday"
	description = ""
	parsemap = {"val":"bool"}
	
class pProgFan2Friday(InformationObj):
	name = "pProgFan2Friday"
	description = ""
	parsemap = {"val":"bool"}
	
class pProgFan2Thursday(InformationObj):
	name = "pProgFan2Thursday"
	description = ""
	parsemap = {"val":"bool"}
	
class pProgFan2Wednesday(InformationObj):
	name = "pProgFan2Wednesday"
	description = ""
	parsemap = {"val":"bool"}
	
class pProgFan2Tuesday(InformationObj):
	name = "pProgFan2Tuesday"
	description = ""
	parsemap = {"val":"bool"}
	
class pProgFan2Monday(InformationObj):
	name = "pProgFan2Monday"
	description = ""
	parsemap = {"val":"bool"}
	
class pProgFan2Enable(InformationObj):
	name = "pProgFan2Enable"
	description = ""
	parsemap = {"val":"uint:8"}
