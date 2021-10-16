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

import gc

## 3) Moduling Zone-----------------------------------------------------------------------------------------------------
##    

class Robotics_jomo(Customclass_jomo):
    '''Modul für eine Zentrale Robotersteuerung. Standartimports in der üblichen Ausführlichkeit benötigt.
    Preferences nutzen große Räder, im Abstand von 10cm. 
    '''

    #überschreiben
    class TouchSensor_jomo(TouchSensor, Customclass_jomo):
        #fill
    

    class ColorSensor_jomo(ColorSensor, Customclass_jomo):
        #fill
    

    class InfraredSensor_jomo(InfraredSensor, Customclass_jomo):
        #fill
    

    class UltrasonicSensor_jomo(UltrasonicSensor, Customclass_jomo):
        #fill
    

    class GyroSensor_jomo(GyroSensor, Customclass_jomo):
        #fill

    
    class DriveBase_jomo(DriveBase, Customclass_jomo):
        #fill

        def follow_line(self, line_color=Color.BLACK):
            ##

        ## Fahre bis Ultraschallsensor diesunddas..

        ## Fahre bis Farbsensor diesunddas..

        ## Fahre bis Hell/Dunkelsensor diesunddas..

        ## Folge der Linie mit der Farbe 'farbe' bis Sensor diesunddas..

        ## Beschleunige diesunddas

        ## makecourse für Abweichung des Winkels bei Gyro, korrigiert Kurs
    

    class Motor_jomo(Motor, Customclass_jomo):
        #fill
    

    #neue, eigene Klassen
    class Extension_jomo(Motor_jomo):
        #fill
    

    class Message_jomo(Customclass_jomo):
        #fill

        ## connect stelle verbindung her

        ## code_messg1 messagecodierer 1

        ## decode_messg1 messagedecodierer 1

        ## code_messg2 messagecodierer 2

        ## decode_messg2 messagedecodierer 2

        ## code_messg3 messagecodierer 3

        ## decode_messg3 messagedecodierer 3
        
        ## code_messg4 messagecodierer 4

        ## decode_messg4 messagedecodierer 4

        ## receive Nachricht empfangen

        ## send Nachricht senden


    def __init__(self, makeredo=True, wheel_diameter=45, axle_track=100,
     driveports=(Port.A, Port.D), extports=(Port.B, Port.C),
     sensor={'S1': 'gyro', 'S2': 'touch', 'S3': 'touch', 'S4': 'ultrasonic'}):
        if makeredo==True:
            do=RedoINTE_jomo()
        if driveports[0]!==' ':
            self.a=Motor_jomo(driveports[0])
        if driveports[1]!==' ':
            self.b=Motor_jomo(driveports[1])
        if extports[0]!==' ':
            self.c=Extension_jomo(extports[0])
        if extports[1]!==' ':
            self.d=Extension_jomo(extports[1])
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
        elif redo==2:
            do.redo2()
        elif redo==3:
            do.redo3()
        elif redo==4:
            do.redo4()
        elif redo==5:
            do.redo5()
        elif redo==6:
            do.redo6()
        elif redo==7:
            do.redo7()
        elif redo==8:
            do.redo8()
        elif redo==9:
            do.redo9()
        elif redo==10:
            do.redo10()