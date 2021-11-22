#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


#11cm

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
            motor.run_angle(100, 10)
            motor.run_angle(100, -10)
    elif ambient2 < 11:
        if ambient > 11:
            motor.run_angle(100, 10)
            motor.run_angle(100, -10) 
