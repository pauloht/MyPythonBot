from tkinter import *;
import tkinter as tk
import time;
import pyautogui;
from . import MainView;
import json;
from Data import ActionFlow;
from Data.Actions import MouseClickAction, PrintAction, SleepAction, Action;


class FlowView:
    menu_inicial = None;
    countLabel = None;
    currentActionLabel = None;
    btnRecordClickAction = None;
    flow = None;
    index = 0;
    sleepTime = 2;
    currentAction = None;
    saveTxt = None;
    sleepInValue = "";

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
        time.sleep(self.sleepTime);
        currentMouseX, currentMouseY = pyautogui.position();
        self.currentAction = MouseClickAction.MouseClickAction(currentMouseX, currentMouseY);
        self.onActionUpdate();

    def CreateSleepAction(self):
        try:
            time = int(self.sleepInValue.get());
            self.currentAction = SleepAction.SleepAction(time);
            self.onActionUpdate();
        except:
            print("Canceling");

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

    def __init__(self, old_menu, flow):
        print("Creating FlowView");
        old_menu.destroy();
        self.menu_inicial = Tk();
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
        centerWrapper.grid_columnconfigure(0, weight=1);
        centerWrapper.grid_columnconfigure(1, weight=1);
        clickBtn = Button(
            master = centerWrapper,
            text = "Click Btn",
            command = self.CreateMouseClickAction
            );
        clickBtn.grid(row=0,column=0, sticky="nsew");
        sleepBtn = Button(
            master = centerWrapper,
            text = "Sleep Btn",
            command = self.CreateSleepAction
            );
        sleepBtn.grid(row=1,column=0, sticky="nsew");
        self.sleepInValue = tk.StringVar()
        inValueEntry = tk.Entry(centerWrapper, textvariable=self.sleepInValue)
        inValueEntry.grid(row=1, column=1, sticky="nsew");
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
        saveTxt.insert(INSERT, "DefaultName.txt")
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
        self.menu_inicial.mainloop();
        # self.btnRecordClickAction = Button(
        #     master = self.menu_inicial,
        #     text = "Record Click",
        #     command = self.CreateMouseClickAction,
        #     bg = "green",
        #     width = 500,
        #     height = 200);
        # self.btnRecordClickAction.place(
        #     x = 0,
        #     y = 50);
