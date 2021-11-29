#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


# Create your objects here.
ev3 = EV3Brick()
#Druck = TouchSensor(Port.2)
StrasseL = Motor(Port.B)
StrasseM = Motor(Port.C)
StrasseR = Motor(Port.A)
playing = 0

# Write your program here.
while True:
    while not (Button.CENTER in ev3.buttons.pressed()):
        pass
    while (Button.CENTER in ev3.buttons.pressed()):
        playing = 1

    while playing == 1:
        StrasseR.run_time(-99,5000)
    
        StrasseM.run_time(-99,5000)

        StrasseL.run_time(-99,5000)