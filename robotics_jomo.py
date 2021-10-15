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

## 3) Moduling Zone-----------------------------------------------------------------------------------------------------
##    

class Robotics_jomo():
    '''Modul für eine Zentrale Robotersteuerung. Standartimports in der üblichen Ausführlichkeit benötigt.
    Preferences nutzen große Räder, im Abstand von 10cm. 
    '''

    #überschreiben
    class TouchSensor_jomo(TouchSensor):
        #fill
    

    class ColorSensor_jomo(ColorSensor):
        #fill
    

    class InfraredSensor_jomo(InfraredSensor):
        #fill
    

    class UltrasonicSensor_jomo(UltrasonicSensor):
        #fill
    

    class GyroSensor_jomo(GyroSensor):
        #fill

    
    class DriveBase_jomo(DriveBase):
        #fill
    

    class Motor_jomo(Motor):
        #fill
    

    class Extension_jomo(Motor_jomo):
        #fill
    

    def __init__(self, makeredo=True, wheel_diameter=45, axle_track=100, driveports=(Port.A, Port.D), 
    sensor={'S1': 'gyro', 'S2': 'touch', 'S3': 'touch', 'S4': 'ultrasonic'}):
        if makeredo==True:
            do=RedoINTE_jomo()
        self.a=Motor_jomo(driveports[0])
        self.b=Motor_jomo(driveports[1])
        self.DriveBase_jomo(self.a, self.b, wheel_diameter, axle_track)
        if sensor[0]=='gyro': 
            self.s1=GyroSensor_jomo(Port.S1)
        elif sensor[0]=='touch':
            self.s1=TouchSensor_jomo(Port.S1)
        elif sensor[0]=='color':
            self.s1=ColorSensor_jomo(Port.S1)
        elif sensor[0]=='infrared':
            self.s1=InfraredSensor_jomo(Port.S1)
        elif sensor[0]=='ultrasonic':
            self.s1=UltrasonicSensor_jomo(Port.S1)
        else:
            pass
        if sensor[1]=='gyro':
            self.s2=GyroSensor_jomo(Port.S2)
        elif sensor[1]=='touch':
            self.s2=TouchSensor_jomo(Port.S2)
        elif sensor[1]=='color':
            self.s2=ColorSensor_jomo(Port.S2)
        elif sensor[1]=='infrared':
            self.s2=InfraredSensor_jomo(Port.S2)
        elif sensor[1]=='ultrasonic':
            self.s2=UltrasonicSensor_jomo(Port.S2)
        else:
            pass
        if sensor[2]=='gyro':
            self.s3=GyroSensor_jomo(Port.S3)
        elif sensor[2]=='touch':
            self.s3=TouchSensor_jomo(Port.S3)
        elif sensor[2]=='color':
            self.s3=ColorSensor_jomo(Port.S3)
        elif sensor[2]=='infrared':
            self.s3=InfraredSensor_jomo(Port.S3)
        elif sensor[2]=='ultrasonic':
            self.s3=UltrasonicSensor_jomo(Port.S3)
        else:
            pass
        if sensor[3]=='gyro':
            self.s4=GyroSensor_jomo(Port.S4)
        elif sensor[3]=='touch':
            self.s4=TouchSensor_jomo(Port.S4)
        elif sensor[3]=='color':
            self.s4=ColorSensor_jomo(Port.S4)
        elif sensor[3]=='infrared':
            self.s4=InfraredSensor_jomo(Port.S4)
        elif sensor[3]=='ultrasonic':
            self.s4=UltrasonicSensor_jomo(Port.S4)
        else:
            pass

    def redo_(self, redo=1):
        if redo==0:
            do.sdo()
        elif redo==1:
            do.redo1()
        elif redo==1:
            do.redo1()
        elif redo==1:
            do.redo1()
        elif redo==1:
            do.redo1()
        elif redo==1:
            do.redo1()
        elif redo==1:
            do.redo1()
        elif redo==1:
            do.redo1()
        elif redo==1:
            do.redo1()
        elif redo==1:
            do.redo1()
        elif redo==1:
            do.redo1()