import time

startz = 0.00
starty = 0.00 
stopz = 5.00 
stopy = 5.00 
step = 1

start_time = time.time()
zvoltage = startz
yvoltage = starty
# setZ(startz)
# setY(starty)
time.sleep(0.5)
stepz = int(((stopz - startz) / step))
stepy = int(((stopy - starty) / step))
# print(f"stepy = {stepy}")
for y in range(stepy):
    # setY(yvoltage)
    print(f"y = {yvoltage}")
    time.sleep(0.1)
    
    for up in range(0, stepz):
        # setZ(zvoltage)
        print(f"z = {zvoltage}")
        time.sleep(0.1)
        # measured_v = measure_dcv()
        # chart(zvoltage, yvoltage, measured_v)
        zvoltage += step
    yvoltage += step
    # setZ(zvoltage)
    # setY(yvoltage)
    print(f"z = {zvoltage}")
    print(f"y = {yvoltage}")
    time.sleep(0.1)
    # measured_v = measure_dcv()
    # chart(zvoltage, yvoltage, measured_v)

    for down in range(0, stepz):
        # setZ(zvoltage)
        print(f"z = {zvoltage}")
        time.sleep(0.1)
        # measured_v = measure_dcv()
        # chart(zvoltage, yvoltage, measured_v)
        zvoltage -= step
    yvoltage += step
    # setZ(zvoltage)
    print(f"z = {zvoltage}")
    time.sleep(0.1)
    # measured_v = measure_dcv()
    # chart(zvoltage, yvoltage, measured_v)

end_time = time.time()
total_time = end_time - start_time
print(f"time = {total_time} seconds")
