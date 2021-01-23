import tkinter as tk
from tkinter import filedialog, Text, simpledialog, Label
import os
import finvizscraper as fs
root = tk.Tk()

def addFile():
    #This doesnt add a task rn, instead it just opens file manager (part of tutorial)
    filename = filedialog.askopenfilename(initialdir="/", title = "select File")
    filetypes=(("exectables", "*.exe"),("All files","*.*"))



canvas = tk.Canvas(root, height = 700, width = 700, bg ='thistle1')
canvas.pack()




frame = tk.Frame(root, bg = "white")
frame.place(relwidth=0.8, relheight= 0.8, relx = 0.1, rely = 0.1)

qy = 100
qx = 25
listnum = 1
list = []
def getTask():
    global qy
    global tasklabel
    global listnum
    global list
    task = simpledialog.askstring("Enter Task", "Please enter a task")
    tasklabel = Label(frame, text = str(listnum) + '. ' + str(task)  , fg = 'black')
    tasklabel.place(x = qx, y = qy)
    list.append(task)
    qy += 30
    listnum += 1

def destroyTask():
    global listnum
    checkoffTask = simpledialog.askinteger("Enter Number", "Please enter the number of the task you to mark as completed")
    del list[checkoffTask]
    listnum -=1


def addImpInfo():
    global marketCapLabel
    global InstOwnLabel
    global ATRLabel
    global floatLabel
    global ShortFloatLabel
    tickerList = fs.findImpInfoOnTicker()
    marketCapLabel = Label(frame, text = "Market Cap: " + str(tickerList[0]), fg = 'black')
    floatLabel = Label(frame, text = "Float: " + str(tickerList[1]), fg = 'black')
    ShortFloatLabel = Label(frame, text="Short Float: " + str(tickerList[2]), fg='black')
    ATRLabel = Label(frame, text="ATR: " + str(tickerList[3]), fg='black')
    InstOwnLabel = Label(frame, text="Inst Own: " + str(tickerList[4]), fg='black')
    marketCapLabel.pack(pady= 5)
    floatLabel.pack(pady= 5)
    ShortFloatLabel.pack(pady= 5)
    InstOwnLabel.pack(pady= 5)
    ATRLabel.pack(pady= 5)


def deleteStockInfo():
    marketCapLabel.destroy()
    InstOwnLabel.destroy()
    floatLabel.destroy()
    ShortFloatLabel.destroy()
    ATRLabel.destroy()


AddStockInfo = tk.Button(frame, text = "Get Stock Info", padx = 5, pady = 5, fg = 'white', bg = 'turquoise', command = addImpInfo)
AddStockInfo.pack(side = tk.TOP)

removeTask = tk.Button(frame, text = "Remove Stock Info", command = deleteStockInfo)
removeTask.pack(pady= 10)






root.mainloop();