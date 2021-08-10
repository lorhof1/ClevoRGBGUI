import time, tkinter
mode = "flash"
color = "white"
f = open("/sys/devices/platform/clevo_xsm_wmi/kb_color", "w")

#try to set the kb color to white, error if impossible
try:
    f.write("white")
    print("sucessfully test set keyboard color")

except:
    print("could not set keyboard color; make sure the prequisites are installed and you have write access to /sys/devices/platform/clevo_xsm_wmi/kb_color")

def setColor(passedColor):
    mode = "static"
    f.write(passedColor)
    print("sucessfully set keyboard color to " + passedColor)

def flash(delay):
    mode = "flash"
    while mode == "flash":
        setColor("red")
        time.sleep(delay)
        setColor("yellow")
        time.sleep(delay)
        setColor("green")
        time.sleep(delay)
        setColor("cyan")
        time.sleep(delay)
        setColor("blue")
        time.sleep(delay)
        setColor("magenta")
        time.sleep(delay)


window = tkinter.Tk()
window.title=("ClevoLinuxRGBGui")

btnWhite = tkinter.Button(window, text="White", command=lambda : setColor('white'))
btnRed = tkinter.Button(window, text="Red", command=lambda : setColor('red'))
btnYellow = tkinter.Button(window, text="Yellow", command=lambda : setColor('yellow'))
btnGreen = tkinter.Button(window, text="Green", command=lambda : setColor('green'))
btnCyan = tkinter.Button(window, text="Cyan", command=lambda : setColor('cyan'))
btnBlue = tkinter.Button(window, text="Blue", command=lambda : setColor('blue'))
btnMagenta = tkinter.Button(window, text="Magenta", command=lambda : setColor('magenta'))
#btnFlash = tkinter.Button(window, text="Rainbow Effect", command=lambda : flash(.1))

btnWhite.pack()
btnRed.pack()
btnYellow.pack()
btnGreen.pack()
btnCyan.pack()
btnBlue.pack()
btnMagenta.pack()
#btnFlash.pack()

window.mainloop()

f.close()
