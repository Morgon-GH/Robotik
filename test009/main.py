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


#11cm

druck = 12
ev3 = EV3Brick()
color = ColorSensor(Port.S2)
color2 = ColorSensor(Port.S1)
motor = Motor(Port.B)
# ev3.screen.set_font()

while True:
    ambient2=color2.ambient()
    ambient=color.ambient()
    # print("ambient: " +str(ambient) + "   abmient2: " +str(ambient2))
    ev3.screen.clear()
    ev3.screen.draw_text(1,1,str(ambient))
    ev3.screen.draw_text(1,20,str(ambient2))
    if ambient2 > 11:
        if ambient < 11:
            motor.run_angle(100, druck)
            motor.run_angle(100, -druck)
    elif ambient2 < 11:
        if ambient > 2:
            motor.run_angle(100, druck)
            motor.run_angle(100, -druck) 
