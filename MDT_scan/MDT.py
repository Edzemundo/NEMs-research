
"""MDT.py
Author: Edmund Agyekum

This program is meant to simplify the commands provided by the MDT_COMMAND_LIB to make using the library easier.
A "wrapper" if you will...
It also initially connects to the first MDT device it recognizes

"""



from MDT_COMMAND_LIB import * # Library supplied by Thorlabs
import time #used for time delays during scanning
import pyvisa #pure python implementation of VISA

# the following 2 values can be found in the original library documentation from Thorlabs
baud = 115200
timeout = 3

"""Programs initially selects the first device provided by the mdtlistdevices function
Note: this will need to be edited if multiple mdt devices are being used by the same computer running the program
"""
devices = mdtListDevices()
serial = devices[0][0]
# print(serial)


def run():
	"""connects to the device then requests a command
	
		Args:
			None
			
		Commands:
			connect - connects to device (useful if device did not connect automatically)
			disconnect - disconnect device (useful for troubleshooting)
			setx - asks for and sets the x-axis voltage
			sety - asks for and sets the y-axis voltage
			setz - asks for and sets the z-axis voltage
	"""

    connect()

    userinput = input("Enter command: ")
    while len(userinput) != 0:

        if userinput.lower() == "connect":
            connect()

        elif userinput.lower() == "disconnect":
            disconnect()

        elif userinput.lower() == "setx":
            xvoltage = input("Voltage: ")
            check_num(xvoltage)
            setX(xvoltage)

        elif userinput.lower() == "sety":
            yvoltage = input("Voltage: ")
            check_num(yvoltage)
            setY(yvoltage)
        
        elif userinput.lower() == "setz":
            zvoltage = input("Voltage: ")
            check_num(zvoltage)   
            setZ(zvoltage)      

        else:
            print("Not a recognized command")

        userinput = input("Enter command: ")

def connect():
	# connects to first listed device
    global hdl 
    hdl = mdtOpen(serial, baud, timeout)
    openstatus = mdtIsOpen(serial)
    if openstatus == 1:
        print(f"Device {serial} connected successfully")
    else:
        print("Device not connected")
    print(f"hdl = {hdl}")

def disconnect():
	# disconnects connected device
    result = mdtClose(hdl)
    if result == 0:
        print(f"Device {serial} disconnected successfully")
    else:
        print(f"Device {serial} disconnection failed")

def isconnected():
	# queries if device is connected
    openstatus = mdtIsOpen(serial)
    if openstatus == 1:
        print(f"Device {serial} connected successfully")
    else:
        print("Device not connected")

def setX(voltage):
	# sets x voltage
    result = mdtSetXAxisVoltage(hdl, voltage)
    if result == 0:
        print(f"X-axis set to {voltage} volts")
    else:
        print("unsuccessful")

def setY(voltage):
	# sets y voltage
    result = mdtSetYAxisVoltage(hdl, voltage)
    if result == 0:
        print(f"Y-axis set to {voltage} volts")
    else:
        print("unsuccessful")

def setZ(voltage):
	# sets z voltage
    result = mdtSetZAxisVoltage(hdl, voltage)
    if result == 0:
        print(f"Z-axis set to {voltage} volts")
    else:
        print("unsuccessful")


def getX():
	# requests x voltage
    xvoltage = [0]
    result = mdtGetXAxisVoltage(hdl, xvoltage)
    if result == 0:
        return(xvoltage[0])
    else:
        print("no no no")

def getY():
	# requests y voltage
    yvoltage = [0]
    result = mdtGetYAxisVoltage(hdl, yvoltage)
    if result == 0:
        return(yvoltage[0])
    else:
        print("no no no")

def getZ():
	# requests z voltage
    zvoltage = [0]
    result = mdtGetZAxisVoltage(hdl, zvoltage)
    if result == 0:
        return(zvoltage[0])
    else:
        print("no no no")


def check_num(number):
	# checks if input value is a number
    try:
        float(number)
    except:
        print("Input is not a number")



# ---------------------------------------------------------------------------------------



#the following lines are test code to check if the program is functional. It is run in the command line.
# if __name__ == "__main__":
#     run(scan(0,0,10,10,1))

