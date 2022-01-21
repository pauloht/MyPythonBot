from tkinter import *;
import tkinter as tk
import pyautogui
from View import FlowView
from Data import ActionFlow
from Data.Actions import MouseClickAction, PrintAction;

menu_inicial = Tk();
menu_inicial.title("Primeira APP");

def initWindow():
    global menu_inicial;
    menu_inicial.geometry(
        "500x250");
    menu_inicial['bg'] = "gray"
    #menu_inicial.resizable(False, False);

btnGroup = []

def createFlowAction():
    global menu_inicial;
    menu_inicial.destroy();
    menu_inicial = Tk();
    menu_inicial.title("Flow Creation");
    initWindow();
    FlowView.FlowView(menu_inicial, ActionFlow.ActionFlow())


    # menu_inicial.title("Second window");
    # menu_inicial['bg'] = "gray";
    # menu_inicial.mainloop();

createFlowBtn = Button(
    master = menu_inicial,
    command = createFlowAction,
    text = "Create Flow"
)
btnGroup.append(createFlowBtn)

for btn in btnGroup:
    btn.pack();

initWindow();
menu_inicial.mainloop();

#print screen
# def printSS():
#     im2 = pyautogui.screenshot('my_screenshot.png');

#move mouse to a screen pixel location
# def moveMouse():
#     pyautogui.moveTo(50, 50);

# faz label
# label_1 = Label(menu_inicial, text = "MeuLabel");
# label_1.pack();

# faz text field
# T = Text(menu_inicial, height = 50, width = 200);
# T.pack();

# fazer dropdown
# lista = ["Option1", "Opt2", "Opt3"]
# dropdownValue = StringVar(menu_inicial);
# dropdownValue.set("Select an value");
# dropdown = OptionMenu(
# 	menu_inicial, dropdownValue, *lista)
# dropdown.pack();

# faz botao
# btnMoveMouse = Button(
#     master = menu_inicial,
#     text = "Mover mouse",
#     command = moveMouse);
# btnMoveMouse.pack();
