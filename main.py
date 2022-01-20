from tkinter import *
import pyautogui

menu_inicial = Tk();
menu_inicial.title("Primeira APP");
menu_inicial.geometry(
    "500x250");



def printSS():
    im2 = pyautogui.screenshot('my_screenshot.png');

def moveMouse():
    pyautogui.moveTo(50, 50);

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

menu_inicial['bg'] = "gray"
menu_inicial.mainloop();
