import pyautogui
from .Action import Action

class WriteAction(Action):
    Type = "KWrite"

    def __init__(self, stringToWrite):
        Action.__init__(self);
        self.Type = WriteAction.Type;
        self.stringToWrite = stringToWrite;

    def __str__(self):
        separator = Action.ActionSeparator;
        return self.Type + separator + self.stringToWrite;

    def Serialize(self):
        return self.__str__();

    def Deserialize(json):
        print(*json);
        stringToWrite = (json[1]);
        obj = WriteAction(stringToWrite);

        return obj;

    def OnAction(self):
        pyautogui.write(self.stringToWrite, interval=0.25)
