from PIL import Image
import numpy as np
import os

row = 5
column = 5

max_voltage = float("-inf")
min_voltage = float("inf")
max_y = 0
max_x = 0

with open(os.path.join(os.getcwd(), "trial29.txt"), "r") as file:
    lines = file.readlines()
    

    for line in lines:
        elements = line.split(",")
        # print(elements)
        if float(elements[2]) > max_voltage:
            max_voltage = float(elements[2])
        elif float(elements[2]) < min_voltage:
            min_voltage = float(elements[2])
        if int(elements[0]) > max_x:
            max_x = int(elements[0])
        if int(elements[1]) > max_y:
            max_y = int(elements[1])
    
    max_x += 1
    max_y += 1

    arr = np.zeros((max_y, max_x), np.int64)
    print(max_x)
    print(max_y)

    for line in lines:
        elements = line.split(",")
        # print(elements)
        voltage = float(elements[2])
        value = int(abs(((voltage - min_voltage) / (max_voltage - min_voltage))) * 255)
        arr[int(elements[1]), int(elements[0])] = value


img = Image.fromarray(arr, "L")

img.show()
# print(arr)

# np.savetxt("img.txt", arr)