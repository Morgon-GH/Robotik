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
color = ColorSensor(Port.S2)
motor = Motor(Port.B)


# Write your program here.
while True:
    ambient=color.ambient()
    ev3.screen.clear()
    ev3.screen.print(ambient)
    if ambient < 11:
        ev3.speaker.beep()
        motor.run_angle(100,10)
        motor.run_angle(100,-10)
        ev3.speaker.beep()

