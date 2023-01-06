import os

# opens txt result file from experiment
with open(os.path.join(os.getcwd(), "trial123.txt")) as file:
    dataraw = file.read()
    data = dataraw.split()

 #determine step size
    firstline = data[0].split(",")
    secondline = data[1].split(",")
    stepsizex = float(secondline[0]) - float(firstline[0])
    stepsizey = input("Y step size: 0.25")

print(stepsizey)