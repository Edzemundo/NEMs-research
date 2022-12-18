"""imaging.py
Author: Edmund S. Agyekum

This program creates an image of the txt file created by the scan.py program using the Pillow library
and an array created through numpy

"""
import numpy as np
from PIL import Image as im

def imagify(filelocin):
    """creates an image of the txt file created after running scan
    """
    # filelocin = "trial73.txt"
    fileloc = filelocin.replace("'","")

    # opens txt result file from experiment
    with open(fileloc) as file:
        dataraw = file.read()
        data = dataraw.split()

    # determines dimensions of array
    lastline = data[-1].split(",")
    rows = int(lastline[0])+1
    columns = int(lastline[1])+1  

    # finding the min and max voltage values
    min = 100.0
    max = -100.0

    for elements in data:
        element = elements.split(",")
        if float(element[2]) < min:
            min = float(element[2])
        if float(element[2]) > max:
            max = float(element[2])

# converting to 0-255 scale and make a list of those transformed values
    valuelist = []

    ratio = lambda x : ((x-min)/(max-min))*255
    for elements in data:
        element = elements.split(",")
        value = int(ratio(float(element[2])))
        valuelist.append(value)

# creating the array and picture from it and names picture after text file
    arr = np.array(valuelist)
    grid = np.reshape(arr, (rows,columns))
    image = im.fromarray(grid.astype(np.uint8))
    image = image.rotate(90)
    image = image.transpose(im.FLIP_TOP_BOTTOM)
    imagename = fileloc.replace(".txt",".png")
    image.save(imagename)


    print(f"rows = {rows}, columns = {columns}")
    print(f"max value = {max}, min value = {min}")
    print(image)

if __name__ == "__main__":
    filelocin = input("drag and drop file here or type name of file if it is in the same folder/directory:")
    imagify(filelocin)