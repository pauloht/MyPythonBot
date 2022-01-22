from tkinter import *;
import tkinter as tk
import pyautogui
from View import FlowView
from Data import ActionFlow
from Data.Actions import MouseClickAction, PrintAction;
import os

class MainView:
    def initWindow(self):
        self.menu_inicial.geometry(
            "500x250");
        self.menu_inicial['bg'] = "gray"

    def createFlowAction(self):
        FlowView.FlowView(self.menu_inicial, ActionFlow.ActionFlow())

    def loadFlowAction(self):
        path = "./Saved/" + self.inValue.get();
        if (os.path.exists(path)):
            f = open(path, "r")
            stream = f.read()
            f.close();
            FlowView.FlowView(self.menu_inicial,
                ActionFlow.ActionFlow.Deserialize(stream));
        else:
            print("Failed to open file: " + path);

    def executeFlowAction(self):
        print("Todo");

    def __init__(self):
        self.menu_inicial = Tk();
        self.menu_inicial.title("Primeira APP");
        self.menu_inicial.grid_columnconfigure(0, weight=1);
        self.menu_inicial.grid_columnconfigure(1, weight=1);
        self.menu_inicial.grid_rowconfigure(0, weight=1);
        self.menu_inicial.grid_rowconfigure(1, weight=1);
        self.menu_inicial.grid_rowconfigure(2, weight=1);
        createFlowBtn = Button(
            master = self.menu_inicial,
            command = self.createFlowAction,
            text = "Create Flow"
        )
        createLoadBtn = Button(
            master = self.menu_inicial,
            command = self.loadFlowAction,
            text = "Load Flow"
        )
        executeFlowBtn = Button(
            master = self.menu_inicial,
            command = self.executeFlowAction,
            text = "Execute Flow"
        )
        createFlowBtn.grid(row=0,column=0, sticky="nsew", columnspan=2);
        createLoadBtn.grid(row=1,column=0, sticky="nsew");
        executeFlowBtn.grid(row=2,column=0,sticky="nsew");
        self.inValue = tk.StringVar()
        inValueEntry = tk.Entry(self.menu_inicial, textvariable=self.inValue)
        inValueEntry.grid(row=1, column=1, sticky="nsew", rowspan=2);
        self.initWindow();
        self.menu_inicial.mainloop();
