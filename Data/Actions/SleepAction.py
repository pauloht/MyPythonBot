import pyautogui
import time;
from .Action import Action
import datetime
import random;

class SleepAction(Action):
    def __init__(self, sleepTime, sleepVar):
        Action.__init__(self);
        self.sleepTime = sleepTime;
        self.sleepVar = sleepVar;
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
        sleepVar = int(json[2]);
        obj = SleepAction(sleepTime, sleepVar);

        return obj;

    def OnAction(self):
        print("Executing sleepAction");
        sleepTime = self.sleepTime + (random.random() * 2 - 1) * self.sleepVar;
        if sleepTime <= 0:
            sleepTime = 1;
        currentTime = datetime.datetime.now()
        wakeUpTime = currentTime + datetime.timedelta(0, sleepTime) # days, seconds, then other fields.
        print("Sleeping " + str(sleepTime) + ", will wake up at : " + str(wakeUpTime));
        time.sleep(sleepTime);
