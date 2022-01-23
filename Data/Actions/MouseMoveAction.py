import pyautogui
import random
from .Action import Action

class MouseMoveAction(Action):
    Type = "MMove"
    cordX = 0;
    cordY = 0;

    def __init__(self, cordX, cordY, timeToMove, jitter):
        random.seed();
        Action.__init__(self);
        self.cordX = cordX;
        self.cordY = cordY;
        self.Type = "MMove";
        self.timeToMove = timeToMove;
        self.jitter = jitter;

    def __str__(self):
        return "MMove|(" + str(self.cordX) + "," + str(self.cordY) + ")";

    def Serialize(self):
        separator = Action.ActionSeparator;
        return self.Type + separator + str(self.cordX) + separator + str(self.cordY) + separator + str(self.timeToMove) + separator + str(self.jitter);

    def Deserialize(json):
        print(*json);
        cordX = int(json[1]);
        cordY = int(json[2]);
        timeToMove = int(json[3]);
        jitter = int(json[4])
        obj = MouseMoveAction(cordX, cordY, timeToMove, jitter);

        return obj;

    def OnAction(self):
        jitterX = (random.random() * 2 - 1) * self.jitter;
        jitterY = (random.random() * 2 - 1) * self.jitter;
        print("Executing mouseMoveAction");
        pyautogui.moveTo(
            self.cordX + jitterX,
            self.cordY + jitterY,self.timeToMove);
