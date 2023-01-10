import os
import csv
import numpy as np
from PIL import Image as im

"""creates an image of the txt file created after running scan
"""
filelocin = os.path.join(os.getcwd(),"sample122.csv")
fileloc = filelocin.replace("'","")


# opens txt result file from experiment
# with open(fileloc) as file:
#     dataraw = file.read()
#     data = dataraw.split()

with open(fileloc) as file:
    dataraw = list(csv.reader(file, delimiter=','))
    print(dataraw[0])
#determine step sizes
# firstline = data[0].split(",")
# secondline = data[1].split(",")