import json;
from json import JSONEncoder;
from .Actions import Action, SleepAction, MouseClickAction, MouseMoveAction, WriteAction, ImageAction

class ActionFlow:
    ActionList = [ ]
    ActionFlowSeparator = "|";

    def __init__(self):
        self.Name = "Default_Name.txt";
        print("Initing action flow");

    def ExecuteFlow(self):
        print("Executing " + self.Name + " flow");

        for action in self.ActionList:
            ret = action.OnAction();
            if (ret != None):
                break;
        return ret;

    def AddAction(self, Action):
        self.ActionList.append(Action);

    def Serialize(self):
        s = str(len(self.ActionList)) + ActionFlow.ActionFlowSeparator;

        for v in self.ActionList:
            s += v.Serialize() + ActionFlow.ActionFlowSeparator;

        return s;

    def Deserialize(json):
        first_split = json.split(ActionFlow.ActionFlowSeparator);
        _len = int(first_split[0]);
        flow = ActionFlow();
        flow.ActionList = [];
        print("Has " + str(_len) + " Actions");

        for x in range(_len):
            actionJson = first_split[x + 1];
            actionAtributes = actionJson.split(Action.Action.ActionSeparator);
            type = actionAtributes[0];
            newAction = None;

            if (type == "Sleep"):
                newAction = SleepAction.SleepAction.Deserialize(actionAtributes);
            elif (type == "MouseClick"):
                newAction = MouseClickAction.MouseClickAction.Deserialize(actionAtributes);
            elif (type == MouseMoveAction.MouseMoveAction.Type):
                newAction = MouseMoveAction.MouseMoveAction.Deserialize(actionAtributes);
            elif (type == WriteAction.WriteAction.Type):
                newAction = WriteAction.WriteAction.Deserialize(actionAtributes);
            elif (type == ImageAction.ImageAction.Type):
                newAction = ImageAction.ImageAction.Deserialize(actionAtributes);
            if (newAction != None):
                flow.ActionList.append(newAction);

        return flow;
