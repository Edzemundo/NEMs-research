from MDT import *
import time

zrecord = open("zrecord.txt", "a")

connect()
voltage = 0.00

for i in range(0, 10001): 
    setZ(voltage)
    time.sleep(1)
    result = getZ()
    zrecord.write(f"{voltage},{result}\n")
    voltage = voltage + 0.01

disconnect()
