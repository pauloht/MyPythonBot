import json;
from json import JSONEncoder
from enum import Enum

class Action:
    ActionSeparator = "-";

    def __init__(self):
        print("ActionInit");
        self.Name = "Default Name";
        self.Type = "Undefined";

    def OnAction(self):
        print("No override to action");

    def Serialize(self):
        return "undefined";

    def Deserialize(json):
        return Action();
