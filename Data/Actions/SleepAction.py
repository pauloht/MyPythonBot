import pyautogui
from .Action import Action

class SleepAction(Action):
    sleepTime = 1;
    sleepVar = 1;

    def __init__(self, sleepTime):
        self.sleepTime = sleepTime;

    def __str__(self):
        return "Sleep|(" + str(self.sleepTime) + " +/- " + str(self.sleepVar) + ")";

    def onAction():
        time.sleep(self.sleepTime);
