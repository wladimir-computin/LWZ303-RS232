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
	unit = "°C"
	
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
	parsemap = {"val":"int:8"}
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
	parsemap = {"val":"uint:8"}
	
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
	parsemap = {"val":"uint:8"}
	
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
