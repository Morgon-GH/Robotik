#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()
StrasseL = Motor(Port.B)
StrasseM = Motor(Port.C)
StrasseR = Motor(Port.A)
Druck = TouchSensor(Port.S1)

statusL = 0
statusM = 0
statusR = 0

#programm
while True:
    if Button.LEFT in ev3.buttons.pressed():
        if statusL == 0:
            statusL = 1
        elif statusL == 1:
            statusL = 0
        while (Button.LEFT in ev3.buttons.pressed()):
            wait(10)

    if Button.LEFT in ev3.buttons.pressed():
        if statusM == 0:
            statusM = 1
        elif statusM == 1:
            statusM = 0
        while (Button.LEFT in ev3.buttons.pressed()):
            wait(10)

    if Button.RIGHT in ev3.buttons.pressed():
        if statusR == 0:
            statusR = 1
        if statusR == 1:
            statusR = 0
        while (Button.LEFT in ev3.buttons.pressed()):
            wait(10)

    if statusL == 1:
        StrasseL.run(-200)
    else:
        StrasseL.stop()

    if statusM == 1:
        StrasseM.run(-200)
    else:
        StrasseM.stop()

    if statusR == 1:
        StrasseR.run(-200)
    else:
        StrasseR.stop()


    if Druck.pressed():
        print('druck')

    wait(100)