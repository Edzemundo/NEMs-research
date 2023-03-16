"""scan2gui.py
Author: Edmund S. Agyekum

This program acts as a gui for the scanning process. it is the second iteration,
porting from pure tk to pysimplegui which is a tk (among other packages) wrapper.

"""

import PySimpleGUI as sg
import scan as sc
import imaging as im

sg.theme("Dark Blue 6") #set the theme of the window

voltages = [] #voltage values to be transferred over to the scan function

#input and output tuples are to prevent having to constantly type these variables in
inputs = ("startzin","startyin","stopzin","stopyin","stepin")
outputs = ("startzout","startyout","stopzout","stopyout","stepout")

#1st column in gui
col1 = [[sg.Text("Start Z: ")],
        [sg.Text("Start Y: ")],
        [sg.Text("Stop Z: ")],
        [sg.Text("Stop Y:")],
        [sg.Text("Step: ")],
        [sg.VPush()],
        []]

#2nd column in gui
col2 = [[sg.Input(size=(15), justification="c", key = inputs[0]), sg.Text("V")],
        [sg.Input(size=(15), justification="c", key = inputs[1]), sg.Text("V")],
        [sg.Input(size=(15), justification="c", key = inputs[2]), sg.Text("V")],
        [sg.Input(size=(15), justification="c", key = inputs[3]), sg.Text("V")],
        [sg.Input(size=(15), justification="c", key = inputs[4]), sg.Text("V")]]

#3rd column in gui
col3 = [[sg.Text(key = outputs[0])],
        [sg.Text(key = outputs[1])],
        [sg.Text(key = outputs[2])],
        [sg.Text(key = outputs[3])],
        [sg.Text(key = outputs[4])]]

#1st (scanning) tab including everthing else not in columns
tab1 = [[sg.Column(col1, pad=15), sg.Column(col2, pad=5), sg.Column(col3, pad=0)],
        [sg.Push(), sg.Text("", key = "statusout", pad = (10,5)), sg.Push()], 
        [sg.Push(), sg.Push(), sg.Radio(".csv", "RAD1", key=".csv", pad=(17,5), default = True)],
        [sg.Push(), sg.Button("Set Values", pad = (37,10)), sg.Radio(".txt", "RAD1", pad=(21,5))],
        [sg.Button("Clear Values", pad=(20,10)), sg.Button("Scan 2", key = "scan2", pad=(10,10)), sg.Checkbox("Image file", key = "image_request", pad = (15,10), enable_events=True , default=True)]]
# sg.Push can be used on both sides for centering

#2nd (imaging) tab
tab2 = [[sg.Text("Insert file for imaging")],
        [sg.Input(size=(35), key="type_image"), sg.FileBrowse(key="browse_image")],
        [sg.Push(), sg.Text(key="image_status"),sg.Push()],
        [sg.Push(), sg.Button("Image", key="tab2_image"),sg.Push()]]

#overall layout
layout = [[sg.Titlebar("Scan by Edmund", background_color="black")],
          [sg.TabGroup([[sg.Tab("Scan", tab1), sg.Tab("Imaging", tab2)]])]]

#describes the overall window
window = sg.Window("Scan 2", layout, size = (350,420))

completed_entry = False #used to determine if variables have been entered and set

while True:
    #recuring loop as window will be constantly reading and updating values on every "event instance"
    event, values = window.read() #event initializes the gui, values is a dictionary containing all values in window
    
    #required in order to close the window normally
    if event == sg.WIN_CLOSED or event == "Exit":
        break

    #when the "Set Values" button is clicked
    if event == "Set Values":

        try:
            #adds the input voltages to the voltages array in a specific order
            voltages.append(float(values["startzin"]))
            voltages.append(float(values["startyin"]))
            voltages.append(float(values["stopzin"]))
            voltages.append(float(values["stopyin"]))
            voltages.append(float(values["stepin"]))

            #prints out the "x set!" readout on column 3
            for i in range(len(outputs)):
                window[outputs[i]].update(f"{voltages[i]} set!")
            window["statusout"].update("Voltages Set!") #statusout test becomes "Voltages set" 

            startz, starty, stopz, stopy, step = voltages # assigns these variables to the values in the voltages array respectively

            #test prints
            print(event, values)
            print(voltages)
            print(startz,step)

            completed_entry = True #shows that the values have been entered and set

            voltages = [] #clears the voltage array for potential new values. values are still stored in variables above for scan2
        
        #if not all values are entered or invalid values "eg. letters are entered", it will call an error in statusout text
        except ValueError:
            window["statusout"].update("All voltages must be filled with numbers")


    #if clear values button is clicked
    if event == "Clear Values":
        voltages = []
        values = dict.fromkeys(values, 0) #sets all the values in dictionary read from the window to 0
        
        #clears the input boxes.
        for i in range(len(inputs)):
            window[inputs[i]].update("")
            window[outputs[i]].update("")
        window["statusout"].update("Voltages Cleared") # status out set to "Voltages Cleared"

        startz, starty, stopz, stopy, step = 0,0,0,0,0 # variables for scan2 set to 0
        completed_entry = False #shows that values not entered and set
        

    #if image button on image tab is clicked
    if event == "tab2_image":
        imageinput = values["type_image"] #gets the file location from input textbox
        if imageinput[-4:] not in [".csv", ".txt"]: #determines if file is not .csv or .txt
            window["image_status"].update("Insert .csv or .txt file")
        else:
            try:
                #asks for the step size of the file since have not implemented y-step size detection
                stepsizey = sg.PopupGetText("Please Enter Step Size:")
                window["image_status"].update("File imaged!")
                im.imagify(imageinput, stepsizey) #images the file using imaging program
        
            except FileNotFoundError:
                window["image_status"].update("File not found") # calls an error if file is not founf


    #if scan2 button is clicked
    if event == "scan2":
        if completed_entry == True: #checks if values are entered and set
            if values[".csv"] == True: #this is used to check if the user wants a .csv file (on by default) using the radio buttons
                namedfile = sg.popup_get_text("Enter file name(no need to add extension): ") #asks for the file name
                namedfile += ".csv" # adds .csv to file name
            else:
                namedfile = sg.popup_get_text("Enter file name(no need to add extension): ")
                namedfile += ".txt" #adds .txt to filename if txt radio was selected
            
            #runs scan2 function from scan program
            window["statusout"].update(f"Creating {namedfile}")
            sc.scan2(startz, starty, stopz, stopy, step, namedfile)
            window["statusout"].update(f"{namedfile} created")
            if values["image_request"] == True: #if image checkbox was selected, images the file
                im.imagify(sc.filename, step)

        else:
            window["statusout"].update("You need to 'Set Values' first") # if values were not entered and set, flags error
        
        
window.close()



