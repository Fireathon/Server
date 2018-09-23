#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# Input Variable factors and Weights
def InputSpansWeights():
    
    # Input Spans
    iCPRiskSpan = [1,2,3,4,5]
    iTempSpan = [0,10,20,25,35]
    fWindSpeedSpan = [0,4,8,16,24]
    fHumiditySpan = [100,70,55,40,30]
    fPressureSpan = [1013,95,700,550,400]
    fCloudSpan = [0,20,40,60,80]
    iSkySpan = [0,0,0.5,1,1]
    iPointSpan = [0,0,0,1,1]
    
    dSpans = {'iCPRisk' : iCPRiskSpan , 'iTemp': iTempSpan, 'fWindSpeed' : fWindSpeedSpan, 
                'fHumidity': fHumiditySpan, 'fPressure': fPressureSpan, 'fCloud': fCloudSpan,
                'iSky': iSkySpan, 'iPoint':iPointSpan}
    
    # Input Weights
    dWeights = {'iCPRisk' : 5 , 'iTemp' : 3 , 'fWindSpeed' : 3, 
                'fHumidity': 1, 'fPressure': 1, 'fCloud': 1,
                'iSky': 3, 'iPoint':4}
    
    return dSpans, dWeights

# Find Variable Risk Level
def FindRiskLevel(dSpans,dWeights,iCPRisk,iTemp,fWindSpeed,fHumidity,fPressure,fCloud,iSky,iPoint):
    # Risk, Temp, WindSpeed, Cloud
    dRiskLevel = {'iCPRisk' : 1 , 'iTemp' : 1 , 'fWindSpeed' : 1, 
        'fHumidity': 1, 'fPressure': 1, 'fCloud': 1,
        'iSky': 1, 'iPoint':1}
    
    dValues = {'iCPRisk' : iCPRisk , 'iTemp': iTemp, 'fWindSpeed' : fWindSpeed, 
            'fHumidity': fHumidity, 'fPressure': fPressure, 'fCloud': fCloud,
            'iSky': iSky, 'iPoint':iPoint}

# Spanning Upwards
    lUpwards = ['iCPRisk' , 'iTemp', 'fWindSpeed', 'fCloud']
    for data in lUpwards:
        for i in range (0,3):
            templist = dSpans[data]
            if templist[i]<= dValues[data] < templist[i+1]:
                dRiskLevel[data] = i+1
            elif dValues[data] >=templist[4]:
                dRiskLevel[data] = 5
        print (dRiskLevel[data])
        
# Spanning Downwards
    lDownwards = ['fHumidity' , 'fPressure']
    for data in lDownwards:
        for i in range (0,3):
            templist = dSpans[data]
            if templist[i]>= dValues[data] > templist[i+1]:
                dRiskLevel[data] = i+1
            elif dValues[data] <= templist[4]:
                dRiskLevel[data] = 5
        print (dRiskLevel[data])   
        
# Categorical Values
    dSky = {0:1,0.5:3,1:5}
    dPoint = {0:1,1:4}
    dRiskLevel['iSky'] = dSky [dValues['iSky']]
    dRiskLevel['iPoint'] = dPoint [dValues['iPoint']]
    
    return dValues,dRiskLevel

# Agreegate and Calculate Refined Risk Level


def CalcRefinedRiskLevel(dRiskLevel,dWeights):
    
    fRisk = (sum(dRiskLevel[k]*(dWeights[k]-1) for k in dRiskLevel))/9.66667
    iRisk = round(fRisk)
    iRisk = max(min(iRisk,5),0)
    
    return fRisk, iRisk

        
    
                    
                    
iCPRisk = 3
iTemp = 25
fWindSpeed = 8
fHumidity = 50
fPressure = 1013
fCloud = 50
iSky = 0.5
iPoint = 0


dSpans, dWeights = InputSpansWeights()
dValues, dRiskLevel = FindRiskLevel(dSpans,dWeights,iCPRisk,iTemp,fWindSpeed,
                                    fHumidity,fPressure,fCloud,iSky,iPoint)
fRisk, iRisk = CalcRefinedRiskLevel(dRiskLevel,dWeights)





 