from .Action import Action

class PrintAction(Action):
    printMessage = "Default";

    def __init__(self, message):
        self.printMessage = message;

    def OnAction(self):
        print(self.printMessage);
