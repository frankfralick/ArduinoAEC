'''
Python 2.7.2
Frank Fralick

Script for reading in values from a serial port to
update the value of a parameter in an Inventor assembly.
In this example, and Arduino is running a program that takes
in voltage readings from a PV cell or other sensor and sends them to a serial
port.
'''

import sys
import os
import serial

ser = serial.Serial(2, 9600) #get access to COM3 (Arduino's port) baud rate to read is 9600

import win32com.client
from win32com.client import gencache

##Start COM client session with Inventor
oApp = win32com.client.Dispatch('Inventor.Application')
oApp.Visible=True 

#Create object "mod" that will point to the Python COM wrapper for Inventor's type library.
mod = gencache.EnsureModule('{D98A091D-3A0F-4C3E-B36E-61F62068D488}', 0, 1, 0)
#Early binding procedure to recast "oApp" as an instance of the Application class in the wrapper.
#This is a common pattern with Python COM automation. 
oApp = mod.Application(oApp) 
oAssemblyDoc=oApp.Documents.Open("C:\\MyDirectory\\MyAssemblyFile.iam")
#Early binding of the COM object of the assembly document to the AssemblyDocument class in the wrapper.
oAssemblyDoc = mod.AssemblyDocument(oAssemblyDoc)
oParams = oAssemblyDoc.ComponentDefinition.Parameters
#In this example I was modifying a louver assembly.  Modify variable names and
#parameters to change as necessary.  
louver_angle = oParams.ModelParameters.Item("d20").Value


while True:
    light = ser.readline()
    #This splits the string from serial into a list of the words.
    lightlist = light.split()
    #We then index the 5th word, which contains the value we want to use.
    lightValue = float(lightlist[5])
    if lightValue < 5:
        print lightValue;
        oParams.ModelParameters.Item("d20").Value = 0
        oAssemblyDoc.Update()
    elif 5 <= lightValue:
        #Inventor angle parameter must be passed in radians even if the parameter
        #in the user interface is shown in degrees.
        oParams.ModelParameters.Item("d20").Value = lightValue*(3.14/180)
        oAssemblyDoc.Update()
    oAssemblyDoc.Update()        

        
