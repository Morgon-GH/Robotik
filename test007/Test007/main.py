from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

ev3 = EV3Brick()
color = ColorSensor(Port.S2)
motor = Motor(Port.B)

while True:
    ambient=color.ambient()
    if ambient < 11:
        motor.run_angle(100,10)
        motor.run_angle(100,-10)