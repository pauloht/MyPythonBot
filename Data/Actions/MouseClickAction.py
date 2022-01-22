import pyautogui
from .Action import Action

class MouseClickAction(Action):
    Type = "MouseClick"

    def __init__(self):
        Action.__init__(self);
        self.Type = MouseClickAction.Type;

    def __str__(self):
        return "Click";

    def Serialize(self):
        separator = Action.ActionSeparator;
        return self.Type;

    def Deserialize(json):
        print(*json);
        obj = MouseClickAction();

        return obj;

    def OnAction(self):
        pyautogui.click();
