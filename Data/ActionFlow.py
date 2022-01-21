from .Actions import Action

class ActionFlow:
    ActionList = [ ]

    def __init__(self):
        print("Initing action flow");

    def ExecuteFlow(self):
        for action in self.ActionList:
            action.OnAction();

    def AddAction(self, Action):
        self.ActionList.append(Action);
