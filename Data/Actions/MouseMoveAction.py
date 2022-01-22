import pyautogui
import random
from .Action import Action

class MouseMoveAction(Action):
    Type = "MMove"
    cordX = 0;
    cordY = 0;

    def __init__(self, cordX, cordY):
        random.seed();
        Action.__init__(self);
        self.cordX = cordX;
        self.cordY = cordY;
        self.Type = "MMove";
        self.jitter = 5;

    def __str__(self):
        return "MMove|(" + str(self.cordX) + "," + str(self.cordY) + ")";

    def Serialize(self):
        separator = Action.ActionSeparator;
        return self.Type + separator + str(self.cordX) + separator + str(self.cordY);

    def Deserialize(json):
        print(*json);
        cordX = int(json[1]);
        cordY = int(json[2]);
        obj = MouseMoveAction(cordX, cordY);

        return obj;

    def OnAction(self):
        pyautogui.moveTo(
            self.cordX + (random.random() * 2 - 1) * self.jitter,
            self.cordY + (random.random() * 2 - 1) * self.jitter, 2);
