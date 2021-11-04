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

# Für Customclass&Alle
import gc



## 3) Moduling Zone-----------------------------------------------------------------------------------------------------
##    

class Customclass_jomo():
    '''Superclass for all classes of this module'''

    def __init__(self):
        pass
        #

    def _reinit(self):
        self.__init__()
        #

    def _treat_demit(self, demitas='print'):
        self._htdemit=['print', 'showonscreen']
        if demitas in self._htdemit:
            self._demitas=demitas
        else:
            print("There was a mistake as the attribute 'demitas' was given. So this warning is printed. If the problem is not because of your own code, contact support.")

    def _demit(self, todemit="", _demitas=self._demitas):
        if _demitas=='print':
            print(todemit)
        if _demitas=='showonscreen':
            pass
            #Override in robotic!
        if _demitas=='':        # <- fill!
            pass
        if _demitas=='':
            pass
        if _demitas=='':
            pass
        else:
            print("There was a mistake as the attribute 'demitas' was given. So this warning is printed. If the problem is not because of your own code, contact support.")

    def _demit_warning(self, todw=101):
        self._config_warning()
        x="Warning/Error/Exeption with the Code" +str(todw) +": "
        self._demit(x)
        self._demit(self._warnings[todw])

    def _config_warning(self, add=(10000, 'Automatic! If this is printed, there is a usage or programming mistake')):
        self._warnings={}
        self._warnings.append(add)

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
        # collects all intsances of Customclass_jomo


class Attribute_jomo(Customclass_jomo):
    def __init__(self, value, kind='int'):
        '''kind can be: 'int', 'bool', 'char', 'string', 'float', 'double', 'long', 'port', 'stop',
         'direction', 'color', 'button'
        '''
        self._kinds=['int', 'bool', 'char', 'string', 'float', 'double', 'long', 'port', 'stop',
         'direction', 'color', 'button']
        self._value=value
        if kind in self._kinds:
            self._kind=kind
        else:
            del self

    def set_(self, value):
        self._value=value

    def get_val(self):
        return self._value

    def get_kin(self):
        return self._kind