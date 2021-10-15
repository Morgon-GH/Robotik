## 0) Filepath----------------------------------------------------------------------------------------------------------
##    
#!/usr/bin/env pybricks-micropython

## 1) Commentation Zone-------------------------------------------------------------------------------------------------
##    
##    Author: Johannes und Moritz
##    Language: Micropython (Python) v 2.0
##    Important comments: This program requires LEGO EV3 MicroPython v2.0 or higher.
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

class Customclass_jomo():
    '''Superclass for all classes of this module'''

    def __init__(self):
        #

    def reinit(self):
        self.__init__()
        #

    def __del__(self):
        del self
        gc=Garbage()
        if gc:
            gc.collect()
            print(b)
            gc = None
        else:
            pass
        except Exception as e:
            pass
        ##

    def reset_ns():
        # 


class Attribute_jomo(Customclass_jomo):
    def set_(self):
        ##
        pass

    def get_(self):
        ##
        pass