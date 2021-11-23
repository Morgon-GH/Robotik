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
##         Program (x) 
##         Module  ( )



## 2) Import Zone-------------------------------------------------------------------------------------------------------
##    

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, TouchSensor, ColorSensor, InfraredSensor, UltrasonicSensor, GyroSensor
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotic import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

import threading



## 3) Definition Zone---------------------------------------------------------------------------------------------------
##    

class Strassengame(EV3Brick):

    class Straße(threading.Thread):

        def __init__(self, id="default", port=Port.A):
            threading.Thread.__init__(self)
            self.id=id
            self.mot=Motor(port)
            self.tempo_=True
            self.tempo=100
            self.hinbeschleunigen={1: 1}
        
        def run(self):
            pass

        def sethinbeschleunigen(self):
            pass

    def __init__(self):
        self.l=Straße(id="l", port=Port.A)
        self.m=Straße(id="m", port=Port.B)
        self.r=Straße(id="r", port=Port.C)

    def stelleSchnelligkeit(self):
        pass

    def play(self):
        pass



## 4) Programming Zone--------------------------------------------------------------------------------------------------
##    


