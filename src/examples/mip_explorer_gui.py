#!/usr/bin/env python

"""
This GUI is designed for general exploration using MiP.
./mip_explorer_gui.py -i hci0 -b D0:39:72:C4:7A:01
"""
from Tkinter import *
from movement_canvas import MovementCanvas
import logging
import mippy
import argparse
import time

class SoundWindow(Toplevel):
    """
    Class to manage and control the sound window.
    """

    def __init__(self, master=None):
        Toplevel.__init__(self, master)
        #self.pack()
        self.startSoundWindow()

    def getVolume(self):
        volumeString = self.volumeEntry.get()
        volume = int(volumeString)
        return volume

    def setVolume(self):
        volume = self.getVolume()
        mip.setVolume(volume)

    def soundCallback(self,soundNumber):
        mip.playSound(soundNumber)

    def startSoundWindow(self):
        """
        Manage a sound control window
        """
        self.title("Sound Window")
        self.geometry("600x350")
        soundMenubar = Menu(self)
        soundFileMenu = Menu(soundMenubar, tearoff=0)
        soundFileMenu.add_command(label="Exit", command=self.destroy)
        soundMenubar.add_cascade(label="File", menu=soundFileMenu)
        self.config(menu=soundMenubar)
        soundFrame = Frame(self)
        soundFrame.pack()
        # Volume control
        volumeFrame = Frame(soundFrame)
        volumeFrame.pack()
        volumeButton = Button(volumeFrame, text = "Volume(0..7):", command = self.setVolume)
        volumeButton.grid(column=0,row=0)
        volumeStringVar = StringVar()
        self.volumeEntry = Entry(volumeFrame, textvariable = volumeStringVar)
        self.volumeEntry.insert(0,"1")
        self.volumeEntry.grid(column=1,row=0)
        # Add sounds
        soundsFrame1 = Frame(soundFrame)
        soundsFrame1.pack()
        button1 = Button(soundsFrame1, text ="Beep", command = lambda: self.soundCallback(1))
        button1.pack(side = LEFT)
        button2 = Button(soundsFrame1, text ="Burp", command = lambda: self.soundCallback(2))
        button2.pack(side = LEFT)
        button5 = Button(soundsFrame1, text ="Raspberry", command = lambda: self.soundCallback(5))
        button5.pack(side = LEFT)
        button14 = Button(soundsFrame1, text ="Ah! (interested)", command = lambda: self.soundCallback(14))
        button14.pack(side = LEFT)
        button15 = Button(soundsFrame1, text ="Ah! (disappointed)", command = lambda: self.soundCallback(15))
        button15.pack(side = LEFT)
        button16 = Button(soundsFrame1, text ="Oh Yeah!", command = lambda: self.soundCallback(16))
        button16.pack(side = LEFT)
        button17 = Button(soundsFrame1, text ="Meh", command = lambda: self.soundCallback(17))
        button17.pack(side = LEFT)
        soundsFrame2 = Frame(soundFrame)
        soundsFrame2.pack()
        button19 = Button(soundsFrame2, text ="See yah", command = lambda: self.soundCallback(19))
        button19.pack(side = LEFT)
        button20 = Button(soundsFrame2, text ="MiP chatter", command = lambda: self.soundCallback(20))
        button20.pack(side = LEFT)
        button22 = Button(soundsFrame2, text ="Stop", command = lambda: self.soundCallback(22))
        button22.pack(side = LEFT)
        button23 = Button(soundsFrame2, text ="Goodnight", command = lambda: self.soundCallback(23))
        button23.pack(side = LEFT)
        button26 = Button(soundsFrame2, text ="Hi Yah!", command = lambda: self.soundCallback(26))
        button26.pack(side = LEFT)
        button29 = Button(soundsFrame2, text ="Lets Go!", command = lambda: self.soundCallback(29))
        button29.pack(side = LEFT)
        soundsFrame3 = Frame(soundFrame)
        soundsFrame3.pack()
        button32 = Button(soundsFrame3, text ="Eigh (something horrible)", command = lambda: self.soundCallback(32))
        button32.pack(side = LEFT)
        button35 = Button(soundsFrame3, text ="Hellllooo", command = lambda: self.soundCallback(35))
        button35.pack(side = LEFT)
        button36 = Button(soundsFrame3, text ="Bah?", command = lambda: self.soundCallback(36))
        button36.pack(side = LEFT)
        button37 = Button(soundsFrame3, text ="Ohaye", command = lambda: self.soundCallback(37))
        button37.pack(side = LEFT)
        button38 = Button(soundsFrame3, text ="Huh?", command = lambda: self.soundCallback(38))
        button38.pack(side = LEFT)
        soundsFrame4 = Frame(soundFrame)
        soundsFrame4.pack()
        button39 = Button(soundsFrame4, text ="Mip Humming", command = lambda: self.soundCallback(39))
        button39.pack(side = LEFT)
        button40 = Button(soundsFrame4, text ="Mip Humming", command = lambda: self.soundCallback(40))
        button40.pack(side = LEFT)
        button41 = Button(soundsFrame4, text ="Mip Laughing", command = lambda: self.soundCallback(41))
        button41.pack(side = LEFT)
        button42 = Button(soundsFrame4, text ="Heaaahhh", command = lambda: self.soundCallback(42))
        button42.pack(side = LEFT)
        button43 = Button(soundsFrame4, text ="Harp sound", command = lambda: self.soundCallback(43))
        button43.pack(side = LEFT)
        button44 = Button(soundsFrame4, text ="Lets MiP", command = lambda: self.soundCallback(44))
        button44.pack(side = LEFT)
        soundsFrame5 = Frame(soundFrame)
        soundsFrame5.pack()
        button45 = Button(soundsFrame5, text ="MiP chatter", command = lambda: self.soundCallback(45))
        button45.pack(side = LEFT)
        button46 = Button(soundsFrame5, text ="'kay", command = lambda: self.soundCallback(46))
        button46.pack(side = LEFT)
        button47 = Button(soundsFrame5, text ="Music (verse 1)", command = lambda: self.soundCallback(47))
        button47.pack(side = LEFT)
        button48 = Button(soundsFrame5, text ="Music (verse 2)", command = lambda: self.soundCallback(48))
        button48.pack(side = LEFT)
        button49 = Button(soundsFrame5, text ="Out of power", command = lambda: self.soundCallback(49))
        button49.pack(side = LEFT)
        button50 = Button(soundsFrame5, text ="Happy", command = lambda: self.soundCallback(50))
        button50.pack(side = LEFT)
        soundsFrame6 = Frame(soundFrame)
        soundsFrame6.pack()
        button51 = Button(soundsFrame6, text ="Yeuh", command = lambda: self.soundCallback(51))
        button51.pack(side = LEFT)
        button53 = Button(soundsFrame6, text ="Music", command = lambda: self.soundCallback(53))
        button53.pack(side = LEFT)
        button54 = Button(soundsFrame6, text ="Oh ah", command = lambda: self.soundCallback(54))
        button54.pack(side = LEFT)
        button55 = Button(soundsFrame6, text ="Oh oh (bad)", command = lambda: self.soundCallback(55))
        button55.pack(side = LEFT)
        button56 = Button(soundsFrame6, text ="Oh yeah!", command = lambda: self.soundCallback(56))
        button56.pack(side = LEFT)
        button58 = Button(soundsFrame6, text ="Howell", command = lambda: self.soundCallback(58))
        button58.pack(side = LEFT)
        button60 = Button(soundsFrame6, text ="Play", command = lambda: self.soundCallback(60))
        button60.pack(side = LEFT)
        soundsFrame7 = Frame(soundFrame)
        soundsFrame7.pack()
        button61 = Button(soundsFrame7, text ="Lets fish", command = lambda: self.soundCallback(61))
        button61.pack(side = LEFT)
        button62 = Button(soundsFrame7, text ="Fire", command = lambda: self.soundCallback(62))
        button62.pack(side = LEFT)
        button64 = Button(soundsFrame7, text ="Rar", command = lambda: self.soundCallback(64))
        button64.pack(side = LEFT)
        button65 = Button(soundsFrame7, text ="La la la la la (derogatory)", command = lambda: self.soundCallback(65))
        button65.pack(side = LEFT)
        button66 = Button(soundsFrame7, text ="Ah-choo", command = lambda: self.soundCallback(66))
        button66.pack(side = LEFT)
        button67 = Button(soundsFrame7, text ="Snoring", command = lambda: self.soundCallback(67))
        button67.pack(side = LEFT)
        button68 = Button(soundsFrame7, text ="Feck", command = lambda: self.soundCallback(68))
        button68.pack(side = LEFT)
        soundsFrame8 = Frame(soundFrame)
        soundsFrame8.pack()
        button72 = Button(soundsFrame8, text ="Lets trick", command = lambda: self.soundCallback(72))
        button72.pack(side = LEFT)
        button73 = Button(soundsFrame8, text ="duh duh duh (cage escape sound)", command = lambda: self.soundCallback(73))
        button73.pack(side = LEFT)
        button74 = Button(soundsFrame8, text ="Waaah", command = lambda: self.soundCallback(74))
        button74.pack(side = LEFT)
        button75 = Button(soundsFrame8, text ="Wakey Wakey", command = lambda: self.soundCallback(75))
        button75.pack(side = LEFT)
        button76 = Button(soundsFrame8, text ="Yay", command = lambda: self.soundCallback(76))
        button76.pack(side = LEFT)
        button77 = Button(soundsFrame8, text ="Roam whistle", command = lambda: self.soundCallback(77))
        button77.pack(side = LEFT)
        soundsFrame9 = Frame(soundFrame)
        soundsFrame9.pack()
        button82 = Button(soundsFrame9, text ="You", command = lambda: self.soundCallback(82))
        button82.pack(side = LEFT)
        button86 = Button(soundsFrame9, text ="Ribit", command = lambda: self.soundCallback(86))
        button86.pack(side = LEFT)
        button87 = Button(soundsFrame9, text ="Boring", command = lambda: self.soundCallback(87))
        button87.pack(side = LEFT)
        button89 = Button(soundsFrame9, text ="Lets Go", command = lambda: self.soundCallback(89))
        button89.pack(side = LEFT)
        soundsFrame10 = Frame(soundFrame)
        soundsFrame10.pack()
        button90 = Button(soundsFrame10, text ="Yipppee!", command = lambda: self.soundCallback(90))
        button90.pack(side = LEFT)
        button91 = Button(soundsFrame10, text ="ho ho ho ho ho", command = lambda: self.soundCallback(91))
        button91.pack(side = LEFT)
        button93 = Button(soundsFrame10, text ="Crafty", command = lambda: self.soundCallback(93))
        button93.pack(side = LEFT)
        button94 = Button(soundsFrame10, text ="Ha ha", command = lambda: self.soundCallback(94))
        button94.pack(side = LEFT)
        button95 = Button(soundsFrame10, text ="This is MiP", command = lambda: self.soundCallback(95))
        button95.pack(side = LEFT)
        button97 = Button(soundsFrame10, text ="Crying", command = lambda: self.soundCallback(97))
        button97.pack(side = LEFT)
        soundsFrame11 = Frame(soundFrame)
        soundsFrame11.pack()
        button101 = Button(soundsFrame11, text ="Beeping", command = lambda: self.soundCallback(101))
        button101.pack(side = LEFT)
        button103 = Button(soundsFrame11, text ="Laser Beam", command = lambda: self.soundCallback(103))
        button103.pack(side = LEFT)
        button104 = Button(soundsFrame11, text ="Swanny whistle", command = lambda: self.soundCallback(104))
        button104.pack(side = LEFT)
        button106 = Button(soundsFrame11, text ="MiP", command = lambda: self.soundCallback(106))
        button106.pack(side = LEFT)

class ModeWindow(Toplevel):
    """
    Class to manage and control the mode dialog. Used for chagning MiPs mode in and out of App.
    """

    def __init__(self, master=None):
        Toplevel.__init__(self, master)
        self.startModeWindow()

    def startModeWindow(self):
        self.title("Mode Window")
        self.geometry("200x100")
        modeMenubar = Menu(self)
        modeFileMenu = Menu(modeMenubar, tearoff=0)
        modeFileMenu.add_command(label="Exit", command=self.destroy)
        modeMenubar.add_cascade(label="File", menu=modeFileMenu)
        self.config(menu=modeMenubar)
        modeFrame = Frame(self)
        modeFrame.pack()
        self.modeVar = IntVar()
        self.modeVar.set(0x1) # We are by default in App mode
        appRadio = Radiobutton(modeFrame, text="App", variable=self.modeVar, value=0x1, 
                               command=self.modeSelected)
        appRadio.pack(side=TOP)
        danceRadio = Radiobutton(modeFrame, text="Dance", variable=self.modeVar, value=0x4, 
                                 command=self.modeSelected)
        danceRadio.pack(side=TOP)
        defaultRadio = Radiobutton(modeFrame, text="Default", variable=self.modeVar, value=0x5, 
                                 command=self.modeSelected)
        defaultRadio.pack(side=TOP)
        roamRadio = Radiobutton(modeFrame, text="Roam", variable=self.modeVar, value=0x8, 
                                 command=self.modeSelected)
        roamRadio.pack(side=TOP)

    def modeSelected(self):
        mip.setGameMode(self.modeVar.get())


class EyesWindow(Toplevel):
    """
    Class to manage and control the eyes.
    """

    def __init__(self, master=None):
        Toplevel.__init__(self, master)
        self.startEyesWindow()

    def startEyesWindow(self):
        self.title("Eyes Window")
        self.geometry("400x100")
        eyesMenubar = Menu(self)
        eyesFileMenu = Menu(eyesMenubar, tearoff=0)
        eyesFileMenu.add_command(label="Exit", command=self.destroy)
        eyesMenubar.add_cascade(label="File", menu=eyesFileMenu)
        self.config(menu=eyesMenubar)
        eyesFrame = Frame(self)
        eyesFrame.pack()
        self.leftEyeLeftVar = StringVar()
        self.leftEyeLeftVar.set("on")
        self.leftEyeRightVar = StringVar()
        self.leftEyeRightVar.set("on")
        self.rightEyeLeftVar = StringVar()
        self.rightEyeLeftVar.set("on")
        self.rightEyeRightVar = StringVar()
        self.rightEyeRightVar.set("on")
        self.leftEyeLeftOption = OptionMenu(eyesFrame, self.leftEyeLeftVar,
                                       "off", "on", "slow blink", "fast blink", 
                                       command=self.updateEyes)
        self.leftEyeLeftOption.grid(column=0,row=0)
        self.leftEyeRightOption = OptionMenu(eyesFrame, self.leftEyeRightVar,
                                        "off", "on", "slow blink", "fast blink", 
                                       command=self.updateEyes)
        self.leftEyeRightOption.grid(column=1,row=0)
        self.rightEyeLeftOption = OptionMenu(eyesFrame,self.rightEyeLeftVar,
                                        "off", "on", "slow blink", "fast blink", 
                                       command=self.updateEyes)
        self.rightEyeLeftOption.grid(column=2,row=0)
        self.rightEyeRightOption = OptionMenu(eyesFrame,self.rightEyeRightVar,
                                         "off","on", "slow blink", "fast blink", 
                                       command=self.updateEyes)
        self.rightEyeRightOption.grid(column=3,row=0)
        leftWinkButton = Button(eyesFrame, text = "Wink", command = lambda: self.winkEyes(0x0))
        leftWinkButton.grid(column=0,row=1)
        rightWinkButton = Button(eyesFrame, text = "Wink", command = lambda: self.winkEyes(0x1))
        rightWinkButton.grid(column=3,row=1)

    def updateEyes(self,value):
        """
        Based on the eyes window per-eye option menus, update MiPs eyes
        """
        #leftEyeLeftString = self.leftEyeLeftVar.get()
        #logging.debug('updateEyes : leftEyeLeftString = %s' % (leftEyeLeftString))
        #leftEyeLeftInt = self.optionToInt(leftEyeLeftString)
        #logging.debug('updateEyes : leftEyeLeftInt = %d' % (leftEyeLeftInt))
        leftEyeLeft = self.optionToInt(self.leftEyeLeftVar.get())
        leftEyeRight = self.optionToInt(self.leftEyeRightVar.get())
        rightEyeLeft = self.optionToInt(self.rightEyeLeftVar.get())
        rightEyeRight = self.optionToInt(self.rightEyeRightVar.get())
        mip.setHeadLed(leftEyeLeft,leftEyeRight,rightEyeLeft,rightEyeRight)

    def optionToInt(self,s):
        """
        Convert an option menu string to an integer value suitable for setHeadLed i.e.
        "off" returns 0
        "on" returns 1
        "slow blink" returns 2
        "fast blink" returns 3
        """
        if s == "off":
            return 0
        elif s == "on":
            return 1
        elif s == "slow blink":
            return 2
        elif s == "fast blink":
            return 3
        else:
            return 0
            
    def winkEyes(self,eye=0x1):
        """
        Wink an eye.
        eye=0x0 left eye
        eye=0x1 right eye
        """
        # all on
        mip.setHeadLed(0x1,0x1,0x1,0x1)
        time.sleep(1.0)
        # first half
        if eye == 1:
            mip.setHeadLed(0x1,0x1,0x1,0x0)
        else:
            mip.setHeadLed(0x0,0x1,0x1,0x1)
        time.sleep(0.2)
        # wink
        if eye == 1:
            mip.setHeadLed(0x1,0x1,0x0,0x0)
        else:
            mip.setHeadLed(0x0,0x0,0x1,0x1)
        time.sleep(1.0)
        # second half
        if eye == 1:
            mip.setHeadLed(0x1,0x1,0x1,0x0)
        else:
            mip.setHeadLed(0x0,0x1,0x1,0x1)
        time.sleep(0.2)
        # all on
        mip.setHeadLed(0x1,0x1,0x1,0x1)

class ChestWindow(Toplevel):
    """
    Class to manage and control the chest LED.
    """
    global updateChestLed
    updateChestLed = 0

    def __init__(self, master=None):
        Toplevel.__init__(self, master)
        self.startChestWindow()

    def getRedValue(self):
        """
        Get the Red Value from the red Entry / redVar,
        and convert it into a float
        Returns the red value
        """
        redString = self.redVar.get()
        try:
            redValue = float(redString)
        except ValueError:
            print "ChestWindow: Red Value not a valid float:Changing to 0.0"
            self.redVar.set("0.0")
            redValue = 0.0
        return redValue

    def getGreenValue(self):
        """
        Get the Green Value from the green Entry / redVar,
        and convert it into a float.
        Returns the green value
        """
        greenString = self.greenVar.get()
        try:
            greenValue = float(greenString)
        except ValueError:
            print "ChestWindow: Green Value not a valid float:Changing to 0.0"
            self.greenVar.set("0.0")
            greenValue = 0.0
        return greenValue

    def getBlueValue(self):
        """
        Get the Blue Value from the blue Entry / blueVar,
        and convert it into a float
        Returns the blue value
        """
        blueString = self.blueVar.get()
        try:
            blueValue = float(blueString)
        except ValueError:
            print "ChestWindow: Blue Value not a valid float:Changing to 0.0"
            self.blueVar.set("0.0")
            blueValue = 0.0
        return blueValue

    def getIncRedValue(self):
        """
        Get the Red increment Value from the red increment Entry / incRedVar,
        and convert it into a float
        Returns the red increment value
        """
        redString = self.incRedVar.get()
        try:
            incRedValue = float(redString)
        except ValueError:
            print "ChestWindow: Red Increment Value not a valid float:Changing to 0.0"
            self.incRedVar.set("0.0")
            incRedValue = 0.0
        return incRedValue

    def getIncGreenValue(self):
        """
        Get the Green increment Value from the green increment Entry / incGreenVar,
        and convert it into a float
        Returns the green increment value
        """
        greenString = self.incGreenVar.get()
        try:
            incGreenValue = float(greenString)
        except ValueError:
            print "ChestWindow: Green Increment Value not a valid float:Changing to 0.0"
            self.incGreenVar.set("0.0")
            incGreenValue = 0.0
        return incGreenValue

    def getIncBlueValue(self):
        """
        Get the Blue increment Value from the blue increment Entry / incBlueVar,
        and convert it into a float
        Returns the blue increment value
        """
        blueString = self.incBlueVar.get()
        try:
            incBlueValue = float(blueString)
        except ValueError:
            print "ChestWindow: Blue Increment Value not a valid float:Changing to 0.0"
            self.incBlueVar.set("0.0")
            incBlueValue = 0.0
        return incBlueValue

    def setChestLed(self):
        """
        Get the current values from the red/green/blue entrys (via redVar/greenVar/blueVar)
        Call mip.setChestLed to update MiPs chest LED colour.
        """
        redValue = self.getRedValue()
        greenValue = self.getGreenValue()
        blueValue = self.getBlueValue()
        mip.setChestLed(redValue,greenValue,blueValue)

    def update(self):
        """
        Called when the update button is clicked.
        Also called from main update if increments are non-zero
        See updateChestLed
        """
        global updateChestLed

        incRed = self.getIncRedValue()
        incGreen = self.getIncGreenValue()
        incBlue = self.getIncBlueValue()
        if (incRed != 0.0) or (incGreen != 0.0) or (incBlue != 0.0):
            updateChestLed = 1
        else:
            updateChestLed = 0
        # If incRed/incGreen/incBlue are non-zero increment redVar/greenVar/blueVar
        r = self.getRedValue()+incRed
        g = self.getGreenValue()+incGreen
        b = self.getBlueValue()+incBlue
        # range check results (0..1)
        # red 
        if r < 0.0 :
            if self.invertRed.get() == 1:
                r = -r
                self.incRedVar.set(-incRed)
            else:
                r += 1.0
        if r > 1.0:
            if self.invertRed.get() == 1:
                r = 1.0-(r-1.0)
                self.incRedVar.set(-incRed)
            else:
                r -= 1.0
        # green
        if g < 0.0 :
            if self.invertGreen.get() == 1:
                g = -g
                self.incGreenVar.set(-incGreen)
            else:
                g += 1.0
        if g > 1.0:
            if self.invertGreen.get() == 1:
                g = 1.0-(g-1.0)
                self.incGreenVar.set(-incGreen)
            else:
                g -= 1.0
        # blue
        if b < 0.0 :
            if self.invertBlue.get() == 1:
                b = -b
                self.incBlueVar.set(-incBlue)
            else:
                b += 1.0
        if b > 1.0:
            if self.invertBlue.get() == 1:
                b = 1.0-(b-1.0)
                self.incBlueVar.set(-incBlue)
            else:
                b -= 1.0
        # update rgb
        self.redVar.set(r)
        self.greenVar.set(g)
        self.blueVar.set(b)
        # set chest LED
        self.setChestLed()

    def setColour(self,r,g,b):
        """
        Set the Chest LED to a set colour.
        This routine called from a button
        """
        # update rgb text boxes
        self.redVar.set(r)
        self.greenVar.set(g)
        self.blueVar.set(b)
        # set chest LED
        self.setChestLed()


    def startChestWindow(self):
        self.title("Chest LED Window")
        self.geometry("350x225")
        chestMenubar = Menu(self)
        chestFileMenu = Menu(chestMenubar, tearoff=0)
        chestFileMenu.add_command(label="Exit", command=self.destroy)
        chestMenubar.add_cascade(label="File", menu=chestFileMenu)
        self.config(menu=chestMenubar)
        chestFrame = Frame(self)
        chestFrame.pack()
        self.redVar = StringVar()
        self.redVar.set("0.0")
        self.greenVar = StringVar()
        self.greenVar.set("1.0")
        self.blueVar = StringVar()
        self.blueVar.set("0.0")
        redLabel = Label(chestFrame, text = "Red(0..1):")
        redLabel.grid(column=1,row=1)
        greenLabel = Label(chestFrame, text = "Green(0..1):")
        greenLabel.grid(column=2,row=1)
        blueLabel = Label(chestFrame, text = "Blue(0..1):")
        blueLabel.grid(column=3,row=1)
        redEntry = Entry(chestFrame, textvariable=self.redVar, width=4)
        redEntry.grid(column=1,row=2)
        greenEntry = Entry(chestFrame, textvariable=self.greenVar, width=4)
        greenEntry.grid(column=2,row=2)
        blueEntry = Entry(chestFrame, textvariable=self.blueVar, width=4)
        blueEntry.grid(column=3,row=2)
        updateButton = Button(chestFrame, text = "Update", command = self.update)
        updateButton.grid(column=2,row=3)
        incrementLabel = Label(chestFrame, text = "Increment")
        incrementLabel.grid(column=2,row=4)
        self.incRedVar = StringVar()
        self.incRedVar.set("0.0")
        self.incGreenVar = StringVar()
        self.incGreenVar.set("0.0")
        self.incBlueVar = StringVar()
        self.incBlueVar.set("0.0")
        incRedEntry = Entry(chestFrame, textvariable=self.incRedVar, width=4)
        incRedEntry.grid(column=1,row=5)
        incGreenEntry = Entry(chestFrame, textvariable=self.incGreenVar, width=4)
        incGreenEntry.grid(column=2,row=5)
        incBlueEntry = Entry(chestFrame, textvariable=self.incBlueVar, width=4)
        incBlueEntry.grid(column=3,row=5)
        self.invertRed = IntVar()
        invertRedCheckButton = Checkbutton(chestFrame,text = "Invert",variable = self.invertRed,onvalue = 1,offvalue = 0)
        invertRedCheckButton.grid(column=1,row=6)
        self.invertGreen = IntVar()
        invertGreenCheckButton = Checkbutton(chestFrame,text = "Invert",variable = self.invertGreen,
                                             onvalue = 1,offvalue = 0)
        invertGreenCheckButton.grid(column=2,row=6)
        self.invertBlue = IntVar()
        invertBlueCheckButton = Checkbutton(chestFrame,text = "Invert",variable = self.invertBlue,onvalue = 1,offvalue = 0)
        invertBlueCheckButton.grid(column=3,row=6)
        redButton = Button(chestFrame, text = "Red", command = lambda: self.setColour(1.0,0.0,0.0))
        redButton.grid(column=1,row=7)
        greenButton = Button(chestFrame, text = "Green", command = lambda: self.setColour(0.0,1.0,0.0))
        greenButton.grid(column=2,row=7)
        blueButton = Button(chestFrame, text = "Blue", command = lambda: self.setColour(0.0,0.0,1.0))
        blueButton.grid(column=3,row=7)
        yellowButton = Button(chestFrame, text = "Yellow", command = lambda: self.setColour(1.0,1.0,0.0))
        yellowButton.grid(column=1,row=8)
        cyanButton = Button(chestFrame, text = "Cyan", command = lambda: self.setColour(0.0,1.0,1.0))
        cyanButton.grid(column=2,row=8)
        magentaButton = Button(chestFrame, text = "Magenta", command = lambda: self.setColour(1.0,0.0,1.0))
        magentaButton.grid(column=3,row=8)
        blackButton = Button(chestFrame, text = "Black", command = lambda: self.setColour(0.0,0.0,0.0))
        blackButton.grid(column=1,row=9)
        whiteButton = Button(chestFrame, text = "White", command = lambda: self.setColour(1.0,1.0,1.0))
        whiteButton.grid(column=3,row=9)


class TelemetryWindow(Toplevel):
    """
    Class to manage and control the mode dialog. Used for chagning MiPs mode in and out of App.
    """
    global updateTelemetry
    global distanceValueLabel
    global batteryValueLabel
    updateTelemetry = 0

    def __init__(self, master=None):
        Toplevel.__init__(self, master)
        self.startTelemetryWindow()

    def startTelemetryWindow(self):
        global updateTelemetry
        global distanceValueLabel
        global batteryValueLabel
        global orientationValueLabel
        self.title("Telemetry Window")
        self.geometry("300x300")
        telemetryMenubar = Menu(self)
        telemetryFileMenu = Menu(telemetryMenubar, tearoff=0)
        telemetryFileMenu.add_command(label="Exit", command=self.stopTelemetryWindow)
        telemetryMenubar.add_cascade(label="File", menu=telemetryFileMenu)
        self.config(menu=telemetryMenubar)
        telemetryFrame = Frame(self)
        telemetryFrame.pack()
        updateTelemetry = 1
        # orientation
        orientationLabel = Label(telemetryFrame, text = "Orientation:")
        orientationLabel.grid(column=0,row=0)
        orientationValueLabel = Label(telemetryFrame, text = "Upright")
        orientationValueLabel.grid(column=1,row=0)
        # battery level
        batteryLabel = Label(telemetryFrame, text = "Battery(v):")
        batteryLabel.grid(column=0,row=1)
        batteryValueLabel = Label(telemetryFrame, text = "0.0")
        batteryValueLabel.grid(column=1,row=1)
        # distance
        resetOdometerButton = Button(telemetryFrame, text = "Reset", command = self.resetOdometer)
        resetOdometerButton.grid(column=0,row=2)
        distanceLabel = Label(telemetryFrame, text = "Distance(cm):")
        distanceLabel.grid(column=1,row=2)
        distanceValueLabel = Label(telemetryFrame, text = "0.0")
        distanceValueLabel.grid(column=2,row=2)

    def stopTelemetryWindow(self):
        global updateTelemetry
        updateTelemetry = 0
        self.destroy()

    def resetOdometer(self):
        mip.resetOdomemeter()

def getDistance():
    distanceString = distanceEntry.get()
    distance = float(distanceString)
    # distance = 3.0 causes MiP to spin instead - number overflow?
    if distance > 2.5:
        distance = 2.5
    return distance

def getAngle():
    angleString = angleEntry.get()
    angle = int(angleString)
    return angle

def getSpeed():
    speedString = speedEntry.get()
    speed = int(speedString)
    return speed

def forwardCallBack():
    distance = getDistance()
    mip.distanceDrive(distance=distance)

def backwardCallBack():
    distance = getDistance()
    mip.distanceDrive(distance=-distance)

def forwardRadarCallBack():
    speed = getSpeed()
    mip.continuousDriveForwardUntilRadar(speed=speed)

def leftCallBack():
    angle = getAngle()
    mip.turnByAngle(angle=-angle)

def rightCallBack():
    angle = getAngle()
    mip.turnByAngle(angle=angle)

def startSoundWindow():
    soundWindow = SoundWindow()

def startTelemetryWindow():
    """
    Manage a telemetry window
    """
    telemetryWindow = TelemetryWindow()

def startModeWindow():
    """
    Manage a mode changing window
    """
# move MiP in and out of computer control, allow selection of roam and music modes
    modeWindow = ModeWindow()

def startEyesWindow():
    """
    Manage an eyes control window
    """
    eyesWindow = EyesWindow()

def startChestWindow():
    """
    Manage the Chest LED control window
    """
    global chestWindow
    chestWindow = ChestWindow()

def updateLoop():
    """
    Top-level update loop.
    Called by Tk every 50ms
    Calls updateMovement to drive MiP in continuous drive mode if applicable
    Updates Telemetry data if the telemetry window is open
    Updates Chest LED if increments are set
    """
    global updateTelemetry
    global lastOrientationUpdateTime
    global lastDistanceUpdateTime
    global lastBatteryUpdateTime
    global distanceValueLabel
    global batteryValueLabel
    global orientationValueLabel
    global updateChestLed

    updateMovement()
    thisTime = time.time()
    if(updateTelemetry == 1):
        #logging.debug('updateLoop : updateTelemetry = 1')
        if((thisTime - lastOrientationUpdateTime) > 1.0):
            #logging.debug('updateLoop : Attempting orientation update')
            orientation = mip.getMiPOrientationStatus()
            orientationString = ['on back' , 'face down' , 'upright' , 'picked up',
                                 'hand stand' , 'face down on tray' , 
                                 'on back with kickstand' ]
            #logging.debug('updateLoop : Orientation = %s ' % (orientationString[orientation]))
            orientationValueLabel.config(text=orientationString[orientation])
            if(orientation == 2):
                orientationValueLabel.config(background='green')
            else:
                orientationValueLabel.config(background='red')
            lastOrientationUpdateTime = thisTime
        if((thisTime - lastDistanceUpdateTime) > 10.0):
            #logging.debug('updateLoop : Attempting distance update')
            distance = mip.getOdometer()
            #logging.debug('updateLoop : Distance = %f cm' % (distance))
#            distanceValueLabel.config(text=str(distance))
            distanceValueLabel.config(text=("%.2f" % distance).strip())
            lastDistanceUpdateTime = thisTime
        if((thisTime - lastBatteryUpdateTime) > 60.0):
            #logging.debug('updateLoop : Attempting battery level update')
            batteryLevel = mip.getBatteryLevel()
            #logging.debug('updateLoop : Battery Level = %f v' % (batteryLevel))
#            batteryValueLabel.config(text=str(batteryLevel))
            batteryValueLabel.config(text=("%.2f" % batteryLevel).strip())
            lastBatteryUpdateTime = thisTime
    if updateChestLed == 1:
        chestWindow.update()
    finishTime = time.time()
    # calculate elapsed time in milliseconds
    elapsedTime = (int)((finishTime-thisTime)*1000.0)
    # nextUpdateTime in milliseconds
    nextUpdateTime = (int)(50-elapsedTime)
    # make sure we pause at least 1ms
    if nextUpdateTime < 1:
        nextUpdateTime = 1
    if elapsedTime > 1:
        logging.debug('updateLoop: elapsed time %d ms, next update in %d ms' % (elapsedTime,nextUpdateTime))
    root.after(nextUpdateTime,updateLoop)

def updateMovement():
    """
    Called to read current pointer position from the movement canvas
    and drive MiP in continuous drive mode based on it's potision.
    If the magnitude of movement is small, leave MiP and do not drive him
    """
    # movementCanvas.positionX,movementCanvas.positionY, (-50 - 50)
    # movementCanvas.positionAngle,movementCanvas.positionMagnitude
    if movementCanvas.positionMagnitude > 10:
        forwardSpeed = int((-movementCanvas.positionY * 0x20)/50)
        turnSpeed = int((movementCanvas.positionX * 0x20)/50)
        logging.debug('updateMovement : forwardSpeed %d : turnSpeed %d' % (forwardSpeed,turnSpeed))
        mip.continuousDrive(forwardSpeed,turnSpeed)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='MiP Exploration GUI.')
    mippy.add_arguments(parser)
    args = parser.parse_args()
    logging.basicConfig(level=logging.DEBUG)
    gt = mippy.GattTool(args.adaptor, args.device)
    mip = mippy.Mip(gt)
    # initialise some global variables
    lastBatteryUpdateTime = 0.0
    lastDistanceUpdateTime = 0.0
    lastOrientationUpdateTime = 0.0
    # start gui
    root = Tk()
    root.title("MiP Explorer GUI")
    root.geometry("600x300")
    #logging.debug('main:1')

    menubar = Menu(root)
    fileMenu = Menu(menubar, tearoff=0)
    fileMenu.add_command(label="Exit", command=root.quit)
    menubar.add_cascade(label="File", menu=fileMenu)
    windowMenu = Menu(menubar, tearoff=0)
    windowMenu.add_command(label="Sound", command=startSoundWindow)
    windowMenu.add_command(label="Telemetry", command=startTelemetryWindow)
    windowMenu.add_command(label="Mode", command=startModeWindow)
    windowMenu.add_command(label="Eyes", command=startEyesWindow)
    windowMenu.add_command(label="Chest", command=startChestWindow)
    menubar.add_cascade(label="Window", menu=windowMenu)
    root.config(menu=menubar)

    #logging.debug('main:2')
    rootFrame = Frame(root)
    rootFrame.grid(column=0,row=1)
    
    #logging.debug('main:3')
    # Fixed drive GUI
    fixedDriveFrame = Frame(rootFrame)
    fixedDriveFrame.grid(column=0,row=0)
    configFrame = Frame(fixedDriveFrame)
    configFrame.grid(column=0,row=0)

    #logging.debug('main:4')
    labeld = Label(configFrame, text = "Distance(m):")
    labeld.grid(column=0,row=0)

    distanceStringVar = StringVar()
    distanceEntry = Entry(configFrame, textvariable = distanceStringVar)
    distanceEntry.insert(0,"0.1")
    distanceEntry.grid(column=1,row=0)

    labela = Label(configFrame, text = "Angle(deg):")
    labela.grid(column=0,row=1)

    angleStringVar = StringVar()
    angleEntry = Entry(configFrame, textvariable = angleStringVar )
    angleEntry.insert(0,"90")
    angleEntry.grid(column=1,row=1)

    labels = Label(configFrame, text = "Speed(1-32):")
    labels.grid(column=0,row=2)

    speedStringVar = StringVar()
    speedEntry = Entry(configFrame, textvariable = speedStringVar )
    speedEntry.insert(0,"10")
    speedEntry.grid(column=1,row=2)

    controlFrame = Frame(fixedDriveFrame)
    controlFrame.grid(column=0,row=1)

    buttonf = Button(controlFrame, text="F", command=forwardCallBack)
    buttonf.grid(column=1,row=0)

    buttonf = Button(controlFrame, text="FR", command=forwardRadarCallBack)
    buttonf.grid(column=1,row=1)

    buttonb = Button(controlFrame, text="B", command=backwardCallBack)
    buttonb.grid(column=1,row=2)

    buttonl = Button(controlFrame, text="L", command=leftCallBack)
    buttonl.grid(column=0,row=1)

    buttonr = Button(controlFrame, text="R", command=rightCallBack)
    buttonr.grid(column=2,row=1)

    quitButton = Button(controlFrame, text='Quit', command=root.destroy)
    quitButton.grid(column=1,row=3)

    #logging.debug('main:5')
    # movement canvas (continuous drive mode)
    movementCanvas = MovementCanvas(rootFrame,300,300)
    movementCanvas.canvas.grid(column=1,row=0)
    movementCanvas.setBindings()
    # Initialise odometer
    mip.resetOdomemeter()

    #logging.debug('main:6')
    root.after(50,updateLoop)
    #logging.debug('main:7')
    root.mainloop()
