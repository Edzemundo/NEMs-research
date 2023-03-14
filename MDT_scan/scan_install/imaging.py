"""imaging.py
Author: Edmund S. Agyekum

This program creates an image of the txt file created by the scan.py program using the Pillow library
and an array created through numpy

"""
import os
import csv
import numpy as np
from PIL import Image as im


def imagify(filelocin, stepsizey):
    """determine if file is txt or csv then run appropriate function
    """
    fileloc = filelocin.replace("'","")
    if fileloc.endswith(".csv"):
        imagifycsv(fileloc, stepsizey)
    elif fileloc.endswith(".txt"):
        imagifytxt(fileloc, stepsizey)
    else:
        print("Only .csv and .txt file formats supported")



def imagifytxt(filelocin, stepsizey):
    """creates an image of the txt file created after running scan
    """
    # filelocin = "trial73.txt"
    fileloc = filelocin.replace("'","")
    
    # opens txt result file from experiment
    with open(fileloc) as file:
        dataraw = file.read()
        data = dataraw.split()

    #determine step sizes
    firstline = data[0].split(",")
    secondline = data[1].split(",")
    stepsizex = float(secondline[0]) - float(firstline[0])
    stepsizey = float(stepsizey)

    # determines dimensions of array
    lastline = data[-1].split(",")
    rows = int(float(lastline[0])/stepsizex)+1
    columns = int(float(lastline[1])/stepsizey)+1

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
    global image # made global to open the image outside the function.
    global resized_image
    arr = np.array(valuelist)
    grid = np.reshape(arr, (rows,columns))
    image = im.fromarray(grid.astype(np.uint8))
    image = image.rotate(90)
    image = image.transpose(method=im.Transpose.FLIP_TOP_BOTTOM)
    imageloc = fileloc.replace(".txt" or ".csv",".png")
    resized_image = image.resize((image.size[0]*4, image.size[1]*4))
    resized_image.save(imageloc)
    image.show(imageloc)

# prints out some (maybe) helpful information on the image after it has been created
    print(f"rows = {rows}, columns = {columns}")
    print(f"max value = {max}, min value = {min}")
    print(f"Image has been created at '{imageloc}'")



def imagifycsv(filelocin, stepsizey):
    """creates an image of the csv file created after running scan
    """
    # opens txt result file from experiment
    fileloc = filelocin.replace("'","")
    with open(fileloc) as file:
        data = list(csv.reader(file, delimiter=','))

    #determine step sizes
    firstline = data[0]
    secondline = data[1]
    stepsizex = float(secondline[0]) - float(firstline[0])
    stepsizey = float(stepsizey)

    # determines dimensions of array
    lastline = data[-1]
    rows = int(float(lastline[0])/stepsizex)+1
    columns = int(float(lastline[1])/stepsizey)+1

    # finding the min and max voltage values
    min = 100.0
    max = -100.0

    for elements in data:
        if float(elements[2]) < min:
            min = float(elements[2])
        if float(elements[2]) > max:
            max = float(elements[2])

    # converting to 0-255 scale and make a list of those transformed values
    valuelist = []

    ratio = lambda x : ((x-min)/(max-min))*255
    for elements in data:
        value = int(ratio(float(elements[2])))
        valuelist.append(value)

    
    # creating the array and picture from it and names picture after text file
    global image # made global to open the image outside the function.
    global resized_image
    arr = np.array(valuelist)
    grid = np.reshape(arr, (rows,columns))
    image = im.fromarray(grid.astype(np.uint8))
    image = image.rotate(90)
    image = image.transpose(method=im.Transpose.FLIP_TOP_BOTTOM)
    imageloc = fileloc.replace(".csv",".png")
    resized_image = image.resize((image.size[0]*4, image.size[1]*4))
    resized_image.save(imageloc)
    image.show(imageloc)

# prints out some (maybe) helpful information on the image after it has been created
    print(f"rows = {rows}, columns = {columns}")
    print(f"max value = {max}, min value = {min}")
    print(f"Image has been created at '{imageloc}'")


"""runs if the python file is run directly. Asks for txt/csv file then created the image"""
if __name__ == "__main__":
    # filelocin = os.path.join(os.getcwd(),"sample124.csv") #test line
    filelocin = input("drag and drop file here or type name of file if it is in the same folder/directory: ")
    imagify(filelocin)
    resized_image.show()
    