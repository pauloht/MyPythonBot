import pyautogui
from .Action import Action
from PIL import Image
from PIL import ImageChops

class ImageAction(Action):
    Type = "Image"

    def __init__(self, image_name, cordX, cordY, lengthX, lengthY):
        Action.__init__(self);
        self.Type = ImageAction.Type;
        self.image_name = image_name;
        self.cordX = cordX;
        self.cordY = cordY;
        self.lengthX = lengthX;
        self.lengthY = lengthY;

    def __str__(self):
        separator = Action.ActionSeparator;
        return  (self.Type + separator + self.image_name + separator +
               str(self.cordX) + separator + str(self.cordY) + separator +
               str(self.lengthX) + separator + str(self.lengthY));


    def Serialize(self):
        return str(self);

    def Deserialize(json):
        print(*json);
        fileName = json[1];
        cordX = int(json[2])
        cordY = int(json[3])
        lengthX = int(json[4])
        lengthY = int(json[5])
        obj = ImageAction(fileName, cordX, cordY, lengthX, lengthY);

        return obj;

    def OnAction(self):
        on_screen = pyautogui.screenshot(region=(
                                            self.cordX,
                                            self.cordY,
                                            self.lengthX,
                                            self.lengthY
                                            ))
        on_disk = Image.open("./Images/" + self.image_name);
        diff = ImageChops.difference(on_screen, on_disk)

        if diff.getbbox():
            print("images are different")
        else:
            print("images are the same")
