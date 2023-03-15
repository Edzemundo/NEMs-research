"""scan2gui.py
Author: Edmund S. Agyekum

This program acts as a gui for the scanning process. it is the second iteration,
porting from pure tk to pysimplegui which is a tk (among other packages) wrapper.

"""

import PySimpleGUI as sg
# import scan as sc
import imaging as im

sg.theme("Dark Blue 6")

voltages = []
inputs = ("startzin","startyin","stopzin","stopyin","stepin")
outputs = ("startzout","startyout","stopzout","stopyout","stepout")

col1 = [[sg.Text("Start Z: ")],
        [sg.Text("Start Y: ")],
        [sg.Text("Stop Z: ")],
        [sg.Text("Stop Y:")],
        [sg.Text("Step: ")],
        [sg.VPush()],
        []]

col2 = [[sg.Input(size=(15), justification="c", key = inputs[0]), sg.Text("V")],
        [sg.Input(size=(15), justification="c", key = inputs[1]), sg.Text("V")],
        [sg.Input(size=(15), justification="c", key = inputs[2]), sg.Text("V")],
        [sg.Input(size=(15), justification="c", key = inputs[3]), sg.Text("V")],
        [sg.Input(size=(15), justification="c", key = inputs[4]), sg.Text("V")]]


col3 = [[sg.Text(key = outputs[0])],
        [sg.Text(key = outputs[1])],
        [sg.Text(key = outputs[2])],
        [sg.Text(key = outputs[3])],
        [sg.Text(key = outputs[4])]]


tab1 = [[sg.Column(col1, pad=15), sg.Column(col2, pad=5), sg.Column(col3, pad=0)],
        [sg.Push(), sg.Text("", key = "statusout", pad = (10,5)), sg.Push()], 
        [sg.Push(), sg.Push(), sg.Radio(".csv", "RAD1", key=".csv", pad=(17,5), default = True)],
        [sg.Push(), sg.Button("Set Values", pad = (37,10)), sg.Radio(".txt", "RAD1", pad=(21,5))],
        [sg.Button("Clear Values", pad=(20,10)), sg.Button("Scan 2", key = "scan2", pad=(10,10)), sg.Checkbox("Image file", key = "image_request", pad = (15,10), enable_events=True , default=True)]]
# sg.Push can be used on both sides for centering

tab2 = [[sg.Text("Insert file for imaging")],
        [sg.Input(size=(35), key="type_image"), sg.FileBrowse(key="browse_image")],
        [sg.Push(), sg.Text(key="image_status"),sg.Push()],
        [sg.Push(), sg.Button("Image", key="tab2_image"),sg.Push()]]

layout = [[sg.Titlebar("Scan by Edmund", background_color="black")],
          [sg.TabGroup([[sg.Tab("Scan", tab1), sg.Tab("Imaging", tab2)]])]]

window = sg.Window("Scan 2", layout, size = (350,420))

completed_entry = False

while True:
    event, values = window.read()
    
    if event == sg.WIN_CLOSED or event == "Exit":
        break

    if event == "Set Values":

        try:
            voltages.append(float(values["startzin"]))
            voltages.append(float(values["startyin"]))
            voltages.append(float(values["stopzin"]))
            voltages.append(float(values["stopyin"]))
            voltages.append(float(values["stepin"]))

            for i in range(len(outputs)):
                window[outputs[i]].update(f"{voltages[i]} set!")
            window["statusout"].update("Voltages Set!")

            startz, starty, stopz, stopy, step = voltages

            print(event, values)
            print(voltages)
            print(startz,step)

            completed_entry = True

            voltages = []
        
        except ValueError:
            window["statusout"].update("All voltages must be filled with numbers")


    if event == "Clear Values":
        voltages = []
        values = dict.fromkeys(values, 0)
        
        for i in range(len(inputs)):
            window[inputs[i]].update("")
            window[outputs[i]].update("")
        window["statusout"].update("Voltages Cleared")

        startz, starty, stopz, stopy, step = 0,0,0,0,0
        completed_entry = False
        

    if event == "tab2_image":
        imageinput = values["type_image"]
        if imageinput[-4:] not in [".csv", ".txt"]:
            window["image_status"].update("Insert .csv or .txt file")
        else:
            try:
                stepsizey = sg.PopupGetText("Please Enter Step Size:")
                window["image_status"].update("File imaged!")
                im.imagify(imageinput, stepsizey)
        
            except FileNotFoundError:
                window["image_status"].update("File not found")



    # if event == "scan2":
    #     if completed_entry == True:  
    #         if values[".csv"] == True:
    #             namedfile = sg.popup_get_text("Enter file name(no need to add extension): ")
    #             namedfile += ".csv"
    #         else:
    #             namedfile = sg.popup_get_text("Enter file name(no need to add extension): ")
    #             namedfile += ".txt"
            
    #         window["statusout"].update(f"Creating {namedfile}")
    #         sc.scan2(startz, starty, stopz, stopy, step, namedfile)
    #         window["statusout"].update(f"{namedfile} created")
    #         if values["image_request"] == True:
    #             im.imagify(sc.filename, step)

    #     else:
    #         window["statusout"].update("You need to 'Set Values' first")
        
        
window.close()



