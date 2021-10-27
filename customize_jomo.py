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
##    Version: 1.0.13 (Version.release.commit, reset per each new version and release)
##    Look for the documentation. If there are questions, write to the Support.



## 2) Import Zone-------------------------------------------------------------------------------------------------------
##    

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, TouchSensor, ColorSensor, InfraredSensor, UltrasonicSensor, GyroSensor
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile 

# Für Customclass&Alle
import gc



## 3) Moduling Zone-----------------------------------------------------------------------------------------------------
##    

class Customclass_jomo():
    '''Superclass for all classes of this module'''

    def __init__(self, developement=False):
        if developement=True:
            self._printers=True
        else:
            pass
        #

    def _reinit(self):
        self.__init__()
        #

    def _printer(self, toprint='  '):
        if self._printers==True:
            print(toprint)
        else: 
            pass

    def __del__(self):
        del self
        gc=Garbage()
        if gc:
            gc.collect()
            gc = None
        else:
            pass
        except Exception as e:
            pass
        ##

    def reset_ns():
        # has to collect all objects of the kind Customclass_jomo


class Attribute_jomo(Customclass_jomo):
    # Not used now; no usage in time but might useful in other releases and for developers
    def __init__(self, value, kind='int'):
        '''kind can be: 'int', 'bool', 'char', 'string', 'float', 'double', 'long', 'port', 'stop',
         'direction', 'color', 'button'
        '''
        self.kinds=['int', 'bool', 'char', 'string', 'float', 'double', 'long', 'port', 'stop',
         'direction', 'color', 'button']
        self.value=value
        if kind==self.kinds:
            self.kind=kind
        else:
            del self

    def set_(self, value):
        self.value=value

    def get_val(self):
        return self.value

    def get_kin(self):
        return self.kind