import pyautogui
from .Action import Action
import time;
from PIL import Image
from PIL import ImageChops

class ImageAction(Action):
    Type = "Image"

    def __init__(self, image_name, cordX, cordY, lengthX, lengthY, pulses, onFailFlow):
        Action.__init__(self);
        self.Type = ImageAction.Type;
        self.image_name = image_name;
        self.cordX = cordX;
        self.cordY = cordY;
        self.lengthX = lengthX;
        self.lengthY = lengthY;
        self.pulses = pulses;
        self.onFailFlow = onFailFlow;

    def __str__(self):
        separator = Action.ActionSeparator;
        return  (self.Type + separator + self.image_name + separator +
               str(self.cordX) + separator + str(self.cordY) + separator +
               str(self.lengthX) + separator + str(self.lengthY) + separator +
               str(self.pulses) + separator + self.onFailFlow
               );


    def Serialize(self):
        return str(self);

    def Deserialize(json):
        print(*json);
        fileName = json[1];
        cordX = int(json[2])
        cordY = int(json[3])
        lengthX = int(json[4])
        lengthY = int(json[5])
        pulses = int(json[6])
        onFailFlow = json[7];
        obj = ImageAction(fileName, cordX, cordY, lengthX, lengthY, pulses, onFailFlow);

        return obj;

    def OnAction(self):
        print("Executing image action")
        count = 0;
        while (count < self.pulses):
            on_screen = pyautogui.screenshot(region=(
                                                self.cordX,
                                                self.cordY,
                                                self.lengthX,
                                                self.lengthY
                                                ))
            on_disk = Image.open("./Images/" + self.image_name);
            diff = ImageChops.difference(on_screen, on_disk)
            if diff.getbbox():
                print("Failed " + str(count) + "/" + str(self.pulses));
            else:
                print("images are the same")
                return;
            count = count + 1
            time.sleep(1)
        return self.onFailFlow;
