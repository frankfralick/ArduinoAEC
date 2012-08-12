"""
Python 2.7
Frank Fralick

This example code illustrates how to access values sent from Arduino over 
serial port within a Rhino Python script.  
"""

import rhinoscriptsyntax as rs
import scriptcontext as rsc
import serial
import sys
sys.path.append("C:\\Python27\\Lib\\site-packages\\")

"""
GetObjectGrip will ask the user to select a grip. There are other ways to 
do this, which would be better if you want to control many objects with the values 
from many sensors.   
""" 
handle = rs.GetObjectGrip()

"""
This creates a variable that will be the access point to the serial port.  The
first argument specifies which COM port the device is connected to.  You can 
just trial and error this.  The second argument is the baud rate that the 
Arduino was programmed to transmit at.  
"""
ser = serial.Serial(1,9600)
iterations = 1000
i=0
while True:
    if i<iterations:
        reading = ser.readline()
        readingList = reading.split()
        value = float(readingList[5])
        """
        In this example the z value of the grip will be modified. The value 
        of modifier is just a number that will scale the value being passed 
        from the Arduino to be something that looks more reasonable.
        """        
        modifier = 50
        """
        This methodology can  be applied to any objects that have grips, or 
        simply to an objects location.
        """
        rs.ObjectGripLocation(handle[0], 0, (0,0,value/modifier))
        rs.Redraw()
    else:
        break
    i+=1

