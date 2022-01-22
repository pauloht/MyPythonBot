import pyautogui
import time;
from .Action import Action

class SleepAction(Action):
    def __init__(self, sleepTime):
        Action.__init__(self);
        self.sleepTime = sleepTime;
        self.sleepVar = 1;
        self.Type = "Sleep";
        # self.Type = ActionType.SLEEP;

    def __str__(self):
        return "Sleep|(" + str(self.sleepTime) + " +/- " + str(self.sleepVar) + ")";

    def Serialize(self):
        separator = Action.ActionSeparator;
        return self.Type + separator + str(self.sleepTime) + separator + str(self.sleepVar);

    def Deserialize(json):
        print(*json);
        sleepTime = int(json[1]);
        obj = SleepAction(sleepTime);

        return obj;

    def OnAction(self):
        print("Sleeping Action");
        time.sleep(self.sleepTime);
