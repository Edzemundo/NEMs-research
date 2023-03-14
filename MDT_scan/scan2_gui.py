"""Edmund!!! BEFORE STARTING TEST, CHECK SCAN2 IS IMPORTED AND IMPLEMENTED (scan2 button on line 139)"""
# replace MDT

# import scan
from tkinter import *
from tkinter import ttk
# from tkinter import filedialog as fd



# def usescan2():
    # if status.get() == "Not all variables set":
        # status.set("No values, no start")
    
    # else:
        # scan2(startz, starty, stopz, stopy, step) 
        # status.set("Scanning...")


def set_vars(*args):
    """stores the input values of voltages as their respective variables"""
    try:
        fstartz = float(startz.get())  
        fstarty = float(starty.get())
        fstopz = float(stopz.get())
        fstopy = float(stopy.get())
        fstep = float(step.get())

        status_startz.set(f"{fstartz} V set")
        status_starty.set(f"{fstarty} V set")
        status_stopz.set(f"{fstopz} V set")
        status_stopy.set(f"{fstopy} V set")
        status_step.set(f"{fstep} V set")
    
        status.set("All values set!")
    
    except ValueError:

        status.set("Variable(s) not number or not set")


def clear_vars(*args):
    """Used to clear all varaibles using the clear values button"""

    startz_entry.delete(0, 'end')
    starty_entry.delete(0, 'end')
    stopz_entry.delete(0, 'end')
    stopy_entry.delete(0, 'end')
    step_entry.delete(0, 'end')
    status_startz.set("")
    status_starty.set("")
    status_stopz.set("")
    status_stopy.set("")
    status_step.set("")
    startz.set("")
    starty.set("")
    stopz.set("")
    stopy.set("")
    step.set("")


    status.set("Enter voltage values")


"""Beginning of tk window"""
root = Tk()
root.title("Scan 2")

# main window
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W , E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

mainframe.columnconfigure(0, weight=3)
mainframe.columnconfigure(1, weight=3)
mainframe.columnconfigure(2, weight=3)
mainframe.columnconfigure(3, weight=1)
mainframe.columnconfigure(4, weight=1)
mainframe.rowconfigure(1, weight=1)
mainframe.rowconfigure(2, weight=1)
mainframe.rowconfigure(3, weight=1)
mainframe.rowconfigure(4, weight=1)
mainframe.rowconfigure(5, weight=1)
mainframe.rowconfigure(6, weight=1)
root.minsize(310,400)
root.maxsize(310,400)

# startz variable
startz = StringVar()
status_startz = StringVar()
startz_entry = ttk.Entry(mainframe, width = 12, textvariable=startz)
startz_entry.grid(column=2, row=1, sticky=(W))
ttk.Label(mainframe, text="Start Z: ").grid(column=1, row=1, sticky=W)
ttk.Label(mainframe, text="V").grid(column=3, row=1, sticky=W)
ttk.Label(mainframe, textvariable=status_startz).grid(column=4, row=1, sticky=W)

# starty variable
starty = StringVar()
status_starty = StringVar()
starty_entry = ttk.Entry(mainframe, width = 12, textvariable=starty)
starty_entry.grid(column=2, row=2, sticky=(W))
ttk.Label(mainframe, text="Start Y: ").grid(column=1, row=2, sticky=W)
ttk.Label(mainframe, text="V").grid(column=3, row=2, sticky=W)
ttk.Label(mainframe, textvariable=status_starty).grid(column=4, row=2, sticky=W)


# stopz variable
stopz = StringVar()
status_stopz = StringVar()
stopz_entry = ttk.Entry(mainframe, width = 12, textvariable=stopz)
stopz_entry.grid(column=2, row=3, sticky=(W))
ttk.Label(mainframe, text="Stop Z: ").grid(column=1, row=3, sticky=W)
ttk.Label(mainframe, text="V").grid(column=3, row=3, sticky=W)
ttk.Label(mainframe, textvariable=status_stopz).grid(column=4, row=3, sticky=W)


# stopy variable
stopy = StringVar()
status_stopy = StringVar()
stopy_entry = ttk.Entry(mainframe, width = 12, textvariable=stopy)
stopy_entry.grid(column=2, row=4, sticky=(W))
ttk.Label(mainframe, text="Stop Y: ").grid(column=1, row=4, sticky=W)
ttk.Label(mainframe, text="V").grid(column=3, row=4, sticky=W)
ttk.Label(mainframe, textvariable=status_stopy).grid(column=4, row=4, sticky=W)


# step variable
step = StringVar()
status_step = StringVar()
step_entry = ttk.Entry(mainframe, width = 12, textvariable=step)
step_entry.grid(column=2, row=5, sticky=(W))
ttk.Label(mainframe, text="Step: ").grid(column=1, row=5, sticky=W)
ttk.Label(mainframe, text="V").grid(column=3, row=5, sticky=W)
ttk.Label(mainframe, textvariable=status_step).grid(column=4, row=5, sticky=W)


# shows the status of the input variables
status = StringVar()
status.set("Enter voltage values")
ttk.Label(mainframe, textvariable=status).grid(columnspan=3, column=1, row=6,)


# sets the input variable using the set_vars command
entry_button = ttk.Button(mainframe, text="Enter Values", command=set_vars).grid(column=2, row=7, sticky=W)


"""Dont forget to enter the command in the button below"""
# runs the scan2 command from scan.py depecdency
ttk.Button(mainframe, text="Scan 2").grid(column=2, row=8, sticky=W)

# clears the values using the clear_cars command
ttk.Button(mainframe, text="Clear Values", command=clear_vars).grid(column=1, row=8, sticky=W)

# universal padding for all children in parent(main window)
for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)

# sets the startz entry as the main focus so user can just start typing values after running program
startz_entry.focus()
# hitting return key clears variables
root.bind("<Return>", clear_vars)

root.mainloop()


#------------------------------------------------------------------------------------------------------------------#

#space seperated for **upgraaadeeeesss**🤭 p.s. multiple pages/functionality

