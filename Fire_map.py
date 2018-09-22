#!/usr/bin/env python3
# -*- coding: utf-8 -*
# Let the game begin!

# https://www.civilprotection.gr/sites/default/gscp_uploads/180923.jpg

from PIL import Image
import requests
from io import BytesIO

# Find and download image

def getPPImage():
    response = requests.get('https://www.civilprotection.gr/sites/default/gscp_uploads/180904.jpg')
    img = Image.open(BytesIO(response.content))
    return img

# Get colour from pixels

# Get geo-coord
# Move to the PP map, and esp to the origin (10,95) pixels of the img
# When we move (30.0116 - 19.1162)*scaleX = 810-10 => scaleX = 800/(10.9)
# When we move (41.89614 - 34.4432)*scaleY = (805-95) => scaleY = 710/(7.42)

# imgRight=1052
# imgLeft=556
# imgBottom=693
# imgTop=263
# geoRight = 30.0146
# geoLeft = 19.1162
# geoBottom = 34.4432
# geoTop = 41.8614
    

def getRiskLevelForGeoCoords(geoX, geoY):
    # Get image
    ppImg = getPPImage()
    imgX, imgY = getPixelForCoords(geoX, geoY)
    # Get pixel RGB value for corresponding imgX, imgY
    colorRGB = ppImg.getpixel((imgX, imgY))
    # Convert pixel RBG to risk level
    
    return getRiskLevelForColor(colorRGB)

def getRGBComponentsFrom(cCandidate):
        rValue = round(cCandidate / 0x10000)
        gValue = round((cCandidate % 0x10000) / 0x100)
        bValue = (cCandidate % 0x100)
        return (rValue, gValue, bValue)
    
def getRiskLevelForColor(colorRGBValue):
    redValuesToRiskLevel = [(171,254,162), (168,200,238), (250,255,8), (251,174,0), (250,3,0)]
    selectedCandidate = -1
    bestMatch = 0xffffff
    for cCandidate in redValuesToRiskLevel:
        (candR, candG, candB) = cCandidate
        colorR, colorG, colorB = colorRGBValue
        candRDiff = abs(candR - colorR)
        candGDiff = abs(candG - colorG)
        candBDiff = abs(candB - colorB)
        
        candDiff = (candRDiff**2 + candGDiff**2 + candBDiff**2)**(1/2)
        if candDiff < bestMatch:
            selectedCandidate = cCandidate
            bestMatch = candDiff
            
    # At this point we have the best match
    return redValuesToRiskLevel.index(selectedCandidate) + 1


def getPixelForCoords(geoX, geoY):
    imgX = 10 + (800/10.9) * (geoX - 19.1162)
    imgY = 95 + (710/7.42) * (41.8614 - geoY)
    return (imgX, imgY)

geoX=21.781894
geoY=36.919710

RiskLevel = getRiskLevelForGeoCoords(geoX, geoY)
print (RiskLevel)

 
        

