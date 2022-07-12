from MDT_COMMAND_LIB import *
import time
import pyvisa

baud = 115200
timeout = 3


devices = mdtListDevices()
serial = devices[0][0]
# print(serial)

def run():

    connect()

    userinput = input("Enter command: ")
    while len(userinput) != 0:

        if userinput.lower() == "connect":
            connect()

        elif userinput.lower() == "disconnect":
            disconnect()

        elif userinput.lower() == "setZ":
            xvoltage = input("Voltage: ")
            check_num(xvoltage)

        elif userinput.lower() == "sety":
            yvoltage = input("Voltage: ")
            check_num(yvoltage)
        
        elif userinput.lower() == "setz":
            zvoltage = input("Voltage: ")
            check_num(zvoltage)         

        else:
            print("Not a recognized command")

        userinput = input("Enter command: ")

def connect():
    global hdl 
    hdl = mdtOpen(serial, baud, timeout)
    openstatus = mdtIsOpen(serial)
    if openstatus == 1:
        print(f"Device {serial} connected successfully")
    else:
        print("Device not connected")
    print(f"hdl = {hdl}")

def disconnect():
    result = mdtClose(hdl)
    if result == 0:
        print(f"Device {serial} disconnected successfully")
    else:
        print(f"Device {serial} disconnection failed")

def isconnected():
    openstatus = mdtIsOpen(serial)
    if openstatus == 1:
        print(f"Device {serial} connected successfully")
    else:
        print("Device not connected")

def setX(voltage):
    result = mdtSetXAxisVoltage(hdl, voltage)
    if result == 0:
        print(f"X-axis set to {voltage} volts")
    else:
        print("unsuccessful")

def setY(voltage):
    result = mdtSetYAxisVoltage(hdl, voltage)
    if result == 0:
        print(f"Y-axis set to {voltage} volts")
    else:
        print("unsuccessful")

def setZ(voltage):
    result = mdtSetZAxisVoltage(hdl, voltage)
    if result == 0:
        print(f"Z-axis set to {voltage} volts")
    else:
        print("unsuccessful")


def getX():
    xvoltage = [0]
    result = mdtGetXAxisVoltage(hdl, xvoltage)
    if result == 0:
        return(xvoltage[0])
    else:
        print("no no no")

def getY():
    yvoltage = [0]
    result = mdtGetYAxisVoltage(hdl, yvoltage)
    if result == 0:
        return(yvoltage[0])
    else:
        print("no no no")

def getZ():
    zvoltage = [0]
    result = mdtGetZAxisVoltage(hdl, zvoltage)
    if result == 0:
        return(zvoltage[0])
    else:
        print("no no no")


def check_num(number):
    try:
        float(number)
    except:
        print("Input is not a number")



# ---------------------------------------------------------------------------------------




# if __name__ == "__main__":
#     run(scan(0,0,10,10,1))

