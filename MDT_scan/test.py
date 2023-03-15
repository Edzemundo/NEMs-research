"""imaging.py
Author: Edmund S. Agyekum

This program creates an image of the txt file created by the scan.py program using the Pillow library
and an array created through numpy

"""
import os
import csv
import numpy as np
from PIL import Image as im

"""creates an image of the txt file created after running scan
"""

def imagifycsv(filelocin):
    # opens txt result file from experiment
    fileloc = filelocin.replace("'","")
    with open(fileloc) as file:
        data = list(csv.reader(file, delimiter=','))

    #determine step sizes
    firstline = data[0]
    secondline = data[1]
    stepsizex = float(secondline[0]) - float(firstline[0])
    stepsizey = float(input("Y step size: "))

    # determines dimensions of array
    lastline = data[-1]
    rows = int(float(lastline[0])/stepsizex)+1
    columns = int(float(lastline[1])/stepsizey)+1

    # finding the min and max voltage values
    min = 100.0
    max = -100.0

    for elements in data:
        # element = elements.split(",")
        if float(elements[2]) < min:
            min = float(elements[2])
        if float(elements[2]) > max:
            max = float(elements[2])

    # converting to 0-255 scale and make a list of those transformed values
    valuelist = []

    ratio = lambda x : ((x-min)/(max-min))*255
    for elements in data:
        # element = elements.split(",")
        value = int(ratio(float(elements[2])))
        valuelist.append(value)

    # creating the array and picture from it and names picture after text file
    arr = np.array(valuelist)
    grid = np.reshape(arr, (rows,columns))
    image = im.fromarray(grid.astype(np.uint8))
    image = image.rotate(90)
    image = image.transpose(method=im.Transpose.FLIP_TOP_BOTTOM)
    imagename = fileloc.replace(".csv",".png")
    image.save(imagename)


    print(f"rows = {rows}, columns = {columns}")
    print(f"max value = {max}, min value = {min}")
    print(f"Image has been created at '{imagename}'")

# if __name__ == "__main__":
# filelocin = input("drag and drop file here or type name of file if it is in the same folder/directory:")
# imagify(filelocin)