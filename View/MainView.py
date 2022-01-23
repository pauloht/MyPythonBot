from tkinter import *;
import tkinter as tk
import pyautogui
from View import FlowView
from Data import ActionFlow, ExecuteFlowHandler
from Data.Actions import MouseClickAction, PrintAction;
import os

class MainView:
    SINGLETON = None;

    def initWindow(self):
        self.menu_inicial.geometry(
            "500x250");
        self.menu_inicial['bg'] = "gray"

    def getTxtStream(self):
        if not(hasattr(self, "lastBtn")):
            return None, None;
        try:
            fileName = self.lastBtn.cget("text");
            path = "./Saved/" + fileName;
            if (os.path.exists(path)):
                f = open(path, "r")
                stream = f.read()
                f.close();
                return stream, fileName;
            else:
                return None, None;
        except:
            return None, None;

    def onFileBtnClick(self, btn):
        if (hasattr(self, "lastBtn")):
            self.lastBtn.configure(bg=self.lastColor);
        self.lastBtn = btn;
        self.lastColor = btn.cget("bg");
        btn.configure(bg = "red")

    def createFlowAction(self):
        self.menu_inicial.withdraw();
        FlowView.FlowView(ActionFlow.ActionFlow())

    def loadFlowAction(self):
        stream, fileName = self.getTxtStream();

        if (stream == None):
            return;
        flow = ActionFlow.ActionFlow.Deserialize(stream);
        flow.Name = fileName;
        self.menu_inicial.withdraw();
        FlowView.FlowView(flow);

    def executeFlowAction(self):
        stream, fileName = self.getTxtStream();

        if (stream == None):
            return;
        flow = ActionFlow.ActionFlow.Deserialize(stream)
        flow.Name = fileName;
        ExecuteFlowHandler.ExecuteFlow(flow);

    def createFileBtnsList(self):
        files = os.listdir("./Saved");
        self.fileBtnsFrame.grid_columnconfigure(0, weight=1);
        index = 0;
        containerList = []
        def bindCommand(btn):
            btn.configure(command= lambda: self.onFileBtnClick(btn));

        for v in range(10):
            if (v < len(files)):
                container = Button(
                    master = self.fileBtnsFrame,
                    text = files[v]
                )
                bindCommand(container);
            else:
                container = Frame(
                    master = self.fileBtnsFrame,
                )
            self.fileBtnsFrame.grid_rowconfigure(index, weight=1);
            container.grid(row=index,column=0,sticky="nsew")
            containerList.append(container);
            index = index+1


    def __init__(self):
        if (MainView.SINGLETON != None):
            MainView.SINGLETON.menu_inicial.deiconify();
            return;
        MainView.SINGLETON = self;
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
        self.fileBtnsFrame = Frame(
            master = self.menu_inicial,
            bg = "blue"
        );
        createFlowBtn.grid(row=0,column=0, sticky="nsew", columnspan=2);
        createLoadBtn.grid(row=1,column=0, sticky="nsew");
        executeFlowBtn.grid(row=2,column=0,sticky="nsew");
        self.fileBtnsFrame.grid(row=1,column=1, sticky="nsew", rowspan=2);
        self.createFileBtnsList();
        self.initWindow();
        self.menu_inicial.mainloop();
