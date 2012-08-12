Using Arduino with Inventor:

COM Access:

You must first know how to use Python with Inventor.  This can be done in two ways.  

Access method 1:

There is a utility called tlbimp.exe that is distributed with the Windows SDK.  Inventor 
ships with a .NET interop assembly that can be used with this utility to create a .dll that 
can be added as a reference to your IronPython program.

The example here does not use this method.

Access method 2:

Inventor has a COM automation API, which means that access from .NET is not necessary.  The PythonWin
package contains a utility called makepy that is used to create a Python wrapper for Inventor's COM type
library.  There are many examples online of how to use this utility and also much written about basic concepts
like early binding which are necessary to understand for programming COM API's with Python.

Accessing Inventor directly through COM is more suitable for this example, but either way can work.

PySerial:

You will need a package called PySerial that will handle the serial communication between the Arduino and your 
Python program. 
	