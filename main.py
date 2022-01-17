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

btnPrint = Button(
    master = menu_inicial,
    text = "Print",
    command = printSS);
btnMoveMouse = Button(
    master = menu_inicial,
    text = "Mover mouse",
    command = moveMouse);
btnPrint.pack();
btnMoveMouse.pack();

menu_inicial['bg'] = "gray"
menu_inicial.mainloop();
