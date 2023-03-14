"""scan.py
Author: Edmund S. Agyekum

This program is meant to control both the open-loop piezo-controller and the digital multimeter to undergo
image scanning of the sample.

Program now also supports making the image of the file directly after scanning.

"""

import time
import VISA
import datetime
from MDT import *
from VISA import *
from imaging import *



def run():
    """Used to assign and run various commands
    """
    connect()
    userinput = input("Enter command: ")

    while len(userinput) != 0:

        if userinput.lower() == "scan":
            startz = float(input("Initial z voltage: "))
            # check_num(startz)
            print(f"Initial z voltage = {startz} volts")
            starty = float(input("Initial y voltage: "))
            # check_num(starty)
            print(f"Initial y voltage = {starty} volts")
            stopz = float(input("Final z voltage: "))
            # check_num(stopz)
            print(f"Final z voltage = {stopz} volts")
            stopy = float(input("Final y voltage: "))
            # check_num(stopy)
            print(f"Final y voltage = {stopy} volts")
            step = float(input("Step voltage: "))
            # check_num(step)
            print(f"Step voltage = {step} volts")
            scan(startz, starty, stopz, stopy, step)
            secondinput = input("Would you like to create an image from txt/csv file?:")
            if secondinput.lower() == "yes" or "y" or "yeah" or "roger roger":
                imagify(filename)
        
        elif userinput.lower() == "scan2":
            startz = float(input("Initial z voltage: "))
            # check_num(startz)
            print(f"Initial z voltage = {startz} volts")
            starty = float(input("Initial y voltage: "))
            # check_num(starty)
            print(f"Initial y voltage = {starty} volts")
            stopz = float(input("Final z voltage: "))
            # check_num(stopz)
            print(f"Final z voltage = {stopz} volts")
            stopy = float(input("Final y voltage: "))
            # check_num(stopy)
            print(f"Final y voltage = {stopy} volts")
            step = float(input("Step voltage: "))
            # check_num(step)
            print(f"Step voltage = {step} volts")
            scan2(startz, starty, stopz, stopy, step)
            secondinput = input("Would you like to create an image from txt/csv file?:")
            if secondinput.lower() == "yes" or "y" or "yeah" or "roger roger":
                imagify(filename)
        
        elif userinput.lower() == "disconnect":
            disconnect()
        
        else:
            print("Command not recognized")
        
        userinput = input("Enter command: ")




def scan(startz, starty, stopz, stopy, step):
    """scans and records
    """

    global filename
    filename = input("filename: ")
        
    start_time = time.time()
    zvoltage = startz
    yvoltage = starty
    
    time.sleep(0.5)
    stepz = int(((stopz - startz) / step))
    stepy = int(((stopy - starty) / step))

    # print(f"stepy = {stepy}")
    for y in range(stepy):
        if yvoltage <= stopy:
            setY(yvoltage)
            # print(f"y = {yvoltage}")
            time.sleep(0.1)
            
            for up in range(stepz):
                setZ(zvoltage)
                # print(f"z = {zvoltage}")
                time.sleep(0.1)
                measured_v = measure_dcv()
                chart(zvoltage, yvoltage, measured_v)
                zvoltage += step
            setZ(zvoltage)
            time.sleep(0.1)
            measured_v = measure_dcv()
            chart(zvoltage, yvoltage, measured_v)
            yvoltage += step
            setY(yvoltage)
            for down in range(stepz):
                setZ(zvoltage)
                # print(f"z = {zvoltage}")
                time.sleep(0.1)
                measured_v = measure_dcv()
                chart(zvoltage, yvoltage, measured_v)
                zvoltage -= step
            setZ(zvoltage)
            time.sleep(0.1)
            measured_v = measure_dcv()
            chart(zvoltage, yvoltage, measured_v)
            yvoltage += step
        
        else:
            file.close

        

    end_time = time.time()
    total_time = end_time - start_time
    time_elapsed = str(datetime.timedelta(seconds = total_time))
    print(f"time = {time_elapsed} hours")


def scan2(startz, starty, stopz, stopy, step, namedfile):

    global filename
    filename = f"{namedfile}.csv"
    
    start_time = time.time()
    zvoltage = startz
    yvoltage = starty
    time.sleep(0.5)
    stepz = int(((stopz - startz) / step))
    stepy = int(((stopy - starty) / step))
    # print(f"stepy = {stepy}")
    for y in range(stepy + 1):
        setY(yvoltage)
        print(f"y = {yvoltage}")
        time.sleep(0.1)
        
        for up in range(0, stepz + 1):
            setZ(zvoltage)
            print(f"z = {zvoltage}")
            time.sleep(0.1)
            measured_v = measure_dcv()
            chart(zvoltage, yvoltage, measured_v)
            zvoltage += step
        
        if yvoltage <= stopy:
            yvoltage += step
            zvoltage = startz
            setZ(zvoltage)
            setY(yvoltage)
            print(f"z = {zvoltage}")
            time.sleep(0.3)
            # measured_v = measure_dcv()
            # chart(zvoltage, yvoltage, measured_v)


    end_time = time.time()
    total_time = end_time - start_time
    time_elapsed = str(datetime.timedelta(seconds = total_time))
    print(f"time = {time_elapsed} hours")


def chart(x_value, y_value, z_value):
    """Creates and appends a text csv file with position and value of voltage"""
    global file
    file = open(f"{filename}", "a")
    file.write(f"{x_value},{y_value},{z_value}\n")
    file.close()


def check_num(number):
    """Checks if input is a number"""
    try:
        float(number)
    except:
        print("Input is not a number")

if __name__ == "__main__":
    run()
