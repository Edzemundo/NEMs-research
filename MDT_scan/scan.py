import time
import VISA
from MDT import *
from VISA import *



def run():

    connect()
    startz = input("Initial x voltage: ")
    # check_num(startz)
    print(f"Initial z voltage = {startz} volts")
    starty = input("Initial y voltage: ")
    # check_num(starty)
    print(f"Initial y voltage = {starty} volts")
    stopz = input("Final x voltage: ")
    # check_num(stopz)
    print(f"Final z voltage = {stopz} volts")
    stopy = input("Final y voltage: ")
    # check_num(stopy)
    print(f"Final y voltage = {stopy} volts")
    step = input("Step voltage: ")
    # check_num(step)
    print(f"Step voltage = {step} volts")
    scan(startz, starty, stopz, stopy, step)

    exit_input = input("Press any input to exit: ")


def scan(startz, starty, stopz, stopy, step):

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
    print(f"time = {total_time} seconds")


def scan2(startz, starty, stopz, stopy, step):

    global filename
    filename = input("filename: ")
    
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
    print(f"time = {total_time} seconds")


def chart(x_value, y_value, z_value):
    global file
    file = open(f"{filename}", "a")
    file.write(f"{x_value},{y_value},{z_value}\n")
    file.close()

def check_num(number):
    try:
        float(number)
    except:
        print("Input is not a number")

if __name__ == "__main__":
    run()
