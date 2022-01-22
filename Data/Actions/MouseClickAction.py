import pyautogui
from .Action import Action

class MouseClickAction(Action):
    cordX = 0;
    cordY = 0;

    def __init__(self, cordX, cordY):
        Action.__init__(self);
        self.cordX = cordX;
        self.cordY = cordY;
        self.Type = "MouseClick";

    def __str__(self):
        return "Click|(" + str(self.cordX) + "," + str(self.cordY) + ")";

    def Serialize(self):
        separator = Action.ActionSeparator;
        return self.Type + separator + str(self.cordX) + separator + str(self.cordY);

    def Deserialize(json):
        print(*json);
        cordX = int(json[1]);
        cordY = int(json[2]);
        obj = MouseClickAction(cordX, cordY);
        
        return obj;

    def OnAction(self):
        pyautogui.moveTo(self.cordX, self.cordY);
