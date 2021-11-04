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
##    Version: 1.0.22 (Version.release.commit, reset per each new version and release)
##    Look for the documentation. If there are questions, write to the Support.



## 2) Import Zone-------------------------------------------------------------------------------------------------------
##    

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, TouchSensor, ColorSensor, InfraredSensor, UltrasonicSensor, GyroSensor
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotic import DriveBase
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

    def _reinit(self, sound=' ', sound_=True)

    def play(self):
        ##

    
class Screensetter_jomo(Customclass_jomo):
    def __init__(self):
        pass

    def set_surround(self, headborder=True, downborder=False, up=False, down=False):
        ##

    def inc(self, elment):
        ##