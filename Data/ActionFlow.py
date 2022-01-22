import json;
from json import JSONEncoder;
from .Actions import Action, SleepAction, MouseClickAction

class ActionFlow:
    ActionList = [ ]
    ActionFlowSeparator = "|";

    def __init__(self):
        print("Initing action flow");

    def ExecuteFlow(self):
        for action in self.ActionList:
            action.OnAction();

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
            if (newAction != None):
                flow.ActionList.append(newAction);

        return flow;
