from tkinter import *;
from tkinter import messagebox;
from tkinter.messagebox import askyesno, askquestion
import tkinter as tk
import time;
import pyautogui;
from . import MainView, ShowImageView;
from PIL import Image, ImageTk
import json;
from Data import ActionFlow;
from Data.Actions import MouseClickAction, PrintAction, SleepAction, Action, MouseMoveAction, WriteAction, ImageAction;
import os;
import math;


class FlowView:
    fieldSeparator = " "
    sleepTime = 2

    def switchContext(self):
        if (self.menu_inicial == None):
            return;
        self.menu_inicial.protocol("WM_DELETE_WINDOW", None);
        self.menu_inicial.destroy();
        self.menu_inicial = None;
        MainView.MainView();

    def on_closing(self):
        self.switchContext();

    def onActionUpdate(self):
        self.currentActionLabel.config(text = str(self.currentAction))

    def CreateMouseClickAction(self):
        self.currentAction = MouseClickAction.MouseClickAction();
        self.onActionUpdate();

    def getTxt(self):
        return self.sleepInValue.get()

    def CreateSleepAction(self):
        try:
            allTxt = self.getTxt();
            if (len(allTxt) == 0):
                print("Empty  txt, ignoring");
                return;
            splitTxt = allTxt.split(FlowView.fieldSeparator)
            if (len(splitTxt) < 2):
                print("Expected at least 2 fields, got " + str(len(splitTxt)));
                return;
            time = int(splitTxt[0]);
            timeVar = int(splitTxt[1]);
            self.currentAction = SleepAction.SleepAction(time, timeVar);
            self.onActionUpdate();
        except:
            print("Catch error, canceling");

    def CreateMoveMouseAction(self):
        allTxt = self.getTxt();
        if (len(allTxt) == 0):
            print("Empty  txt, ignoring");
            return;
        splitTxt = allTxt.split(FlowView.fieldSeparator)
        if (len(splitTxt) < 2):
            print("Expected at least 2 fields, got " + str(len(splitTxt)));
            return;
        try:
            timeToMove = int(splitTxt[0])
        except:
            print("Failed to parse timeToMove, string: " + splitTxt[0])
            return;
        try:
            jitter = int(splitTxt[1])
        except:
            print("Failed to parse jitter, string: " + splitTxt[1])
            return;
        time.sleep(self.sleepTime);
        currentMouseX, currentMouseY = pyautogui.position();
        self.currentAction = MouseMoveAction.MouseMoveAction(currentMouseX, currentMouseY, timeToMove, jitter);
        self.onActionUpdate();

    def CreateWriteAction(self):
        toWrite = self.getTxt();
        if (len(toWrite) == 0):
            return;
        self.currentAction = WriteAction.WriteAction(toWrite);
        self.onActionUpdate();

    def CreateImageAction(self):
        #messagebox.showinfo(title="alert", message="Move to firstCorner")
        input = self.getTxt();
        if (len(input) == 0):
            print("input empty");
            return;
        input_split = input.split(FlowView.fieldSeparator);
        if (len(input_split) < 3):
            print("Expected at least 3 fields, got " + str(len(input)));
            return;
        imgName = input_split[0];
        if (len(imgName) == 0):
            print("No image name");
            return;
        png_extension = ".png";
        if not(imgName.endswith(png_extension)):
            imgName += png_extension;
        try:
            pulses = int(input_split[1]);
        except:
            print("Failed to parse to int string:" + input_split[1]);
            return;
        onFailFlow = input_split[2];
        if (len(onFailFlow) == 0):
            print("OnFailFlow field empty");
            return;
        time.sleep(self.sleepTime);
        print("snapshot first position")
        #messagebox.showinfo(title="alert", message="Move to secondCorner")
        currentMouseX, currentMouseY = pyautogui.position();
        time.sleep(self.sleepTime);
        print("snapshot second position")
        currentMouseX2, currentMouseY2 = pyautogui.position();
        difx = abs(currentMouseX - currentMouseX2);
        dify = abs(currentMouseY - currentMouseY2);
        posx = math.floor((currentMouseX + currentMouseX2)/2 - difx/2);
        posy = math.floor((currentMouseY + currentMouseY2)/2 - dify/2);
        self.im = pyautogui.screenshot("./Images/" + imgName,
                                        region=(
                                            posx,
                                            posy,
                                            difx,
                                            dify
                                            ))
        self.currentAction = ImageAction.ImageAction(imgName, posx, posy, difx, dify, pulses, onFailFlow);
        self.onActionUpdate();
        return;

    def initEmptyAction(self):
        self.currentActionLabel.config(text = "No action")
        self.currentAction = None;

    def loadAction(self):
        arrayLen = len(self.flow.ActionList);

        if (arrayLen <= self.index):
            self.initEmptyAction();
            return;
        self.currentAction = self.flow.ActionList[self.index];

        if self.currentAction == None:
            self.initEmptyAction();
            return;
        print("loadAction -> onActionUpdate");
        self.onActionUpdate();

    def insertCurrentAction(self):
        if (self.index >= len(self.flow.ActionList)):
            self.flow.ActionList.insert(self.index, self.currentAction);
        else:
            self.flow.ActionList[self.index] = self.currentAction

    def onNextPress(self):
        self.insertCurrentAction();
        self.index = self.index + 1;
        print("NextPress, index: " + str(self.index));
        self.loadAction();

    def onPreviousPress(self):
        if (self.index <= 0):
            print("OnPrevious ignoring");
            return;
        self.index = self.index - 1;
        print("Previous, index: " + str(self.index));
        self.loadAction();

    def onSavePress(self):
        if (self.currentAction != None):
            self.insertCurrentAction();
        _str = self.saveTxt.get("1.0", END);
        # stream = json.dumps(self.flow, separators=(',', ':'), default=lambda o: o.__dict__);
        stream = self.flow.Serialize();
        with open('./Saved/' + _str[0:(len(_str)-1)], 'w') as f:
            f.write(stream)
            f.close();
        self.switchContext();

    def __init__(self, flow):
        print("Creating FlowView");
        self.menu_inicial = tk.Toplevel();
        self.menu_inicial.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.menu_inicial.title("Flow Creation");
        # MainView.MainView.initWindow(self);
        self.menu_inicial.geometry(
            "500x250");
        self.menu_inicial['bg'] = "gray"
        self.flow = flow;
        self.index = 0;
        self.countLabel = Label(
            self.menu_inicial,
            text = "Count 0");
        upperContainerHeight = 50;
        bottomContainerHeight = 50;
        self.countLabel.place(
                width = 150,
                height = upperContainerHeight,
                x = 150/2,
                y = upperContainerHeight/2,
                anchor = CENTER)
        self.countLabel.pack_propagate(False);

        self.currentActionLabel = Label(
            self.menu_inicial,
            text = "No Action");
        self.currentActionLabel.place(
            width = (500 - 150),
            height = upperContainerHeight,
            x = 150 + (500 - 150)/2,
            y = upperContainerHeight/2,
            anchor = CENTER)

        bottomFrame = Frame(
            self.menu_inicial,
            # bg = "red"
        );
        bottomFrame.place(
            width = 500,
            height = bottomContainerHeight,
            x = 0,
            rely = 1,
            y = -bottomContainerHeight);
        bottomWrapper = Frame(
            bottomFrame,
            bg = "green"
        );
        bottomWrapper.pack(fill = "both", expand=True);
        centerFrameSize = 250 - bottomContainerHeight - upperContainerHeight;
        centerFrame = Frame(
            self.menu_inicial);
        centerFrame.place(
            width = 500,
            height = centerFrameSize,
            x = 0,
            y = upperContainerHeight);
        centerWrapper = Frame(
            centerFrame);
        centerWrapper.pack(fill = "both", expand=True);
        centerWrapper.grid_rowconfigure(0, weight=1);
        centerWrapper.grid_rowconfigure(1, weight=1);
        centerWrapper.grid_rowconfigure(2, weight=1);
        centerWrapper.grid_rowconfigure(3, weight=1);
        centerWrapper.grid_rowconfigure(4, weight=1);
        centerWrapper.grid_columnconfigure(0, weight=1);
        centerWrapper.grid_columnconfigure(1, weight=1);
        clickBtn = Button(
            master = centerWrapper,
            text = "Click Btn",
            command = self.CreateMouseClickAction
            );
        clickBtn.grid(row=0,column=0, sticky="nsew");
        moveBtn = Button(
            master = centerWrapper,
            text = "Move Mouse",
            command = self.CreateMoveMouseAction
            );
        moveBtn.grid(row=1,column=0,sticky="nsew");
        writeBtn = Button(
            master = centerWrapper,
            text = "Write Txt",
            command = self.CreateWriteAction
            );
        writeBtn.grid(row=2,column=0,sticky="nsew");
        sleepBtn = Button(
            master = centerWrapper,
            text = "Sleep Btn",
            command = self.CreateSleepAction
            );
        sleepBtn.grid(row=3,column=0, sticky="nsew");
        imageBtn = Button(
            master = centerWrapper,
            text = "ImageBtn",
            command = self.CreateImageAction
            );
        imageBtn.grid(row=4,column=0, sticky="nsew");
        self.sleepInValue = tk.StringVar()
        inValueEntry = tk.Entry(centerWrapper, textvariable=self.sleepInValue)
        inValueEntry.grid(row=0, column=1, sticky="nsew", rowspan=4);
        previousButton = Button(
            master = bottomWrapper,
            text = "Previous",
            command = self.onPreviousPress
            );
        nextButton = Button(
            master = bottomWrapper,
            text = "Next",
            command = self.onNextPress
            );
        saveFrame = Frame(
            master = bottomWrapper,
            );
        bottomWrapper.grid_rowconfigure(0, weight=1);
        bottomWrapper.grid_columnconfigure(0, weight=1);
        bottomWrapper.grid_columnconfigure(1, weight=1);
        bottomWrapper.grid_columnconfigure(2, weight=1);
        previousButton.grid(row=0,column=0, sticky="nsew");
        saveFrame.grid(row=0,column=1, sticky="nsew");
        nextButton.grid(row=0,column=2, stick="nsew");
        saveButton = Button(
            master = saveFrame,
            text = "Save",
            command = self.onSavePress
            );
        saveTxt = Text(
            master = saveFrame)
        saveTxt.insert(INSERT, flow.Name)
        self.saveTxt = saveTxt;
        saveButton.place(
            relx = 0.5,
            rely = 0.5,
            y = -12.5,
            width = 150,
            height = 25,
            anchor = "center"
        )
        saveTxt.place(
            relx = 0.5,
            rely = 0.5,
            y = 12.5,
            width = 150,
            height = 25,
            anchor = "center"
        )
        self.loadAction();
        # self.menu_inicial.mainloop();
