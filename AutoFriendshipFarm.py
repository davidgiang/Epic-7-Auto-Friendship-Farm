import pyautogui
import time
import tkinter as tk
from tkinter import *
import threading
from threading import *
import os

class AutoFriendshipFarm():

    file_format = '.png'
    stop_bool = False

    def __init__(self, num_runs, bagicon, clearconfirmbutton, clearportal, confirmbutton, readybutton, selectteambutton, stageclear, startbutton, stopexploring, teleportname):
        self.num_runs = num_runs
        self.bagicon = bagicon
        self.clearconfirmbutton = clearconfirmbutton
        self.clearportal = clearportal
        self.confirmbutton = confirmbutton
        self.readybutton = readybutton
        self.selectteambutton = selectteambutton
        self.stageclear = stageclear
        self.startbutton = startbutton
        self.stopexploring = stopexploring
        self.teleportname = teleportname

    def startAFF(self):
        self.stop_bool = False
        runs_to_do = self.num_runs

        while runs_to_do > 0:
            if self.stop_bool == True:
                num_runs.set("Stopped")
                break

            runs_to_do -= 1

            self.findAndClickButton('readybutton')
            time.sleep(2)
            self.findAndClickButton('selectteambutton')
            time.sleep(2)
            self.findAndClickButton('startbutton')
            time.sleep(4)
            self.findAndClickButton('bagicon')
            time.sleep(0.75)
            self.findAndClickButton('teleportname')
            time.sleep(0.75)
            self.findAndClickButton('confirmbutton')
            time.sleep(1.1)
            self.findAndClickButton('clearportal')
            time.sleep(0.75)
            self.findAndClickButton('stopexploring')
            time.sleep(3.5)
            self.findAndClickButton('stageclear')
            time.sleep(1)
            self.findAndClickButton('clearconfirmbutton')
            time.sleep(3)

            num_runs.set(runs_to_do)

    def stopAFF(self):
        print("Setting stop bool to true")
        self.stop_bool = True

    def findAndClickButton(self, image):
        image_ff = image + self.file_format
        print("Finding " + str(image))
        image_box = pyautogui.locateOnScreen(image_ff, confidence = 0.9)

        if image_box == None:
            print(str(image) + " not found")
            return

        pyautogui.moveTo(image_box)
        pyautogui.click(button='left')
        print("Clicked " + str(image) + " button")


####


# AFF = AutoFriendshipFarm(3, "bagicon.png", "clearconfirmbutton.png", "clearportal.png", "confirmbutton.png",
#                          "readybutton.png", "selectteambutton.png", "stageclear.png", "startbutton.png",
#                          "stopexploring.png", "teleportname.png")
#
# AFF.startAFF()


####

root = tk.Tk()

num_runs = StringVar()
num_runs.set('Not entered')

def bootUp():
    try:
        global AFF
        AFF = AutoFriendshipFarm(int(num_runs.get()), "bagicon.png", "clearconfirmbutton.png", "clearportal.png", "confirmbutton.png",
                                 "readybutton.png", "selectteambutton.png", "stageclear.png", "startbutton.png",
                                 "stopexploring.png", "teleportname.png")
        print("AFF initiated")
    except:
        print("Failed to initiate AFF")

def enterNumRuns():
    print("Submitting Num Runs")
    get_call = numRunEntry.get()
    try:
        if isinstance(int(get_call), int):
            num_runs.set(get_call)
        else:
            num_runs.set("Invalid")
    except:
        num_runs.set("Invalid")

    bootUp()

def startButton():
    print("Starting Auto Friendship Farm")
    startButton['state'] = 'disabled'
    numRunSubmit['state'] = 'disabled'

    if num_runs.get() == 'Invalid' or num_runs.get() == 'Not entered':
        print('Error')
    else:
        try:
            threading.Thread(target=AFF.startAFF).start()
        except:
            print("No AFF initiated yet")

def stopButton():
    print("Stopping Auto Friendship Farm")
    startButton['state'] = 'normal'
    numRunSubmit['state'] = 'normal'

    try:
        threading.Thread(target=AFF.stopAFF).start()
    except:
        print("No AFF initated yet")

########################################

startButtonFrame = tk.Frame(
    master = root,
    height = 500,
    width = 500
)

stopButtonFrame = tk.Frame(
    master = root,
    height = 500,
    width = 500
)

startButton = tk.Button(
    master = startButtonFrame,
    text = "Start",
    width = 5,
    height = 1,
    bg = "gray",
    fg = "black",
    command = startButton
)

stopButton = tk.Button(
    master = stopButtonFrame,
    text = "Stop",
    width = 5,
    height = 1,
    bg = "gray",
    fg = "black",
    command = stopButton
)

numRunFrame = tk.Frame(
    master = root,
    height = 500,
    width = 500
)

numRunLabel = tk.Label(
    master = numRunFrame,
    text = 'Enter Run Amount: '
)

numRunEntry = tk.Entry(
    master = numRunFrame,
    width = 17
)

numRunsToDo = tk.Label(
    master = root,
    text = "Runs Left to Do: "
)

numRunAmt = tk.Label(
    master = root,
    textvariable = num_runs
)

numRunSubmit = tk.Button(
    master=root,
    text="Enter",
    width=5,
    height=1,
    bg="gray",
    fg="black",
    command=enterNumRuns
)

####

startButtonFrame.pack()
startButtonFrame.place(relx=0.04, rely=0.85)

stopButtonFrame.pack()
stopButtonFrame.place(relx=0.22, rely=0.85)

startButton.pack()
stopButton.pack()

numRunFrame.pack()
numRunFrame.place(relx=0.04, rely=0.1)
numRunLabel.pack(side="left")
numRunEntry.pack()

numRunsToDo.pack()
numRunsToDo.place(relx=0.04, rely=0.48)
numRunAmt.pack()
numRunAmt.place(relx=0.45, rely=0.48)

numRunSubmit.pack()
numRunSubmit.place(relx=0.825, rely=0.085)

root.title("Auto Friendship Farm by Traase")
root.geometry("320x240")
root.resizable(False, False)
root.mainloop()