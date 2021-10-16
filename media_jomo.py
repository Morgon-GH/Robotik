## 0) Filepath----------------------------------------------------------------------------------------------------------
##    
#!/usr/bin/env pybricks-micropython

## 1) Commentation Zone-------------------------------------------------------------------------------------------------
##    
##    Author: Johannes und Moritz
##    Language: Micropython (Python) v 2.0
##    Important comments: This program requires LEGO EV3 MicroPython v2.0 or higher.
##                        Garbage Collector might needed.
##    File: 
##         Program ( ) 
##         Module  (x)
##    Version: 1.0.1
##    Click "Open user guide" on the EV3 extension tab for more information. look if own modules are needed.

## 2) Import Zone-------------------------------------------------------------------------------------------------------
##    

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, TouchSensor, ColorSensor, InfraredSensor, UltrasonicSensor, GyroSensor
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile 

import gc

## 3) Moduling Zone-----------------------------------------------------------------------------------------------------
##    

class Picturefile_jomo(Customclass_jomo):
    #fill
    def __init__(self, picture=' ', picture_=False):
        if sound_=True:
            self.picture=picture
        else:
            self.picture=' '
        ##
    
    def imp(self):
        ##

    def exp(self):
        ##


class Audiofile_jomo(Customclass_jomo):
    def __init__(self, sound=' ', sound_=False):
        if sound_=True:
            self.sound=sound
        else:
            self.sound=' '
        ##

    def play(self):
        ##

    
class Screensetter_jomo(Customclass_jomo):

    def set_surround(self, headborder=True, downborder=False, up=False, down=False):
        ##

    def inc(self, elment):
        ##