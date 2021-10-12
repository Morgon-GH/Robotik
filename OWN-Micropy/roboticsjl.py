## 0) Filepath----------------------------------------------------------------------------------------------------------
##    
#!/usr/bin/env pybricks-micropython

## 1) Commentation Zone-------------------------------------------------------------------------------------------------
##    
##    Author: Johannes (L)
##    Language: Micropython (Python) v 2.0
##    Important comments: This program requires LEGO EV3 MicroPython v2.0 or higher.
##    File: 
##         Program ( ) 
##         Module  (x)
##    Version: 1.0
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

class Roboticsjl():
    '''Modul für eine Zentrale Robotersteuerung. Standartimports in der üblichen Ausführlichkeit benötigt.
    Preferences nutzen große Räder, im Abstand von 10cm. 
    '''

    #überschreiben
    class TouchSensorjl(TouchSensor):
        #fill
    

    class ColorSensorjl(ColorSensor):
        #fill
    

    class InfraredSensorjl(InfraredSensor):
        #fill
    

    class UltrasonicSensorjl(UltrasonicSensor):
        #fill
    

    class GyroSensorjl(GyroSensor):
        #fill

    
    class DriveBasejl(DriveBase):
        #fill
    

    class Motorjl(Motor):
        #fill
    

    class Extensionjl(Motorjl):
        #fill
    

    def __init__(self, makeredo=True, wheel_diameter=45, axle_track=100, driveports=(Port.A, Port.D), 
    sensor={'S1': 'gyro', 'S2': 'touch', 'S3': 'touch', 'S4': 'ultrasonic'}):
        self.a=Motorjl(driveports[0])
        self.b=Motorjl(driveports[1])
        self.DriveBasejl(self.a, self.b, wheel_diameter, axle_track)
        if sensor[0]=='gyro': 
            self.s1=GyroSensorjl(Port.S1)
        elif sensor[0]=='touch':
            self.s1=TouchSensorjl(Port.S1)
        elif sensor[0]=='color':
            self.s1=ColorSensorjl(Port.S1)
        elif sensor[0]=='infrared':
            self.s1=InfraredSensorjl(Port.S1)
        elif sensor[0]=='ultrasonic':
            self.s1=UltrasonicSensorjl(Port.S1)
        else:
            pass
        if sensor[1]=='gyro':
            self.s2=GyroSensorjl(Port.S2)
        elif sensor[1]=='touch':
            self.s2=TouchSensorjl(Port.S2)
        elif sensor[1]=='color':
            self.s2=ColorSensorjl(Port.S2)
        elif sensor[1]=='infrared':
            self.s2=InfraredSensorjl(Port.S2)
        elif sensor[1]=='ultrasonic':
            self.s2=UltrasonicSensorjl(Port.S2)
        else:
            pass
        if sensor[2]=='gyro':
            self.s3=GyroSensorjl(Port.S3)
        elif sensor[2]=='touch':
            self.s3=TouchSensorjl(Port.S3)
        elif sensor[2]=='color':
            self.s3=ColorSensorjl(Port.S3)
        elif sensor[2]=='infrared':
            self.s3=InfraredSensorjl(Port.S3)
        elif sensor[2]=='ultrasonic':
            self.s3=UltrasonicSensorjl(Port.S3)
        else:
            pass
        if sensor[3]=='gyro':
            self.s4=GyroSensorjl(Port.S4)
        elif sensor[3]=='touch':
            self.s4=TouchSensorjl(Port.S4)
        elif sensor[3]=='color':
            self.s4=ColorSensorjl(Port.S4)
        elif sensor[3]=='infrared':
            self.s4=InfraredSensorjl(Port.S4)
        elif sensor[3]=='ultrasonic':
            self.s4=UltrasonicSensorjl(Port.S4)
        else:
            pass