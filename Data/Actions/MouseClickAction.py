import pyautogui
from .Action import Action

class MouseClickAction(Action):
    cordX = 0;
    cordY = 0;

    def __init__(self, cordX, cordY):
        self.cordX = cordX;
        self.cordY = cordY;

    def __str__(self):
        return "Click|(" + str(self.cordX) + "," + str(self.cordY) + ")";

    def OnAction(self):
        pyautogui.moveTo(self.cordX, self.cordY);
