# -*- coding: utf-8 -*-
"""
Created on Wed Sep 26 16:06:18 2018

@author: nitingera
"""

def fToC(fahrTemp):
    return (fahrTemp - 32) / 1.8

def cToF(celsTemp):
    return (celsTemp * 1.8) + 32

#print(cToF(0))

#print(fToC(212))

def Temperatureconvert(temp, temp_type):
    final_temp = 0
    if(temp_type == "C"):
        final_temp = (temp * 1.8) + 32
    elif(temp_type == "F"):
        final_temp = (temp - 32) / 1.8
    
    return final_temp
    
print(Temperatureconvert(0, "C"))
print(Temperatureconvert(212, "F"))