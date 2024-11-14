class Device:
    def __init__(self, height, width, name):

       self.height = height 
       self.width = width
       self.name = name

    def powerOn(self):

        print("Power is turning on...")

class Computer(Device):

    def powerOn(self):
        
        print("The power light of the computer is glowing green...")

    def powerOff(self):

        print("The power light of the computer is now glowing red...")

    def display(self):

        print("The monitor of the screen is now displaying a photo...")


    